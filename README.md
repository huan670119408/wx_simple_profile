# 简单微信画像

#### 介绍
扫码登陆WEB版微信，生成词云、好友统计图表发送给文件助手。
![词云](images/example1.png)
![饼图](images/example2.png)
![地理坐标系](images/example3.png)


#### 参考
[1] [知乎](https://zhuanlan.zhihu.com/p/26514576)

[2] [itChat](https://github.com/littlecodersh/ItChat)

[3] [pyecharts](http://pyecharts.org/#/zh-cn/prepare)


#### 软件架构
python 3.7.1


#### 安装教程

安装 [itChat](https://github.com/littlecodersh/ItChat) `pip3 install itchat`

安装 [pyecharts](http://pyecharts.org/#/zh-cn/prepare) `pip3 install pyecharts`

安装 [nodejs](https://nodejs.org/en/download/)

安装 phantomjs `npm install -g phantomjs-prebuilt`

安装 [pyecharts-snapshot](http://pyecharts.org/#/zh-cn/prepare) `pip3 install pyecharts-snapshot`

安装 [jieba](https://github.com/fxsjy/jieba) `pip3 install jieba`

#### 使用说明

运行__main__.py，微信扫码登陆后图片会陆续发送给文件助手
