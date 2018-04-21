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

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),

    (r'^t_bi_banner', 't_bi_banner'),
    (r'new_promote', 'new_promote'),
    (r'promote_expand', 'promote_expand'),
    (r'^store_query', 'store_query'),
    (r'rrrrr', 'add_promote_record'),
    (r'^except_store_query', 'except_store_query'),
    (r'^except_store_id_post', 'except_store_id_post'),
    (r'^submit_query_storeid_url', 'submit_query_storeid_url'),
    (r'^addTo_exceptStore', 'addTo_exceptStore'),
    (r'^removeFrom_exceptStore', 'removeFrom_exceptStore'),
)