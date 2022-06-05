from multiprocessing import get_context
import threading

import nonebot
from nonebot import logger

_nb_run = nonebot.run


class Reloader:
    event: threading.Event = None

    @classmethod
    def reload(cls):
        if cls.event is None:
            raise RuntimeError()
        cls.event.set()


def _run(ev: threading.Event, *args, **kwargs):
    Reloader.event = ev
    _nb_run(*args, **kwargs)


def run(*args, **kwargs):
    should_exit = False
    ctx = get_context("spawn")
    while not should_exit:
        event = ctx.Event()
        process = ctx.Process(
            target=_run,
            args=(
                event,
                *args,
            ),
            kwargs=kwargs,
        )
        process.start()
        while not should_exit:
            if event.wait(1):
                logger.info("Receive reboot event")
                process.terminate()
                process.join(5)
                if process.is_alive():
                    logger.warning("Cannot shutdown gracefully in 5 second, force kill process.")
                    process.kill()
                break
            elif process.is_alive():
                continue
            else:
                # Process stoped without setting event
                should_exit = True


nonebot.run = run
