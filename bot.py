import discord
from discord.ext import commands
import random
import os
import asyncio

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='new commands.'))
    print('This Bot is Ready!')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms')


@client.command(aliases = ['test' , '8ball'])
async def _8ball(ctx,*,question):
    responses = ["It is certainly yes",
                 "It is decided so",
                 "No no no",
                 "No",
                 "Definetly No!!"
    ]
    await ctx.send(f'Questions:  {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx , amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def unban(ctx , * , member):
    banned_users = await ctx.guild.bans()
    member_name,member_discriminator = member.split('#')

    for ban_entry in banned_users:
         user = ban_entry.user

    if (user.name , user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))


@client.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    fmt = '{0} joined Discord at {0.created_at} and has {1} roles and joined this server on {0.joined_at}'
    await ctx.send(fmt.format(member, len(member.roles)))









client.run('NjQ0NTkwOTQzODUyNDI5MzIz.XqRl8g.DoMLzYg1OewB8I_JuJHjk9noC80')
