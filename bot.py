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

@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reasoon='no reason'):
    slapped = ", ".join(x.name for x in members)
    rasimg=('https://media.discordapp.net/attachments/549629874189369344/718006206983307286/9k.png',
            'https://media.discordapp.net/attachments/549629874189369344/718006206983307286/9k.png',
            'https://media.discordapp.net/attachments/549629874189369344/718006466581233714/Z.png',
            'https://cdn.discordapp.com/attachments/549629874189369344/718006958074101860/2Q.png')
    embdee=discord.Embed(title='{} just got slapped'.format(slapped),description='for {}'.format(reasoon),color=0xEE8700)
    embdee.set_image(url=random.choice(rasimg))
    await ctx.send(embed=embdee)        
        
        
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send(f"""hihi {member.mention},hope you enjoy in this server to fullest""")
@client.command()
async def say(ctx,*, arg ):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)

@client.command()
async def hug(ctx, members: commands.Greedy[discord.Member]):
    hugged = ", ".join(x.name for x in members)
    ranimg=('https://media.discordapp.net/attachments/629202117093228549/717999255054450688/2Q.png',
            'https://media.discordapp.net/attachments/629202117093228549/717999428287332372/9k.png',
            'https://media.discordapp.net/attachments/629202117093228549/717999855988899870/images.png',
            'https://media.discordapp.net/attachments/629202117093228549/718000025740902470/images.png')
    embde=discord.Embed(title='{} just got hugged'.format(hugged),description='Awwww!',color=0xEE8700)
    embde.set_image(url=random.choice(ranimg))
    await ctx.send(embed=embde)    
    
@client.command()
async def punch(ctx, members: commands.Greedy[discord.Member], *, reasoon='no reason'):
    punched = ", ".join(x.name for x in members)
    raimg=('https://cdn.discordapp.com/attachments/549629874189369344/717991100517711882/2Q.png',
           'https://media.discordapp.net/attachments/549629874189369344/717996658465570816/Z.png',
           'https://media.discordapp.net/attachments/549629874189369344/717997018395443200/images.png',
           'https://media.discordapp.net/attachments/629202117093228549/717997548509593672/images.png')
    emb=discord.Embed(title='{} just got slapped'.format(punched),description='for {}'.format(reasoon),color=0xEE8700)
    emb.set_image(url=random.choice(raimg))
    await ctx.send(embed=emb)
    
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
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    fmt = '{0} joined Discord at {0.created_at} and has {1} roles and joined this server on {0.joined_at}'
    await ctx.send(fmt.format(member, len(member.roles)))









client.run('NjQ0NTkwOTQzODUyNDI5MzIz.XruJEw.OFb8UsHHJcGhuOfnk5ktnXJUfBI')
