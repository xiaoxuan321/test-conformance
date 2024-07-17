# 使用Python 3.9官方基础镜像
FROM python:3.9

# 创建工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器的/app 目录
COPY . /app

# 安装所需依赖
RUN pip install pm4py


