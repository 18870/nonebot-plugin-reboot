__plugin_adapters__ = []
__plugin_name__ = "nonebot_plugin_reboot [重启 bot]"
__plugin_des__ = "用命令重启机器人"
__plugin_usage__ = ""
__plugin_author__ = "18870 <a20110123@163.com>"

from .reloader import Reloader
from .config import plugin_config

if plugin_config.reboot_load_command:
    from .command import reboot_matcher