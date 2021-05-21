import discord
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix = 'J')
status = cycle(['Im John...', 'My Prefix is J', 'Under Development...'])

@client.event
async def on_ready():
    change_status.start()
    print('Hey Boss!, Iam Online and Ready deal with the Servers...')

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    print(f'{member} has joined...')

@client.event
async def on_member_remove(member):
    print(f'{member} has left...')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used...')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Hi':
        await client.process_commands('Hi...!')

client.run