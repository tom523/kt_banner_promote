# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String, create_engine, Integer, Date, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pickle

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class T_bi_banner(Base):
    # 表的名字:
    __tablename__ = 't_bi_banner'

    # 表的结构:
    bannerid = Column(Integer, primary_key=True)
    bannertype = Column(Integer)
    imageUrl = Column(String(100))
    relationType = Column(Integer)
    linkedClassid = Column(String(10))
    linkedUrl = Column(String(100))
    validfrom = Column(Date)
    validto = Column(Date)
    descCn = Column(String(500))
    descEn = Column(String(500))
    showOrder = Column(Integer)
    position = Column(Integer)
    startTime = Column(String(5))
    endTime = Column(String(5))
    market = Column(String(500))
    city = Column(String(500))
    smallPictureUrl = Column(String(50))
    isPopup = Column(String(1))
    versionId = Column(Integer)
    holiday = Column(String(1))
    dayOfWeek = Column(String(100))
    channelId = Column(String(100))
    titleCn = Column(String(100))
    titleEn = Column(String(100))
    briefCn = Column(String(100))
    briefEn = Column(String(100))
    altDesc = Column(String(100))
    citySelectType = Column(SmallInteger)
    stypes = Column(String(200))
    exceptStore = Column(String(15000))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://dicos:000000@192.168.116.94:3306/dicos_ios')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()
user = session.query(T_bi_banner).all()
print pickle.dumps(user)
