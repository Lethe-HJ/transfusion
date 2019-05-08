# coding=utf-8
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


class User_bak(Base):
    """用户表"""
    __tablename__ = 'user_bak'

    id = Column(Integer, primary_key=True, autoincrement=True)

    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))  # 生成一个随机的UUID
    name = Column(String(50), nullable=False)

    _password = Column('password', String(64), nullable=False)
    createtime = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime)
    last_login = Column(DateTime)


    loginnum = Column(Integer, default=0)
    _locked = Column(Boolean, default=False, nullable=False)
    _avatar = Column(String(64))  # 头像字段
    _isdelete = Column(Boolean, default=False, nullable=False)

    email = Column(String(50))
    mobile = Column(String(50))
    num = Column(String(50), unique=True)
    qq = Column(String(50))





    @classmethod
    def all(cls):
        return dbSession.query(cls).all()  # 查询所有

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()  # 通过字段查询

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()

    def _hash_password(self, password):
        return PBKDF2.crypt(password, iterations=0x2537)  # 返回加密后的密码

    @property
    def password(self):
        return self._password

    @password.setter  # 密码设置时触发的装饰器
    def password(self, password):
        # print self._hash_password(password)
        self._password = self._hash_password(password)

    def auth_encrypsd(self, other_password):
        if self._password is not None:
            return self.password == PBKDF2.crypt(other_password, self.password)  # 返回密码匹配的结果
        else:
            return False

    def auth_password(self, otherpassword):
        if self._password is not None:
            return self._password == otherpassword
        else:
            return False

    @property  # 属性方法
    def avatar(self):
        return self._avatar if self._avatar else "default_avatar.jpeg"

    @avatar.setter
    def avatar(self, image_data):
        class ValidationError(Exception):
            def __init__(self, message):
                super(ValidationError, self).__init__(message)
        if 64 < len(image_data) < 1024 * 1024:
            import imghdr
            import os
            ext = imghdr.what("", h=image_data)
            print ext
            print self.uuid
            if ext in ['png', 'jpeg', 'jpg', 'gif', 'bmp'] and not self.is_xss_image(image_data):
                if self._avatar and os.path.exists("static/images/useravatars/" + self._avatar):
                    os.unlink("static/images/useravatars/" + self._avatar)
                file_path = str("static/images/useravatars/" + self.uuid + '.' + ext)
                with open(file_path, 'wb') as f:
                    f.write(image_data)
                self._avatar = self.uuid + '.' + ext
            else:
                raise ValidationError("not in ['png', 'jpeg', 'gif', 'bmp']")
        else:
            raise ValidationError("64 < len(image_data) < 1024 * 1024 bytes")

    def is_xss_image(self, data):
        return all([char in printable for char in data[:16]])

    @property
    def locked(self):
        return self._locked
    
    @locked.setter
    def locked(self, value):
        assert isinstance(value, bool)  # 检查value是否是boll对象
        self._locked = value

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.name,
            'last_login': self.last_login,
        }


class User_new(Base):
    """用户表"""
    __tablename__ = 'user_new'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(50), nullable=False)

    _password = Column('password', String(64), nullable=False)
    createtime = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime)
    last_login = Column(DateTime)

    loginnum = Column(Integer, default=0)
    _locked = Column(Boolean, default=False, nullable=False)
    _avatar = Column(String(64))  # 头像字段
    _isdelete = Column(Boolean, default=False, nullable=False)

    email = Column(String(50))
    mobile = Column(String(50))
    num = Column(String(50), unique=True)
    qq = Column(String(50))

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()  # 查询所有

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()  # 通过字段查询

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()

    @property
    def password(self):
        return self._password


    def auth_password(self, otherpassword):
        if self._password is not None:
            return self._password == otherpassword
        else:
            return False

    @property  # 属性方法
    def avatar(self):
        return self._avatar if self._avatar else "default_avatar.jpeg"





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



class pt_bs_msg(Base):
    __tablename__ = 'pt_bs_msg'
    tret_id = Column(Integer, primary_key=True)
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
        return dbSession.query(cls).filter_by(IDcard=IDcard).first()

    @classmethod
    def by_bednum(cls, bednum):
        return dbSession.query(cls).filter_by(bednum=bednum).first()


class case_history(Base):
    __tablename__ = 'case_history'
    IDcard = Column(String(18), primary_key=True)
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


class Prescription(Base):
    __tablename__ = "prescription"
    tret_id = Column(Integer, primary_key=True)
    medicine_msg = Column(Text(100))
    drug_id_msg = Column(Text(100))

    @classmethod
    def by_tret_id(cls, tret_id):
        return dbSession.query(cls).filter_by(tret_id=tret_id).first()  # 通过字段查询


class Bed_rack(Base):
    __tablename__ = "bed_rack"
    bednum = Column(String(50),primary_key=True)
    rack = Column(String(50),unique=True)

    @classmethod
    def by_bednum(cls, bednum):
        return dbSession.query(cls).filter_by(bednum=bednum).first()

class Drug(Base):
    __tablename__ = "drug"
    id = Column(String(50),primary_key=True)
    drug_name = Column(String(50))

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()