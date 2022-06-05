# Nonebot-plugin-reboot 
用命令重启 bot 


## 注意事项
**不支持** `nb-cli`，即 `nb run` 启动方式。
需要在 bot 目录下使用 `python bot.py` 启动。

仅在 `linux` `python3.8` `fastapi` 驱动器下测试过。
理论上与平台无关，但是我没测试（


## 安装
通过 pip 安装:
`pip install nonebot-plugin-reboot`  
并加载插件


## 使用
**超级用户**向机器人**私聊**发送**命令** `重启`, `reboot` 或 `restart`  
注意命令 `COMMAND_START`.


## 配置项 
`reboot_load_command`: `bool` 
- 加载内置的 `onebot v11` 重启命令 
- 可以通过命令 `重启` `reboot` `restart` 触发重启 
- 默认值: `True` 


## 用程序触发重启
```python
from nonebot_plugin_reboot import Reloader
Reloader.reload()
```


## 依赖 
`nonebot2 >= 2.0.0beta.2` 