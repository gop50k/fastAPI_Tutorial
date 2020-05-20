# coding: UTF-8
from models import *
import db
import os

# テーブル作成、サンプルデータ注入
if __name__ == '__main__':
    path = SQLITE3_NAME
    if not os.path.isfile(path):

        # テーブル作成
        Base.metadata.create_all(db.engine)

    # サンプルユーザ作成
    admin = User(username='admin', password='fastapi', mail='hoge@example.com')
    db.session.add(admin) # 追加
    db.session.commit()

    # サンプルタスク
    task = Task(
        user_id=admin.id,
        content='Testdataの締め切り',
        deadline=datetime(2020, 5, 30, 12, 00, 00),
    )
    print(task)
    db.session.add(task)
    db.session.commit()

    db.session.close() # セッションを閉じる
