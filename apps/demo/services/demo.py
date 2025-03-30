import logging

from apps.demo.schemes.demo import HelloOut

logger = logging.getLogger("demo")


def hello(user: str) -> HelloOut:
    logger.debug("日志打印测试")
    return HelloOut(msg=f"hello,{user}")
