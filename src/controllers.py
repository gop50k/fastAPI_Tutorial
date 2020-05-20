# coding: UTF-8
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import db
from models import User, Task

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
    # ユーザとタスクを取得
    # 現段階では、adminユーザのみを取得
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()

    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'user': user,
                                       'task': task})
