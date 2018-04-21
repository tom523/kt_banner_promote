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

if __name__ == '__main__':

    # job_start()

    ###### 可在此处开始编写您的脚本逻辑代码
    ###### iJobs中执行脚本成功和失败的标准只取决于脚本最后一条执行语句的返回值
    ###### 如果返回值为0，则认为此脚本执行成功，如果非0，则认为脚本执行失败
    db = MySQLdb.connect("192.168.116.94", "dicos", "000000", "dicos_ios", charset='utf8' )
    cursor = db.cursor()
    sql_select = 'SELECT t_bi_banner.bannerid,t_bi_banner.imageUrl,t_bi_banner.relationType,' \
                 't_bi_banner.linkedClassid,t_bi_banner.linkedUrl,date_format(t_bi_banner.validfrom, "%Y-%m-%d"),' \
                 'date_format(t_bi_banner.validto, "%Y-%m-%d"),t_bi_banner.descCn,t_bi_banner.descEn,t_bi_banner.bannertype,' \
                 't_bi_banner.showOrder,t_bi_banner.`position`,t_bi_banner.startTime,t_bi_banner.endTime,' \
                 't_bi_banner.market,t_bi_banner.city,t_bi_banner.smallPictureUrl,t_bi_banner.isPopup,' \
                 't_bi_banner.versionId,t_bi_banner.holiday,t_bi_banner.`dayOfWeek`,t_bi_banner.channelId,' \
                 't_bi_banner.titleCn,t_bi_banner.titleEn,t_bi_banner.briefCn,t_bi_banner.briefEn,' \
                 't_bi_banner.altDesc,t_bi_banner.citySelectType,t_bi_banner.stypes,' \
                 't_bi_banner.exceptStore FROM t_bi_banner'
    cursor.execute(sql_select)
    data = cursor.fetchall()
    print data
    db.close()

