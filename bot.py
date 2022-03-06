import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer

class Bot(Client):
  def start(self):
    self.username = '@' + me.username
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    
  async def stop(self, *args):
      await super().stop()
      logging.info("Bot stopped. Bye.")


app = Bot()
app.run()
