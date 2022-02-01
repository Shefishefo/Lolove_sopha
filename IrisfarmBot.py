from .. import loader		
from asyncio import sleep

class IrisBotMod(loader.Module):
		strings = {"name": "IrisBot"}
	
	def __init__(self):
		self.farm = True
		self.virys = True
		
	async def farmcmd(self, message):
		while self.farm:
			await message.reply("Ферма\n\n<b>Следующая команда будет произведена через 4 часа.\n\nIrisBot by @Sofa_sex</b>")
			await sleep(14500)
			
	async def virysncmd(self, message):
		while self.virys:
			await message.reply("Заразить =\n\n<b>Следующая команда будет произведена через 1 час.\n\nIrisBot by  @Sofa_sex</b>")
			await sleep(3600)
			
	async def virysecmd(self, message):
		while self.virys:
			await message.reply("Заразить -\n\n<b>Следующая команда будет произведена через 1 час.\n\nIrisBot by  @Sofa_sex</b>")
			await sleep(3600)
			
	async def viryshcmd(self, message):
			while self.virys:
			await message.reply("Заразить +\n\n<b>Следующая команда будет произведена через 1 час.\n\nIrisBot by  @Sofa_sex</b>")
			await sleep(3600)
			
	async def watcher(self, message):
		me = (await message.client.get_me())
		if message.sender_id == me.id:
			if message.text.lower() == "ирисфарм стоп":
				self.farm = False
				await message.reply("<b>Ирисфарм остановлен.</b>")
			if message.text.lower() == "ирисвирус стоп":
				self.virys = False
				await message.reply("<b>Ирисвирус остановлен.</b>")
			

		
			
