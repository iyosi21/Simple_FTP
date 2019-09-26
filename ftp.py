# -*- coding: utf8 -*-
#参考：https://qiita.com/castaneai/items/8cb7cd3253275e7cf617
#     すぐ作ってすぐ壊せるFTPサーバーを立てる (Pythonで)
import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import socket
import os.path

# ローカルホストのIPアドレスを取得
# 複数IPアドレスを設定している場合はうまく行かない。
ip = socket.gethostbyname(socket.gethostname())

# 実行ファイルのパスを取得
cur_path = os.path.dirname(__file__)

# 認証ユーザーを作る
authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user('user', 'password', cur_path, perm='elradfmw')

# 個々の接続を管理するハンドラーを作る
handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = authorizer

# FTPサーバーを立ち上げる
server = pyftpdlib.servers.FTPServer((ip, 21), handler)
server.serve_forever()
