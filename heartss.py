from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Magic of smile"}
	@loader.owner
	async def heartsscmd(self, message):
		for _ in range(20):
			for hearts in ['💙','💛', '❤️‍🔥', '🌸', '❄️', '🐾']:
				await message.edit(hearts)
				await sleep(0.3)

	async def policeecmd(self, message):
		for _ in range(12):
			for policee in ['💛💛💛💛⬜️⬜️⬜️💙💙💙💙\n💛💛💛💛⬜️⬜️⬜️💙💙💙💙\n💛💛💛💛⬜️⬜️⬜️💙💙💙💙','💙💙💙💙⬜️⬜️⬜️💛💛💛💛\n💙💙💙💙⬜️⬜️⬜️💛💛💛💛\n💙💙💙💙⬜️⬜️⬜️💛💛💛💛']:
				await message.edit(policee)
				await sleep(0.3)

	async def dick2cmd(self, message):
		await message.edit('\u2060      💦\n❤️❤️❤️\n❄️❄️❄️\n  ❄️❄️❄️\n    ❄️❄️❄️\n     ❄️❄️❄️\n       ❄️❄️❄️\n        ❄️❄️❄️\n         ❄️❄️❄️\n          ❄️❄️❄️\n          ❄️❄️❄️\n      ❄️❄️❄️❄️\n ❄️❄️❄️❄️❄️❄️\n ❄️❄️❄️  ❄️❄️❄️\n    ❄️❄️       ❄️❄️')
		await sleep(1)
		await message.edit('\u2060    💦\n      💦\n❤️❤️❤️\n❄️❄️❄️\n  ❄️❄️❄️\n    ❄️❄️❄️\n     ❄️❄️❄️\n       ❄️❄️❄️\n        ❄️❄️❄️\n         ❄️❄️❄️\n          ❄️❄️❄️\n          ❄️❄️❄️\n      ❄️❄️❄️❄️\n ❄️❄️❄️❄️❄️❄️\n ❄️❄️❄️  ❄️❄️❄️\n    ❄️❄️       ❄️❄️')
		await sleep(1)
		await message.edit('\u2060  💦\n    💦\n      💦\n❤️❤️❤️\n❄️❄️❄️\n  ❄️❄️❄️\n    ❄️❄️❄️\n     '
			'❄️❄️❄️\n       ❄️❄️❄️\n        ❄️❄️❄️\n         ❄️❄️❄️\n          ❄️❄️❄️\n          ❄️❄️❄️\n      ❄️❄️❄️❄️\n ❄️❄️❄️❄️❄️❄️\n ❄️❄️❄️  ❄️❄️❄️\n    ❄️❄️       ❄️❄️')
		await sleep(1)
		await message.edit('\u2060💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n❄️❄️❄️\n  ❄️❄️❄️\n    '
			'❄️❄️❄️\n     ❄️❄️❄️\n       ❄️❄️❄️\n        ❄️❄️❄️\n         ❄️❄️❄️\n          ❄️❄️❄️\n          ❄️❄️❄️\n      ❄️❄️❄️❄️\n ❄️❄️❄️❄️❄️❄️\n ❄️❄️❄️  ❄️❄️❄️\n    ❄️❄️       ❄️❄️')
		await sleep(1)
		await message.edit('\u2060💦💦\n💦\n💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n❄️❄️❄️\n  ❄️❄️❄️\n    '
			'❄️❄️❄️\n     ❄️❄️❄️\n       ❄️❄️❄️\n        ❄️❄️❄️\n         ❄️❄️❄️\n          ❄️❄️❄️\n          ❄️❄️❄️\n      ❄️❄️❄️❄\n ❄️❄️❄️❄️❄️❄️\n ❄️❄️❄️  ❄️❄️❄️\n    ❄️❄️       ❄️❄️')