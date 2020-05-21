# coding: UTF-8
from controllers import *

# FastAPIのルーティング用関数,URLの登録
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
app.add_api_route('/register', register, methods=['GET', 'POST'])
