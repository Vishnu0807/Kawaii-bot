import discord
from discord.ext import commands
import random
import os
import asyncio

client = commands.Bot(command_prefix='-')

@client.command()
async def hypesquad(ctx , * ,member:discord.member):
    if hypesquad== True:
        await ctx.send("This member is in Discord hypesquad")
    else:
        await ctx.send("This member is not in Discord hypesquad")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='-help'))
    print('This Bot is Ready!')

@client.command()
async def connected_accounts(ctx , *, member: discord.Member):
      await ctx.send({connected_accounts})

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send(f"""hihi {member.mention},hope you enjoy in this server to fullest""")
@client.command()
async def say(ctx, arg,arg2,arg3,arg4,arg5,arg6):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg,arg2,arg3,arg4,arg5,arg6)
    
    
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms')


@client.command(aliases = ['test' , '8ball'])
async def _8ball(ctx,*,question):
    responses = ["It is certainly yes",
                 "Yes yes yes",
                 "No no no",
                 "No",
                 "yes certainly",
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









client.run('NjQ0NTkwOTQzODUyNDI5MzIz.XruJEw.OFb8UsHHJcGhuOfnk5ktnXJUfBI')
