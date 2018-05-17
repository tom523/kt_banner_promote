# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST
from blueking.component.shortcuts import get_client_by_request
from common.log import logger
import json
from django.http import HttpResponse
from home_application.models_t_bi_banner import TBiBanner
import datetime
from django.db.models import Avg, Max
from home_application.models import Operation_log
from utils import Operation


def get_user_name(request):
    return request.user.username


def t_bi_banner(request):
    '''

    :param request:
    :return:
    '''
    # if request.method == "GET":
    #     kwargs = {
    #         "app_code": APP_ID,
    #         "app_secret": APP_TOKEN,
    #         "bk_token": request.COOKIES.get('bk_token', ''),
    #         "app_id": 5,
    #         "task_id": 1,
    #     }
    #     client = get_client_by_request(request)
    #     result = client.job.execute_task(kwargs)
    #     task_instance_id = result['data']['taskInstanceId']
    #     task_result = get_task_ip_log(client, task_instance_id, request)
    #     # logger.debug(task_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['logContent'])
    #     promote_table_data = task_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['logContent']
    items = []

    for item in TBiBanner.objects.using('t_bi_banner').all():

        if item.exceptstore is not None:
            exceptStore = "too long" if len(item.exceptstore)>10 else item.exceptstore
        else:
            exceptStore = None
        items.append({
            "bannerid": item.bannerid,
            "imgageUrl": item.imageurl,
            "Validfrom": item.validfrom.strftime("%Y-%m-%d %H:%M:%S"),
            "validto": item.validto.strftime("%Y-%m-%d %H:%M:%S"),
            "descCn": item.desccn,
            "position": item.position,
            "starttime": item.starttime,
            "endtime": item.endtime,
            "channelld": item.channelid,
            "exceptStore": exceptStore,
            "holiday": item.holiday,
            "dayofweek": item.dayofweek,
        })
    return render_json({
        "catalogues": {
            "bannerid": "id",
            "imgageUrl": "图片名称",
            "Validfrom": "开始日期",
            "validto": "截止日期",
            "descCn": "促销名称",
            "position": "排序号",
            "starttime": "开始时间",
            "endtime": "结束时间",
            "channelld": "外卖或堂食",
            "exceptStore": "餐厅编号（排除）",
            "holiday": "节假日",
            "dayofweek": "周几参与活动",
        },
        "items": items
    })


def get_task_ip_log(client, task_instance_id, request):
    kwargs = {
        "app_code": APP_ID,
        "app_secret": APP_TOKEN,
        "bk_token": request.COOKIES.get('bk_token', ''),
        "task_instance_id": task_instance_id,
    }
    result = client.job.get_task_ip_log(kwargs)
    if result['result']:
        if result["data"][0]["isFinished"]:
            return result
        else:
            import time
            time.sleep(10)
            return get_task_ip_log(client, task_instance_id, request)


def new_promote(request):
    return render_mako_context(request, '/home_application/new_promote.html')


# 活动延期
def promote_expand(request):
    new_expandto = request.GET.get('new_expandto')
    banner_id = request.GET.get('banner_id')

    cur = TBiBanner.objects.using('t_bi_banner').get(bannerid=banner_id)
    try:
        cur.promote_expand(new_expandto)
        Operation.success(request.user.username, "promote expanded", "banner_id:%s new_expandto:%s" % (banner_id, new_expandto))
        return render_json({
            "result": True
        })

    except:
        Operation.fail(request.user.username, "promote expanded", "banner_id:%s new_expandto:%s" % (banner_id, new_expandto))
        return render_json({
            "result": False
        })




def get_all_store(request):
    logger.info(u"开始查询所有营运状态的store信息")
    kwargs = {
        "app_code": APP_ID,
        "app_secret": APP_TOKEN,
        "bk_token": request.COOKIES.get('bk_token', ''),
        "app_id": 5,
        "task_id": 3,
    }
    client = get_client_by_request(request)
    result = client.job.execute_task(kwargs)
    task_instance_id = result['data']['taskInstanceId']
    task_result = get_task_ip_log(client, task_instance_id, request)
    d = eval(task_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['logContent'])
    store_tree_data = task_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['logContent']
    logger.info(store_tree_data[:100])
    return eval(store_tree_data)


# 查询某条记录的exceptStore字段,返回python对象
def query_exceptStore(request, banner_id):
    logger.info(u"开始查询banner_id=" + banner_id + u"的except_store_id")
    kwargs = {
        "app_code": APP_ID,
        "app_secret": APP_TOKEN,
        "bk_token": request.COOKIES.get('bk_token', ''),
        "app_id": 5,
        "task_id": 5,
        "steps": [{
            "stepId": 5,
            "ipList": "1:192.168.116.94",
            "scriptParam": banner_id,
        }]
    }
    client = get_client_by_request(request)
    result = client.job.execute_task(kwargs)
    task_instance_id = result['data']['taskInstanceId']
    task_result = get_task_ip_log(client, task_instance_id, request)
    d = eval(task_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['logContent'])
    excepted_store_ids = eval(task_result['data'][0]['stepAnalyseResult'][0]['ipLogContent'][0]['logContent'])
    logger.debug(excepted_store_ids)
    if excepted_store_ids[0][0] == None:
        return None
    else:
        return excepted_store_ids[0][0].split(',')


