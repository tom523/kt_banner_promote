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
    # new_expandto = '2018-08-13'
    # banner_id = '3'
    except_store_ids = sys.argv[1]
    banner_id = sys.argv[2]
    db = MySQLdb.connect("192.168.116.94", "dicos", "000000", "dicos_ios", charset='utf8' )
    cursor = db.cursor()
    id_list = except_store_ids.split(',')
    for id in id_list:
        sql_update_exceptStore = "update t_bi_banner set exceptStore = REPLACE(exceptStore, '" + id + "', '') where bannerid=" + banner_id
        # sql_update_validto = "update t_bi_banner set validto = DATE('%s') where bannerid='%s'"
        retdata = cursor.execute(sql_update_exceptStore)
        # retdata = cursor.execute(sql_update_validto % (new_expandto, banner_id))
        if str(retdata) == "1":
            continue
        else:
            print retdata
            break
    print retdata
    db.commit()
    db.close()


# 脚本返回1 则执行成功
