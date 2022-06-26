from .config import plugin_config, Config
__plugin_adapters__ = []
__plugin_name__ = "nonebot_plugin_reboot [重启 bot]"
__plugin_des__ = "用命令重启机器人"
__plugin_usage__ = ""
__plugin_author__ = "18870 <a20110123@163.com>"

try:
    from nonebot.plugin import PluginMetadata
    __plugin_meta__ = PluginMetadata(
        name=__plugin_name__,
        description=__plugin_des__,
        usage=__plugin_usage__,
        config=Config,
        extra={
            "author": __plugin_author__,
            "adapters": __plugin_adapters__,
        }
    )
except ImportError:
    pass

from .reloader import Reloader

if plugin_config.reboot_load_command:
    from .command import reboot_matcher