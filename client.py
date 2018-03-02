# Author:Win_Li   23147
# Date:2018-02-11 22:56
# 客户端（上传端）
import socket
import os

# 连接到服务端
sk = socket.socket()
address = ('127.0.0.1', 8001)
sk.connect(address)
# 确定上传文件绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# 输入操作和文件，用'|'分割
inp = input('请输入‘命令|文件名')
cmd, file_name = inp.split('|')
# 拼接上传文件绝对路径
path = os.path.join(BASE_PATH, file_name)
# 获取上传文件的大小
file_size = os.stat(path).st_size
# 拼接文件信息
file_data = bytes('%s|%s|%s' % (cmd, file_name, file_size), 'utf8')
sk.send(file_data) # 发送文件信息到服务端
# 发送文件内容
with open(path, 'rb') as file:
    send_data = 0
    while send_data != file_size:
        f = file.read(1024)
        sk.send(f)
        send_data += len(f)
    print('上传成功！')


