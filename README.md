# Nonebot-plugin-reboot 
用命令重启 bot 


## :warning:注意事项
:warning:**不支持** `nb-cli`，即 `nb run` 启动方式。
需要在 bot 目录下使用 `python bot.py` 启动。

仅在 `linux` `python3.8` `fastapi` 驱动器下测试过。
理论上与平台无关，但是我没测试（

:warning:重启时直接对子进程使用 `process.terminate()`，如果你的其他插件启动了子进程，请确保它们能在 5 秒内正确关闭子进程，否则子进程会变成孤立进程。

<hr>  

插件依赖于 `multiprocessing` `spawn` 生成子进程方式工作，支持由 `nb-cli` 生成的 bot.py，或任何显式加载了 `bot.py` 并在加载插件后调用 `nonebot.run` 的启动方式。  

不支持 `nb run` 启动，因为 `nb run` 使用 `importlib` 在函数内加载 `bot.py`，multiprocessing 生成子进程时不会运行 `bot.py`，即 nonebot 初始化和加载插件的过程，导致启动失败。  

得益于使用 `spawn` 方式启动，每次重启都相当于重新加载了所有代码。只有这个插件本身或者 `bot.py` 有更新时才需要彻底关闭 bot 重启。


## 安装
通过 pip 安装:
`pip install nonebot-plugin-reboot`  
并加载插件


## 使用
**超级用户**向机器人**私聊**发送**命令** `重启`, `reboot` 或 `restart`  
> :warning: 注意命令的 `COMMAND_START`.
> 例如 /重启 、 /reboot 、 /restart


## 配置项 
`reboot_load_command`: `bool` 
- 加载内置的 `onebot v11` 重启命令 
- 可以通过命令 `重启` `reboot` `restart` 触发重启 
- 默认值: `True` 


## API
```python
from nonebot_plugin_reboot import Reloader
Reloader.reload() # 触发重启
```


## 依赖 
`nonebot2 >= 2.0.0beta.2` 