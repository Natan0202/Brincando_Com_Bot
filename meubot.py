import discord
import emoji
from discord import message
from discord import guild

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} Olá, humano! Bem vindo!\n1º Regra: Alimente o gato (SEMPRE!)\n2º Regra: De carinho no gato (SEMPRE!)\nNo demais fique a vontade @{message.author.name}')
        elif message.content == '?nivel':
            await message.author.send(f'Nivel: 0')
        elif message.content == 'ping':
            await message.author.send('pong')
        elif message.content == 'oi':
            await message.channel.send(f'Como posso ser útil, @{message.author.name}?')
        elif message.content == 'afeto':
            await message.channel.send(emoji.emojize(f'Por favor, faça carinho em minha barriga... arrgghh :cat_with_tears_of_joy:',use_aliases=True))
    async def on_member_join(self,member):
        guid = member.guild
        if guid.system_channel is not None:
            mensagem = f'Bem vindo! {member.mention}. Acabou de entrar no servidor {guild.name}'
            await guild.system_channel.send(mensagem)
            
intentes = discord.Intents.default()
intentes.members = True

client = MyClient(intentes=intentes)
client.run('OTAxMzExNTMwMjc5MjY0MzI2.YXOBxg.qvl3vX9ObcCpB6kc077kOS7W3QI')