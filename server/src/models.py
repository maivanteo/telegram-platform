# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, DECIMAL
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

Base = declarative_base()
metadata = Base.metadata


class Bot(Base):
    __tablename__ = 'bot'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), default="")
    username = Column(String(255), default=True)
    photo = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), default="")


class Client(Base):
    __tablename__ = 'client'

    # TODO: remove redundant client ID, User_ID is enough here
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, unique=True)
    first_name = Column(String(255), nullable=True)
    username = Column(String(255), nullable=True)
    balance = Column(DECIMAL(12, 2), nullable=True, default=0.00)  # TODO: obsolete
    language_code = Column(String(2), nullable=True)
    photo = Column(String(255), nullable=True)


class Sticker(Base):
    __tablename__ = 'sticker'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), default="")
    username = Column(String(255), default="")
    photo = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    installs = Column(Integer, default=0)
    language = Column(String(2), nullable=True, default='ru')


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    language = Column(String(2), nullable=False, default='ru')


class Channel(Base):
    __tablename__ = 'channel'

    # TODO: remove redundant channel ID, telegram ID is enough here
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    username = Column(String(255), nullable=True)
    photo = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    cost = Column(Integer, nullable=False, default=0)
    language = Column(String(2), nullable=False, default='ru')
    members = Column(Integer, nullable=False, default=0)
    members_growth = Column(Integer, nullable=False, default=0)
    views = Column(Integer, nullable=False, default=0)
    views_growth = Column(Integer, nullable=False, default=0)
    vip = Column(Boolean, default=False)
    verified = Column(Boolean, default=False)
    category_id = Column(ForeignKey('category.id'))
    likes = Column(Integer, nullable=False, default=0)
    mutual_promotion = Column(Boolean, default=False, nullable=False)

    category = relationship('Category')


class Session(Base):
    __tablename__ = 'session'

    # TODO: remove redundant session ID, session_id is enough here
    id = Column(Integer, primary_key=True)
    session_id = Column(String(255), nullable=False, unique=True)
    expiration = Column(DateTime)
    client_id = Column(ForeignKey('client.id'))
    client = relationship('Client')


class ChannelAdmin(Base):
    __tablename__ = 'channeladmin'

    # TODO: multicolumn primary key should be here
    id = Column(Integer, primary_key=True)
    channel_id = Column(ForeignKey('channel.id'), nullable=False)
    admin_id = Column(ForeignKey('client.id'), nullable=False)
    owner = Column(Boolean, nullable=False, server_default=expression.false())
    raw = Column(JSONB)

    admin = relationship('Client')
    channel = relationship('Channel')


class ChannelTag(Base):
    __tablename__ = 'channeltag'

    # TODO: multicolumn primary key should be here
    id = Column(Integer, primary_key=True)
    channel_id = Column(ForeignKey('channel.id'), nullable=False)
    tag_id = Column(ForeignKey('tag.id'), nullable=False)

    channel = relationship('Channel')
    tag = relationship('Tag')


class ChannelSessionAction(Base):
    __tablename__ = 'channelsessionaction'

    # TODO: multicolumn primary key should be here
    id = Column(Integer, primary_key=True)
    channel_id = Column(ForeignKey('channel.id'), nullable=False)
    session_id = Column(ForeignKey("session.id"), nullable=False)
    like = Column(Boolean, nullable=False)

    channel = relationship("Channel")
    session = relationship("Session")
    
    
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)

    client_id = Column(ForeignKey('client.id'), nullable=False)
    client = relationship('Client')

    amount = Column(DECIMAL(12, 2), nullable=False)
    currency = Column(String(5), nullable=False)
    opened = Column(DateTime)
    closed = Column(DateTime)
    result = JSONB()
