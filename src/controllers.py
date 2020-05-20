# coding: UTF-8
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

# FastAPI インスタンスの作成, レスポンス処理用
app = FastAPI(
    title='toDo app made by Fastapi',
    description='toDo app made by Fastapi & starlette',
    version='0.9beta'
)

# テンプレート関連の設定(jinja2)
templates = Jinja2Templates(directory='templates')
jinja_env = templates.env

def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})

def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'username': 'admin'})
