import os

HELLO_MESSAGE="Hello, World!"
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "")  # connect Yandex
SQLALCHEMY_TRACK_MODIFICATIONS = False
