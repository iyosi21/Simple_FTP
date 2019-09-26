# -*- coding: utf8 -*-
import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import socket
import os.path

# ローカルホストのIPアドレスを取得
host = socket.gethostname
ip = socket.gethostbyname(host)

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
