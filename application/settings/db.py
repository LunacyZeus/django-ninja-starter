# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("DJANGO_ENV", "production")

DJANGO_ENV = os.getenv("DJANGO_ENV", "production")

# 由于是demo项目默认用sqlite3测试 然后如果需要多租户请使用psycopg2
if DJANGO_ENV == "production":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# print(DATABASES)
