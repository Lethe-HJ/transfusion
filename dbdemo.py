# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
from datetime import datetime
from string import printable

from pbkdf2 import PBKDF2

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)
from enum import Enum
from libs.db.dbsession import Base, dbSession
from sqlalchemy_enum34 import EnumType


# 连接数据库的数据
HOSTNAME = '47.106.83.135'
PORT = '3306'
DATABASE = 'hospital'
USERNAME = 'admin'
PASSWORD = 'alimysqladmin'
# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
DB_URI = url.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)


# 1创建一个engine引擎
engine = create_engine(DB_URI, echo=False )
# 2sessionmaker生成一个session类
Session = sessionmaker(bind=engine)
# 3创建一个session实例
dbSession = Session()
# 4创建一个模型基类
Base = declarative_base(engine)





class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    _password = Column('password', String(64), nullable=False)
    createtime = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime)
    last_login = Column(DateTime)
    loginnum = Column(Integer, default=0)
    email = Column(String(50))
    mobile = Column(String(50))
    num = Column(String(50), unique=True)

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()  # 查询所有

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()  # 通过字段查询

    def auth_password(self, otherpassword):
        if self._password is not None:
            return self._password == otherpassword
        else:
            return False

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()

    def _hash_password(self, password):
        return PBKDF2.crypt(password, iterations=0x2537)  # 返回加密后的密码

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.name,
            'last_login': self.last_login,
        }



class Pt_bs_msg(Base):
    __tablename__ = 'pt_bs_msg'
    tret_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    bednum = Column(String(50))
    name = Column(String(50), nullable=False)
    gender = Column(String(10), default='未知')
    age = Column(Integer)
    contact = Column(String(50))
    doctor = Column(String(50))
    IDcard = Column(String(50), nullable=False)
    ill = Column(String(50))

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()  # 查询所有

    @classmethod
    def by_tret_id(cls, tret_id):
        return dbSession.query(cls).filter_by(tret_id=tret_id).first()  # 通过字段查询

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name)

    @classmethod
    def by_doctor(cls, doctor):
        return dbSession.query(cls).filter_by(doctor=doctor)

    @classmethod
    def by_IDcard(cls, IDcard):
        return dbSession.query(cls).filter_by(IDcard=IDcard)


class case_history(Base):
    __tablename__ = 'case_history'
    IDcard = Column(String(18))
    dpt = Column(String(50))
    family = Column(String(50))
    HPC = Column(String(200))
    PMH = Column(String(50))
    PH = Column(String(50))
    FH = Column(String(50))
    PS = Column(String(50))
    nurse = Column(String(18))

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()  # 查询所有

    @classmethod
    def by_IDcard(cls, IDcard):
        return dbSession.query(cls).filter_by(IDcard=IDcard).first()  # 通过字段查询