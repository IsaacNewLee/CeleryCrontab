from celery.schedules import crontab
from datetime import timedelta

BROKER_URL = 'redis://127.0.0.1:6379'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'                   # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'                             

CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2'
)
# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=30),          # 每 30 秒执行一次
        'args': (5, 8)                              # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=10, minute=50),      # 每天早上 10 点 50 分执行一次
        'args': (3, 7)                                # 任务函数参数
    }
}
