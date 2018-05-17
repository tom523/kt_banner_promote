from home_application.models import Operation_log
import datetime


def success(username, operation_type, operation_detail):
    Operation_log.objects.create(operator=username, operation_type=operation_type,
                                 operation_detail=operation_detail,
                                 result="success", when_created=datetime.datetime.now())


def fail(username, operation_type, operation_detail):
    Operation_log.objects.create(operator=username, operation_type=operation_type,
                                 operation_detail=operation_detail,
                                 result="fail", when_created=datetime.datetime.now())

















