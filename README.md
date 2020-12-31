# HoshinoBot

Fork自[Ice-Cirno](https://github.com/Ice-Cirno)的[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)项目，但移除了大多数功能(主要是pcr功能)保留框架核心，帮助非pcr玩家接触和自定义HoshinoBot(其实是私用)。

**2020年8月2日0点，qq机器人框架相继停止维护。**
**感谢 酷Q项目 和 CQHTTP插件 的开发者们！感谢他们让Hoshino得以诞生！**
**Hoshino不再对酷Q进行支持**


## 简介

**HoshinoBot:** 基于 [nonebot](http://nonebot.cqp.moe) 框架，开源、无公害、非转基因的QQ机器人。


## 功能介绍

HoshinoBot原本主要功能请见[原文档](https://github.com/Ice-Cirno/HoshinoBot)，本fork项目保留的功能有：

- **入群欢迎**&**退群提醒**
- **复读**
- **机器翻译**
- **官方推特转发**
- **[蜜柑计划](http://mikanani.me)番剧更新订阅**
- **精致睡眠套餐**
- **反馈发送**：反馈内容将由bot私聊发送给维护组


-------------

### 功能模块控制

HoshinoBot 的功能繁多，各群可根据自己的需要进行开关控制，群管理发送 `lssv` 即可查看功能模块的启用状态，使用以下命令进行控制：

```
启用 service-name
禁用 service-name
```







## ~~部署指南~~

**由于酷Q已停止维护，您可以使用[CQHTTP Mirai](https://github.com/yyuueexxiinngg/onebot-kotlin)或[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)作为替代。由于当前mirai仍不稳定（甚至可能删库跑路），请自行参考相应的文档进行部署，本项目组不解答部署问题。**

本bot功能繁多，部分功能需要静态图片资源和带有认证的api key，恕不能公开。部分静态图片等资源请阅读源码后自行解决。

### 部署步骤

#### Windows 部署 (本地计算机或服务器)

1. 安装下面的软件/工具(编辑器在Notepad++和Visual Studio Code中选择一个即可)
    - Python 3.8：https://www.python.org/downloads/windows/
    - Git：https://git-scm.com/download/win
    - Notepad++：https://notepad-plus-plus.org/downloads/
    - Visual Studio Code：https://code.visualstudio.com/

2. 部署CQHTTP Mirai或go-cqhttp

    - CQHTTP Mirai：https://github.com/yyuueexxiinngg/onebot-kotlin
    - go-cqhttp：https://github.com/Mrs4s/go-cqhttp/

3. 修改CQHTTP的配置文件，下面的配置可供参考(若使用其他如cqps等bot需要打开并配置http_config)：

    ```hjson
    http_config: {
        enabled: false
        host: 0.0.0.0
        port: 5700
        timeout: 0
        post_urls: {}
    }
    ws_config: {
        enabled: false
        host: 0.0.0.0
        port: 6700
    }
    ws_reverse_servers: [
        {
            enabled: true
            reverse_url: ws://127.0.0.1:8080/ws/
            reverse_api_url: ws://you_websocket_api.server
            reverse_event_url: ws://you_websocket_event.server
            reverse_reconnect_interval: 3000
        }
    ]
    ```

    关于CQHTTP插件的配置说明，详见 [CQHTTP 文档 -> 配置](https://cqhttp.cc/docs/#/Configuration)

4. 打开一个合适的文件夹，点击资源管理器左上角的 `文件 -> 打开Windows Powershell`(或者其他本地shell工具)

5. 输入以下命令克隆本仓库并安装依赖

    ```powershell
    git clone https://github.com/Watanabe-Asa/HoshinoBot.git
    cd HoshinoBot
    py -3.8 -m pip install -r requirements.txt
    ```
    >若此处有报错信息，请务必解决，将错误信息复制到百度搜索一般即可找到解决办法。  
    >
    >若安装python依赖库时下载速度缓慢，可以尝试使用`py -3.8 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt`命令换源下载

6. 回到资源管理器，进入`hoshino`文件夹，将`config_example`文件夹重命名为`config`，然后右键使用所安装的编辑器打开其中的`__bot__.py`，按照其中的注释说明进行编辑。

    > 如果您不清楚某项设置的作用，请保持默认
    
7. 回到powershell，启动 Hoshino

    ```powershell
    py -3.8 run.py
    ```

    私聊机器人发送`在？`，若机器人有回复，恭喜您！您已经成功搭建起HoshinoBot了。之后您可以尝试在群内发送`help`查看一般功能的相关说明。

    注意，此时您的机器人功能还不完全，部分功能可能无法正常工作。若希望您的机器人可以发送图片，或使用其他功能，请参考本章**更进一步**的对应小节。





#### Linux 部署 (ssh等工具连接服务器)

1. 安装 python3.8 并设置pip：[参考](https://my.oschina.net/u/2401395/blog/3189222)
    
    > 若此处未安装设置成功，请务必解决，百度或谷歌搜索一般即可找到解决办法。 

2. 安装 screen (仅供参考，您也可以使用tmux等其他窗口工具)：

    ```bash
    # 根据系统选择命令安装
    yum install screen 
    apt-get install screen
    ```

    > 常用screen命令参数介绍
    ```bash
    screen -S yourname  # 新建一个名为yourname的screen
    screen -ls          # 列出当前所有的screen作业
    screen -r yourname  # 回到yourname这个screen
    screen -d yourname  # 将yourname这个screen作业离线
    screen -d -r yourname  # 结束当前作业并回到yourname的作业
    screen -wipe  # 检查目前所有的screen作业，并删除已经无法使用的screen作业
    ```
    >另外，在每个screen作业下，所有命令都以`ctrl+a(C-a)`开始，输入`C-a ?`显示所有键绑定信息

4. 在合适的文件夹克隆本仓库并安装依赖包
    ```bash
    cd /root/  # 或者自定义其他位置
    git clone https://github.com/Watanabe-Asa/HoshinoBot.git
    cd HoshinoBot
    python3.8 -m pip install -r requirements.txt
    ```

5. 编辑配置文件
    ```bash
    mv hoshino/config_example hoshino/config
    nano hoshino/config/__bot__.py
    ```
    > 配置文件内有相应注释，请根据您的实际配置填写，HoshinoBot仅支持反向ws通信
    >
    > 您也可以使用`vim`编辑器，若您从未使用过，推荐您使用 `nano` : )
    
6. 运行bot
    ```bash
    python3.8 run.py
    ```
    
    私聊机器人发送`在？`，若机器人有回复，恭喜您！您已经成功搭建起HoshinoBot了。之后您可以尝试在群内发送`help`查看一般功能的相关说明。
    
    注意，此时您的机器人功能还不完全，部分功能可能无法正常工作。若希望您的机器人可以发送图片，或使用其他功能，请参考本章**更进一步**的对应小节。



### 更进一步

现在，机器人已经可以使用一些基本功能了。但还无法使用`番剧订阅`、`推特转发`等功能。这是因为，这些功能需要相应的api key及一些静态资源。相应资源获取有难有易，您可以根据自己的需要去获取。

下面将会分别介绍资源与api key的获取方法：



#### 静态图片资源

> 发送图片的条件：  
> 1. 静态图片资源

您可能希望看到更为精致的图片版结果，若希望机器人能够发送图片，需要准备静态图片资源，其中包括：

- 表情包杂图
- setu库
- 其他(根据需要补充)

等资源。自行收集可能较为困难，所以我们准备了一个较为精简的资源包以及下载脚本，可以满足相关功能的日常使用。如果需要，请加入QQ群 **Hoshino的后花园** 367501912，下载群文件中的`res.zip`。

或者在合适的文件夹位置使用命令创建文件夹，并用相关工具上传所需图片至相应位置。
    ```bash
    cd /root/  # 或者自定义其他位置
    mkdir res
    cd res
    mkdir img
    ```



#### 蜜柑番剧 RSS Token

> 请先在`hoshino/config/__bot__.py`的`MODULES_ON`中取消`mikan`的注释  
> 本功能默认关闭，在群内发送 "启用 bangumi" 即可开启

番剧订阅数据来自[蜜柑计划 - Mikan Project](https://mikanani.me/)，您可以注册一个账号，添加订阅的番剧，之后点击Mikan首页的RSS订阅，复制类似于下面的url地址：

```
https://mikanani.me/RSS/MyBangumi?token=abcdfegABCFEFG%2b123%3d%3d
```

保留其中的`token`参数，在文件`hoshino/config/mikan.py`中填写您的token：

```python
MIKAN_TOKEN = "abcdfegABCFEFG+123=="
```

注意：`token`中可能含有url转义，您需要将`%2b`替换为`+`，将`%2f`替换为`/`，将`%3d`替换为`=`。



#### 推特转发

推特转发功能需要推特开发者账号，具体申请方法请自行[Google](http://google.com)。注：现在推特官方大概率拒绝来自中国大陆的新申请，自备海外手机号及大学邮箱可能会帮到您。

若您已有推特开发者账号，在文件`hoshino/config/twitter.py`中填写您的key：

```python
consumer_key = "your_consumer_key",
consumer_secret = "your_consumer_secret",
access_token_key = "your_access_token_key",
access_token_secret = "your_access_token_secret"
```



#### 其他功能

其他更多适配HoshinoBot的功能插件可以在[社区](https://github.com/pcrbot)找到([插件索引](https://github.com/pcrbot/HoshinoBot-plugins-index))或者直接在github中搜索并自行适配安装。

大多数的插件若无特殊说明，安装方法为在文件夹`hoshino/modules/`下上传或者使用命令`git clone`获取插件文件夹，随后使用命令`pip install XXX`(XXX为插件需求的依赖名)安装依赖，最后在`hoshino/config/__bot__.py`的`MODULES_ON`中添加插件名。当然具体的使用请详细阅读对应的Readme文档。
