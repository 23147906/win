# Author:Win_Li   23147
# Date:2018-02-11 22:56
# 服务端（接收端）
import socket
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) # 获取绝对路径

# 绑定IP，端口
sk = socket.socket()
address = ('127.0.0.1', 8001)
sk.bind(address)
sk.listen(3)
conn, adr = sk.accept()

# 文件的信息 cmd-操作  file_name-文件名 file_size-文件大小
data = conn.recv(1024)
cmd, file_name, file_size = str(data, 'utf8').split('|')
file_size = int(file_size)
# 拼接接收路径
path = os.path.join(BASE_PATH, 'data', file_name)
# 接收文件
with open(path, 'ab') as file:
    receve_data = 0
    while receve_data != file_size:
        data = conn.recv(1024)
        file.write(data)
        receve_data += len(data)
    print('接收完成！')


