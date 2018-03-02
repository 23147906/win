#Author:Win_Li   23147
#Date:2018-01-14 23:52

#通过当前执行文件的路径，定位它的绝对路径，当程序环境变化时，程序依然可用。
import os ,sys
# print(__file__)

# os.path.abspath(__file__)  #当前文件路径
# os.path.dirname(os.path.abspath(__file__)) #当前文件上级路径
# os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前文件上上级路径
# os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #当前文件上上上级路径

file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(file_path)