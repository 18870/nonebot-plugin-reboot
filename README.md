# Nonebot-plugin-reboot 
用命令重启 bot 

[![asciicast](https://asciinema.org/a/z10hzQ7Pgx4s9TVwj0nAv2TsV.svg)](https://asciinema.org/a/z10hzQ7Pgx4s9TVwj0nAv2TsV)

## :warning:注意事项
**不支持** `nb-cli`，即 `nb run` 启动方式。
需要在 bot 目录下使用 `python bot.py` 启动。

重启时直接对子进程使用 `process.terminate()`，如果你的其他插件启动了子进程，请确保它们能在设定的等待时间内正确关闭子进程，否则子进程会变成孤立进程。  
:warning: Windows 下因系统 API 的限制进程会直接被杀死， **没有** 等待时间。

<hr>  

插件依赖于 `multiprocessing` `spawn` 生成子进程方式工作，支持由 `nb-cli` 生成的 bot.py，或任何显式加载了 `bot.py` 并在加载插件后调用 `nonebot.run` 的启动方式。  

不支持 `nb run` 启动，因为 `nb run` 使用 `importlib` 在函数内加载 `bot.py`，multiprocessing 生成子进程时不会运行 `bot.py`，即 nonebot 初始化和加载插件的过程，导致启动失败。  

得益于使用 `spawn` 方式启动，每次重启都相当于重新加载了所有代码。只有这个插件本身或者 `bot.py` 有更新时才需要彻底关闭 bot 重启。


## 安装
通过 nb-cli 安装:  
`nb plugin install nonebot-plugin-reboot`  
通过 pip 安装:  
`pip install nonebot-plugin-reboot`  


## 使用
**超级用户**向机器人**私聊**发送**命令** `重启`, `reboot` 或 `restart`  
> :warning: 注意命令的 `COMMAND_START`.  
> 例如 /重启 、 /reboot 、 /restart


## 配置项 
`reboot_load_command`: `bool` 
- 加载内置的 `onebot v11` 重启命令 
- 可以通过命令 `重启` `reboot` `restart` 触发重启 
- 默认值: `True` 

`reboot_grace_time_limit`: `int`
- 收到重启命令后等待进程退出的最长时间，超时会强制杀进程
- 在 Windows 下没有等待时间，会直接杀进程
- ~~真寻从ctrl+c到彻底退出居然要六秒~~
- 默认值: `20`

## `bot.py`
因为使用了 `spawn` 方式启动子进程，默认的 bot.py 会加载两次插件。  

推荐的写法是将 插件加载部分 和 nonebot启动部分 分开，以避免插件在主进程和子进程都加载一遍

~~真寻启动居然要20秒~~

```python
#
# 上面省略
#

if __name__ == "__mp_main__": # 仅在子进程运行的代码
    # Please DO NOT modify this file unless you know what you are doing!
    # As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
    # 加载插件
    nonebot.load_from_toml("pyproject.toml")
    nonebot.load_plugins("src/plugins")
    nonebot.load_plugin("nonebot_plugin_xxxxxx")
    # ...

if __name__ == "__main__": # 仅在主进程运行的代码
    # nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    # 运行 nonebot
    nonebot.load_plugin("nonebot_plugin_reboot") # 加载重启插件
    nonebot.run(app="__mp_main__:app")
```


## API
```python
require("nonebot_plugin_reboot")
from nonebot_plugin_reboot import Reloader
Reloader.reload(delay=5) # 可选参数 5秒后触发重启
```


## 依赖 
`nonebot2 >= 2.0.0beta.2`  

启用 `reboot_load_command` 时需要以下依赖  
`nonebot-adapter-onebot`