def _add_checked(request, store_tree_data, banner_id):
    excepted_store_ids = query_exceptStore(request,banner_id)
    # 如果except_store_id是none，就直接返回没加checked=true的树形数据
    # 如果except_store_id不是none，就往store_tree_data添加checked标识，用于前端显示已选择的门店
    if excepted_store_ids == None:
        logger.debug(excepted_store_ids)
        return store_tree_data
    else:
        logger.debug(type(store_tree_data))
        for market in store_tree_data:
            logger.debug(type(market))
            logger.debug(str(market)[:1000])
            for city in market['items']:
                logger.debug(str(city)[:1000])
                logger.debug(type(city))
                for district in city['items']:
                    logger.debug(type(district))
                    for store in district['items']:
                        logger.debug(type(store['id']))
                        excepted_store_ids_list = excepted_store_ids
                        logger.debug(excepted_store_ids_list[0])
                        logger.debug(excepted_store_ids)
                        if store['id'] in excepted_store_ids:
                            store['checked'] = True
                            logger.debug(store)
        return store_tree_data

def except_store_query(request):
    banner_id = request.GET.get('banner_id')
    store_tree_data = get_all_store(request)
    store_tree_data_checked = _add_checked(request, store_tree_data, banner_id)
    return render_json(store_tree_data_checked)




def store_query(request):
    return render_json(get_all_store(request))


def _format_join_day(join_day_str, join_day):
    if join_day == "true":
        join_day_str += "1"
    else:
        join_day_str += "0"
    return join_day_str


def format_join_day(join_sunday, join_monday, join_tuesday, join_wednesday, join_thursday, join_friday, join_saturday):
    join_day_str = ""
    join_day_str = _format_join_day(join_day_str, join_sunday)
    join_day_str = _format_join_day(join_day_str, join_monday)
    join_day_str = _format_join_day(join_day_str, join_tuesday)
    join_day_str = _format_join_day(join_day_str, join_wednesday)
    join_day_str = _format_join_day(join_day_str, join_thursday)
    join_day_str = _format_join_day(join_day_str, join_friday)
    join_day_str = _format_join_day(join_day_str, join_saturday)
    return join_day_str


def format_date(date):
    date_list = date.split('/')
    return date_list[2] + "-" + date_list[0] + "-" + date_list[1]


def add_promote_record(request):
    pic_name = request.POST.get('pic_name')
    logger.debug(request.POST.get('join_store'))
    not_join_store = request.POST.get('not_join_store')
    # if not_join_store != "":
    #     store_id_list = []
    #     for store_item in not_join_store:
    #         store_name = store_item['text']
    #         store_id = store_item['id']
    #         store_id_list.append(store_id)
    prmt_datarange = request.POST.get('prmt_datarange')
    prmt_time_start = request.POST.get('prmt_time_start')
    prmt_time_end = request.POST.get('prmt_time_end')
    prmt_descCN = request.POST.get('prmt_descCN')
    prmt_sortNum = request.POST.get('prmt_sortNum')
    prmt_wmts = request.POST.get('prmt_wmts')
    join_sunday = request.POST.get('join_sunday')
    join_monday = request.POST.get('join_monday')
    join_tuesday = request.POST.get('join_tuesday')
    join_wednesday = request.POST.get('join_wednesday')
    join_thursday = request.POST.get('join_thursday')
    join_friday = request.POST.get('join_friday')
    join_saturday = request.POST.get('join_saturday')
    join_holiday = request.POST.get('join_holiday')

    if join_holiday == "false":
        join_holiday_format = "Y"
    else:
        join_holiday_format ="N"

    bannerid = TBiBanner.objects.using('t_bi_banner').aggregate(Max('bannerid'))
    try:
        TBiBanner.objects.using('t_bi_banner').create(
            bannerid=bannerid['bannerid__max']+1,
            bannertype=1,
            imageurl=pic_name,
            relationtype=2,
            linkedclassid=None,
            linkedurl=1,
            validfrom=datetime.datetime.strptime(prmt_datarange.replace('&nbsp;', "").split('-')[0], "%m/%d/%Y"),
            validto=datetime.datetime.strptime(prmt_datarange.replace('&nbsp;', "").split('-')[1], "%m/%d/%Y"),
            desccn=prmt_descCN,
            descen=None,
            showorder=prmt_sortNum,
            position=1,
            starttime=prmt_time_start,
            endtime=prmt_time_end,
            market=None,
            city=None,
            smallpictureurl=None,
            ispopup=1,
            versionid=1,
            holiday=join_holiday_format,
            dayofweek=format_join_day(join_sunday, join_monday, join_tuesday, join_wednesday, join_thursday, join_friday, join_saturday),
            channelid=prmt_wmts,
            titlecn=prmt_descCN,
            titleen=None,
            briefcn=prmt_descCN,
            briefen=None,
            altdesc=None,
            cityselecttype=1,
            stypes=None,
            exceptstore=not_join_store,
        )
        Operation.success(request.user.username, "promote added", "pic_name:%s, prmt_descCN:%s" % (pic_name,prmt_descCN))
        return render_json({
            "result": True
        })
    except Exception,e:
        Operation.fail(request.user.username, "promote added", "pic_name:%s, prmt_descCN:%s" % (pic_name,prmt_descCN))
        return render_json({
            "result": False
        })




def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')



# 门店活动到期
def add_storeid_to_exceptStore(request):
    store_id_list = request.GET.getlist('data[]')
    banner_id = request.GET.get('banner_id')
    cur = TBiBanner.objects.using('t_bi_banner').get(bannerid=banner_id)
    try:
        cur.add_storeids_to_exceptstore(store_id_list)
        Operation.success(request.user.username, "promote ended", "banner_id:%s store_id_list:%s" % (banner_id, store_id_list))
        return render_json({
            "result": True,
        })

    except:
        Operation.fail(request.user.username, "promote ended", "banner_id:%s store_id_list:%s" % (banner_id, store_id_list))
        return render_json({
            "result": False,
        })



def history(request):
    data = []
    for oper in Operation_log.objects.all():
        data.append(oper.toArray())
    return render_mako_context(request, 'home_application/history.html', {"data": data})
