from kutana import Plugin
import psutil
import time
import os


plugin = Plugin(name="Metrics", description="Send some information")


@plugin.on_text("metrics")
async def _(message, env):
    process = psutil.Process(os.getpid())

    taken_memory = int(process.memory_info().rss / 2**20)
    taken_time = time.time() - message.date

    await env.reply("mem: ~{}mib; tim: {}s".format(taken_memory, taken_time))
