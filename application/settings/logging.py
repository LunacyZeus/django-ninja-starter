# # ================================================= #
# # ********************* 日志配置 ******************* #
# # ================================================= #
# # log 配置部分BEGIN #
import os

from application.settings import BASE_DIR

PROJECT_DIR = BASE_DIR.parent

SERVER_LOGS_FILE = os.path.join(PROJECT_DIR, "logs", "server.log")
ERROR_LOGS_FILE = os.path.join(PROJECT_DIR, "logs", "error.log")
LOGS_FILE = os.path.join(PROJECT_DIR, "logs")
if not os.path.exists(os.path.join(PROJECT_DIR, "logs")):
    os.makedirs(os.path.join(PROJECT_DIR, "logs"))

# 格式:[2020-04-22 23:33:01][micoservice.apps.ready():16] [INFO] 这是一条日志:
# 格式:[日期][模块.函数名称():行号] [级别] 信息
STANDARD_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)
CONSOLE_LOG_FORMAT = (
    "[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"
)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": STANDARD_LOG_FORMAT},
        "console": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file": {
            "format": CONSOLE_LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": SERVER_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 5,  # 最多备份5个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ERROR_LOGS_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 3,  # 最多备份3个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "demo": {  # 记录到日志文件(需要创建对应的目录，否则会出错)
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(PROJECT_DIR, "logs", "demo.log"),  # 日志输出文件
            "maxBytes": 1024 * 1024 * 10,  # 文件大小
            "backupCount": 5,  # 备份份数
            "formatter": "standard",  # 使用哪种formatters日志格式
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
        },
        "django": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console", "error", "file"],
            "propagate": False,
            "level": "INFO",
        },
        "uvicorn.error": {
            "level": "INFO",
            "handlers": ["console", "error", "file"],
        },
        "uvicorn.access": {
            "handlers": ["console", "error", "file"],
            "level": "INFO",
        },
    },
}
