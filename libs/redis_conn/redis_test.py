#coding=utf-8
import redis

conn = redis.Redis()
# String操作

conn.set('name', 'zhangsan')
# 在redis中设置值，默认不存在则创建，存在则修改
name = conn.get('name')
print("name = " + name + str(type(name)))  # name = zhangsan


