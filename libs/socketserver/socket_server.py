# encoding=utf-8

from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
from libs.redis_conn.redis_conn import conn
# from libs.socketserver.command_parsing import parsing
class Connection(object):
    clients = set()

    def __init__(self, stream, address):
        Connection.clients.add(self)
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)
        self.read_message()
        self.data = ''
        print("A new user has entered the chat room.", address)

    def read_message(self):  # 读信息
        self._stream.read_until('\n', self.broadcast_messages)

    def broadcast_messages(self, data):  # 广播信息
        self.data = data[:-1]  # 这里的data好像只有一个元素
        print("User_bak said:", self.data, self._address)
        # for conn in Connection.clients:
        #     conn.send_message(data)
        conn.rpush('msg_li', self.data)  # 储存在缓存中的msg_li列表的最右端
        print(conn.lindex('msg_li', -1))
        print("command = " + self.data)
        msg = parsing.get_command()  # 从redis中获得最近的消息
        parsing.parse_command(msg)  # 解析消息
        self.read_message()

    def send_message(self, data):  # 发送信息
        self._stream.write(bytes(data))

    def on_close(self):
        print("A user has left the chat room.", self._address)
        Connection.clients.remove(self)

    def get_data(self):
        print("储存的data值为" + str(self.data))
        return self.data


class ChatServer(TCPServer):
    def handle_stream(self, stream, address):
        print("New connection :", address, stream)
        Connection(stream, address)
        print("connection num is:", len(Connection.clients))

    @classmethod
    def send_msg_to_client(cls, msg, client, encode):
        print('[host said] : "' + str(msg) + '"')
        for conn in Connection.clients:
            conn.send_message(msg.encode(encode))


