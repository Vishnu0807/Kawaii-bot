import random
import time
import discord
from discord.ext import commands
import aiohttp



bot = commands.Bot(command_prefix='-')
bot.remove_command('help')
players = {}


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='-help'),status='do_not_disturb')
    print('This Bot is Ready!')


@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "👑-welcome-👑":
            await channel.send(f"""hihi {member.mention},hope you enjoy in this server to fullest""")


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    hembed=discord.Embed(colour=discord.Colour.orange(),description='More commands will be added soon until then enjoy with the existing commands we have')

    hembed.set_author(name='help')
    hembed.add_field(name='funhelp',value='Returns a list of Fun commands',inline=False)
    hembed.add_field(name='modhelp', value='Returns a list of Moderation commands', inline=False)
    hembed.add_field(name='utihelp', value='Returns a list of Utility commands', inline=False)
    await ctx.send(author,embed=hembed)

@bot.command(pass_context=True)
async def funhelp(ctx):
    author=ctx.message.author
    fembed=discord.Embed(colour=discord.Colour.red(),description='We currently have only a few commands but more commands will be added soon')

    fembed.add_field(name='punch {mention} reason',value='Command to punch a person which is displayed in an Embed',inline=False)
    fembed.add_field(name='hug {mention}',value='Command to hug a person which is displayed in an Embed',inline=False)
    fembed.add_field(name='slap {mention} reason',value='Command to slap a person which is displayed in an Embed',inline=False)
    fembed.add_field(name='say arg',value='Command which repeats what you put in the arg and also deletes your command',inline=False)
    fembed.add_field(name='8ball question',value='Command which generates a random answers to your questions',inline=False)
    fembed.add_field(name='kill {mention}',value='Command to kill a person which is displayed in an Embed',inline=False)
    fembed.add_field(name='bully {mention}',value='Command to bully a person which is displayed in an Embed',inline=False)
    fembed.add_field(name='kiss {mention}',value='Command to kiss a person which is displayed in an Embed')
    await ctx.send(author,embed=fembed)


@bot.command(pass_context=True)
async def modhelp(ctx):
    author=ctx.message.author
    membed=discord.Embed(colour=discord.Colour.dark_blue(),description='We currently have only a few commands and we are working on it,new commands will be added soon until then you can use these...')
    membed.add_field(name='kick {mention} reason',value='Command used to kick someone')
    membed.add_field(name='ban {mention} reason',value='Command to ban someone')
    membed.add_field(name='unban {mention}',value='Command to unban someone')

    await ctx.send(author,embed=membed)

@bot.command(pass_context=True)
async def utihelp(ctx):
    author=ctx.message.author
    umbed=discord.Embed(colour=discord.Colour.dark_grey(),description='We are currently working on new commands and they will be added soon until then you can use these...')
    umbed.add_field(name='clear {amt}',value='This command clears the mentioned amount of messages')
    umbed.add_field(name='info {mention}',value='This command shows the info about a user')

    await ctx.send(author,embed=umbed)


@bot.command()
async def avatar_url(ctx , * ,member:discord.member):
    await ctx.send({avatar_url})




@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency*1000)}ms')

@bot.command(aliases = ['test' , '8ball'])
async def _8ball(ctx,*,question):
    responses = ["It is certainly yes",
                 "Yes yes yes",
                 "No no no",
                 "No",
                 "yes certainly",
                 "Definetly No!!"
    ]
    await ctx.send(f'Questions:  {question}\nAnswer: {random.choice(responses)}')


