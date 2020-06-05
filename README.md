# poseanalysis
安装说明
目前软件可以在以下的环境配置下运行。
操作系统：Window10
外部工具依赖：openpose 1.5.1发行版
一系列python库的环境依赖（具体可参考我们github 的requirements.txt）
Unity 2018.4.12

![示意图](https://github.com/gangsterless/poseanalysis/tree/master/readmeimg/1.jpg)


1 首先保证正确安装openpose ：
option1：可以参考openpose的官方安装配置教程

option2：也可以直接用发行版：
推荐下载GPU版本，
若想达到近似实时最低配置为： 1660ti 6G显存。
https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases

2 安装3dposebaseline
https://github.com/ArashHosseini/3d-pose-baseline
安装完毕后务必按要求下载预训练模型否则无法运行。

3 安装本软件

程序的入口在 main.py
主要依赖的库有：

cligj==0.5.0
colorama==0.4.1
graphviz==0.13.2
greenlet==0.4.15
grpcio==1.25.0
h5py==2.10.0
Jinja2==2.10.3
joblib==0.14.0
MarkupSafe==1.1.1
matplotlib==3.1.0
mistune==0.8.4
mock==3.0.5
more-itertools==8.0.2
oauthlib==3.1.0
opencv-python==4.1.1.26
opt-einsum==3.2.0
packaging==19.2
pandas==0.25.3
pandocfilters==1.4.2
pyproj==2.4.2.post1
scikit-image==0.16.2
scikit-learn==0.21.3
scipy==1.4.1
seaborn==0.9.0
selenium==3.141.0
Send2Trash==1.5.0
Shapely==1.6.4.post2
zipp==0.6.0
具体请参考 requirements.txt

或执行
pip install -r requirements.txt
