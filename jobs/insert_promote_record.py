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




def getCursor(db):
    return db.cursor()


def insert_promote_record():
    db = MySQLdb.connect("192.168.116.94", "dicos", "000000", "dicos_ios", charset='utf8')
    imageUrl = sys.argv[1]
    validfrom = sys.argv[2]
    validto = sys.argv[3]
    startTime = sys.argv[4]
    endTime = sys.argv[5]
    descCn = sys.argv[6]
    showOrder = sys.argv[7]
    channelId = sys.argv[8]
    dayOfWeek = sys.argv[9]
    holiday = sys.argv[10]
    exceptStore = sys.argv[11]

    # print imageUrl
    # print validfrom
    # print validto
    # print startTime
    # print endTime
    # print descCn
    # print showOrder
    # print channelId
    # print dayOfWeek
    # print holiday
    # print exceptStore


    cursor = getCursor(db)
    cursor.execute('select bannerid from t_bi_banner')
    id_list = cursor.fetchall()
    bannerid = id_list[-1][0]+1
    sql_insert = 'insert t_bi_banner(bannerid, imageUrl, bannertype, relationType, linkedUrl, validfrom, validto, descCn, ' \
                 'showOrder, position, startTime, endTime, isPopup, versionId' \
                 ', holiday, dayOfWeek, channelId, titleCn, briefCn, citySelectType, exceptStore)' \
                 ' values("'+str(bannerid)+'", "' + imageUrl  + '", "1", "2", "1", "' + validfrom + '", "'+ validto + '", "'+ descCn +'", "'+showOrder+'", "1", "'+startTime+'", "'+endTime+'", "1", "1", "'+holiday+'", "'+dayOfWeek+'", "'+channelId+'", "'+descCn+'", "'+descCn+'", "1", "'+exceptStore+'"); '
    # retdata = cursor.execute(sql_insert, (imageUrl, validfrom, validto, descCn, showOrder, startTime, endTime, holiday, dayOfWeek, channelId, descCn, descCn, exceptStore))
    retdata = cursor.execute(sql_insert)
    db.commit()
    print(retdata)
    db.close()


if __name__ == '__main__':

    # job_start()

    ###### 可在此处开始编写您的脚本逻辑代码
    ###### iJobs中执行脚本成功和失败的标准只取决于脚本最后一条执行语句的返回值
    ###### 如果返回值为0，则认为此脚本执行成功，如果非0，则认为脚本执行失败

    insert_promote_record()



