import json
from typing import Optional

import redis
from django_redis import get_redis_connection


# 数据处理队列
class DataQueue:
    def __init__(self, alias: str = "1"):
        self.key_name = f"data-{alias}"
        self.conn: redis.Redis = get_redis_connection("default")

    def push(self, value: any) -> None:
        """向队列尾部添加一个元素"""
        if not isinstance(value, str):  # 不为str需要格式化
            value = json.dumps(value)
        self.conn.rpush(self.key_name, value)

    def pop(self) -> Optional[any]:
        """从队列头部弹出一个元素"""
        item = self.conn.lpop(self.key_name)
        return json.loads(item) if item else None

    def length(self) -> int:
        """获取队列长度"""
        return self.conn.llen(self.key_name)

    def get_all(self) -> list[str]:
        """获取队列中的所有元素"""
        return self.conn.lrange(self.key_name, 0, -1)

    def clear(self) -> None:
        """清空队列"""
        self.conn.delete(self.key_name)
