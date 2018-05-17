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

# from django.db import models

from django.db import models

class Operation_log(models.Model):
    operator = models.CharField(max_length=100, null=True)
    operation_type = models.CharField(max_length=100)
    operation_detail = models.TextField(max_length=1000)
    result = models.BooleanField()
    when_created = models.DateTimeField()

    def toDic(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

    def toArray(self):
        # return [getattr(self, attr) for attr in [f.name for f in self._meta.fields]]
        return [self.id, str(self.operator), str(self.operation_type), str(self.operation_detail), str(self.result), self.when_created.strftime("%Y-%m-%d")]
        # return [self.id, self.operator, self.operation_type, self.operation_detail, self.result, self.when_created.strftime("%Y-%m-%d")]