@bot.command()
async def clear(ctx , amount=3):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason = reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@bot.command()
async def unban(ctx , * , member):
    banned_users = await ctx.guild.bans()
    member_name,member_discriminator = member.split('#')

    for ban_entry in banned_users:
         user = ban_entry.user

    if (user.name , user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    fmend = discord.Embed(colour=discord.Colour.dark_magenta(),description='Info about {0}'.format(member))
    fmend.add_field(name='joined this Server on:',value='{0.joined_at}'.format(member))
    fmend.add_field(name='Joined Discord on:',value='{0.created_at}'.format(member))
    fmend.add_field(name='Avatar url:',value='{0.avatar_url}'.format(member))
    await ctx.send(ctx.author,embed = fmend)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')

@bot.command()
async def serverinfo(ctx):
    """Tells you some info about the member."""
    embeded = discord.Embed( description='Server Info',colour=discord.Colour.gold())


    await ctx.send(embed=embeded)

@bot.command()
async def spam(ctx,amt,*,argg):
    await ctx.channel.purge(limit=1)
    for amt in range(0,int(amt)):
        await ctx.send(str(argg))



@bot.command()
async def punch(ctx, members: commands.Greedy[discord.Member], *, reasoon='no reason'):
    punched = ", ".join(x.name for x in members)
    raimg=('https://cdn.discordapp.com/attachments/549629874189369344/717991100517711882/2Q.png',
           'https://media.discordapp.net/attachments/549629874189369344/717996658465570816/Z.png',
           'https://media.discordapp.net/attachments/549629874189369344/717997018395443200/images.png',
           'https://media.discordapp.net/attachments/629202117093228549/717997548509593672/images.png')
    emb=discord.Embed(title='{} just got slapped'.format(punched),description='for {}'.format(reasoon),color=0xEE8700)
    emb.set_image(url=random.choice(raimg))
    await ctx.send(ctx.author,embed=emb)

@bot.command()
async def hug(ctx, members: commands.Greedy[discord.Member]):
    hugged = ", ".join(x.name for x in members)
    ranimg=('https://media.discordapp.net/attachments/629202117093228549/717999255054450688/2Q.png',
            'https://media.discordapp.net/attachments/629202117093228549/717999428287332372/9k.png',
            'https://media.discordapp.net/attachments/629202117093228549/717999855988899870/images.png',
            'https://media.discordapp.net/attachments/629202117093228549/718000025740902470/images.png')
    embde=discord.Embed(title='{} just got hugged'.format(hugged),description='Awwww!',color=0xEE8700)
    embde.set_image(url=random.choice(ranimg))
    await ctx.send(embed=embde)

@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reasoon='no reason'):
    slapped = ", ".join(x.name for x in members)
    rasimg=('https://media.discordapp.net/attachments/549629874189369344/718006206983307286/9k.png',
            'https://media.discordapp.net/attachments/549629874189369344/718006206983307286/9k.png',
            'https://media.discordapp.net/attachments/549629874189369344/718006466581233714/Z.png',
            'https://cdn.discordapp.com/attachments/549629874189369344/718006958074101860/2Q.png')
    embdee=discord.Embed(title='{} just got slapped'.format(slapped),description='for {}'.format(reasoon),color=0xEE8700)
    embdee.set_image(url=random.choice(rasimg))
    await ctx.send(embed=embdee)

@bot.command()
async def say(ctx,*, arg ):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)



@bot.command()
async def kill(ctx, members: commands.Greedy[discord.Member]):
    killed = ", ".join(x.name for x in members)
    rasimgg=('http://68.media.tumblr.com/c9340ffe7bd88258ec374a9cdf571ec3/tumblr_okxuc75yRi1w0ii2ho1_400.gif')
    embdee=discord.Embed(title='{} just got killed'.format(killed),description='What? He just got killed? Oh no!!!',color=0xEE8700)
    embdee.set_image(url=random.choice(rasimgg))
    await ctx.send(embed=embdee)

@bot.command()
async def kiss(ctx, members: commands.Greedy[discord.Member], channel=None):
    kissed = ", ".join(x.name for x in members)
    rasimg1=('https://tenor.com/view/anime-kiss-love-sweet-gif-5095865'
            'https://tenor.com/view/love-sweet-anime-chunibyo-kiss-gif-12879850'
            'https://tenor.com/view/kiss-anime-love-gif-4958649'
            'https://tenor.com/view/anime-ano-natsu-de-matteru-gif-9670722',
             'https://tenor.com/view/koi-to-uso-anime-kiss-gif-13344412')
    embed1=discord.Embed(title='{} just got slapped'.format(kissed),description='Awwww! What a cute couple',color=0xEE8700)
    embed1.set_image(url=random.choice(rasimg1))
    await ctx.send(embed=embed1)

@bot.command()
async def bully(ctx, members: commands.Greedy[discord.Member]):
        bullied = ", ".join(x.name for x in members)
        ranimg1 = ('https://tenor.com/view/kid-luffy-one-piece-bully-gif-5707440'
                   'https://tenor.com/view/fruits-basket-scary-scary-people-bully-gloomy-gif-16058683'
                   'https://tenor.com/view/dna-mad-bully-fight-angry-gif-5600466')
        embed2 = discord.Embed(title='{} just got bullied'.format(bullied),description='Aahh! He is getting bullied someone help!',color=0xEE8700)
        embed2.set_image(url=random.choice(ranimg1))
        await ctx.send(embed=embed2)


@bot.command()
async def all_members(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            await ctx.send(member)

@bot.command()
async def fetch_guilds(ctx,*, limit=1000, before=None, after=None):
    guilds = await bot.fetch_guilds(limit=1000).flatten()
    await ctx.send(guilds)

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@bot.command()
async def roles(ctx, *, member: MemberRoles):
    roleembed = discord.Embed(colour=discord.Colour.gold(),title='Roles of this user')
    roleembed.add_field(name='Roles:',value='I see the following roles: ' + ', '.join(member))
    await ctx.send(embed=roleembed)
    
bot.run('NjQ0NTkwOTQzODUyNDI5MzIz.XuH51A.xlLu7CYNxwxiy0lWHY34x0FY0VI')
