# -*- coding: utf8 -*-
#参考：https://qiita.com/castaneai/items/8cb7cd3253275e7cf617
#     すぐ作ってすぐ壊せるFTPサーバーを立てる (Pythonで)
# -*- coding: utf8 -*-
import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import socket
import os.path

#認証情報
user = "user"
password = "password"

# ローカルホストのIPアドレスを取得
ip = socket.gethostbyname_ex(socket.gethostname())

#複数IPアドレスがあることを想定して、選んでもらう。
i2 = 1
for i in ip[2]:
    print(str(i2) + ":" + str(i))
    i2 = i2 + 1

ip_select = int(input("Please select the IP Address number to use from 1 to N:"))
#番号選択と入力があわないと終了
if len(ip[2]) < ip_select:
    key = input("not found ip address")
    exit

#使用するIPアドレスを代入
ip_use = ip[2][ip_select - 1]

# 実行ファイルのパスを取得
cur_path = os.path.dirname(__file__)

# 認証ユーザーを作る
authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user(user, password, cur_path, perm='elradfmw')

# 個々の接続を管理するハンドラーを作る
handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = authorizer

#メッセージ表示
print("Starting FTP Server from " + str(ip_use) + ":21. username:" + str(user) + " password:" + str(password) + " current:" + str(cur_path))

# FTPサーバーを立ち上げる
server = pyftpdlib.servers.FTPServer((ip_use, 21), handler)
server.serve_forever()
