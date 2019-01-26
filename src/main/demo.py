import os

env_dist = os.environ # environ是在os.py中定义的一个dict environ = {}

# print env_dist.get('LD_LIBRARY_PATH')
# print(env_dist['LD_LIBRARY_PATH'])
os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda/lib64/'
# 打印所有环境变量，遍历字典
for key in env_dist:
    print(key + ' : ' + env_dist[key])
