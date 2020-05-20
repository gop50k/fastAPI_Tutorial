# coding: UTF-8
from urls import app
import uvicorn

# サーバを立ち上げる関数
if __name__ == '__main__':
    uvicorn.run(app=app)
