#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime
import os
import sys
import MySQLdb

def _now(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)

##### 可在脚本开始运行时调用，打印当时的时间戳及PID。
def job_start():
    print "[%s][PID:%s] job_start" % (_now(), os.getpid())

##### 可在脚本执行成功的逻辑分支处调用，打印当时的时间戳及PID。
def job_success(msg):
    print "[%s][PID:%s] job_success:[%s]" % (_now(), os.getpid(), msg)
    sys.exit(0)

##### 可在脚本执行失败的逻辑分支处调用，打印当时的时间戳及PID。
def job_fail(msg):
    print "[%s][PID:%s] job_fail:[%s]" % (_now(), os.getpid(), msg)
    sys.exit(1)


def getCursor():
    db = MySQLdb.connect("192.168.116.94", "dicos", "000000", "dicos_ios", charset='utf8' )
    return db.cursor()


def getStoreTreeData():
    cursor = getCursor()
    sql_select = 'select MarketCode,MarketName from market'
    cursor.execute(sql_select)
    marketCodes = cursor.fetchall()
    storeTreeData = []
    for item in marketCodes:
        marketCode = item[0]
        marketName = item[1]
        sql_select = 'select CityCode,CityName_zh from city where marketCode="%s"'
        cursor.execute(sql_select % (marketCode,))
        citys = cursor.fetchall()
        citys_in_market = []
        for item in citys:
            cityCode = item[0]
            cityName = item[1]
            sql_select = 'select DistrictCode, DistrictName from district where cityCode="%s"'
            cursor.execute(sql_select % (cityCode,))
            districts = cursor.fetchall()
            district_in_citys = []
            for item in districts:
                districtCode = item[0]
                districtName = item[1]
                sql_select = 'select StoreCode, StoreName from store where DistrictCode="%s" and Status=1'
                cursor.execute(sql_select % (districtCode,))
                stores = cursor.fetchall()
                stores_in_district = []
                for store in stores:
                    storeCode = store[0]
                    storeName = store[1]
                    stores_in_district.append({
                        "id": storeCode,
                        "text": storeName,
                    })
                district_in_citys.append({
                    "id": districtCode,
                    "text": districtName,
                    "items": stores_in_district,
                })
            citys_in_market.append({
                "id": cityCode,
                "text": cityName,
                "items": district_in_citys,
            })
        storeTreeData.append({
            "id": marketCode,
            "text": marketName,
            "items": citys_in_market,
        })
    return storeTreeData


if __name__ == '__main__':

    # job_start()

    ###### 可在此处开始编写您的脚本逻辑代码
    ###### iJobs中执行脚本成功和失败的标准只取决于脚本最后一条执行语句的返回值
    ###### 如果返回值为0，则认为此脚本执行成功，如果非0，则认为脚本执行失败

    storeTreeData = getStoreTreeData()
    print storeTreeData
    # for item_market in storeTreeData:
    #     print item_market['text']
    #     for item_city in item_market['items']:
    #         print "--" + item_city['text']
    #         for item_district in item_city['items']:
    #             print "----" + item_district['text']



