import os

DJANGO_ENV = os.getenv("DJANGO_ENV", "development")
REDIS_USER = ""  # redis用户
REDIS_PASSWORD = ""  # redis密码
if DJANGO_ENV == "production":
    REDIS_HOST = ""  # redis端口
    REDIS_PORT = 6379

else:
    REDIS_HOST = "r-wz9e3lgp7l0so3gyw1pd.redis.rds.aliyuncs.com"
    REDIS_PORT = 6379

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "decode_responses": False,
                "max_connections": 1000,
            },
        },
    }
}
