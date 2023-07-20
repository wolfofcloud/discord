import discord
import random
import datetime
token
client = discord.Client(intents=discord.Intents.all())
guild = client.get_guild(661027381980561409)

async def create_channel(message, channel_name ,overwrites):
    category = message.guild.get_channel(687069139067600897)
    new_channel = await message.guild.create_text_channel(name=channel_name, overwrites=overwrites, category=category)
    return new_channel

@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('/create'):
        cot=message.content
        cotlist=cot.splitlines()
        cot=cotlist[0]
        cot=cot.replace('/create ','')
        guild1 = message.guild
        new_role = await guild1.create_role(name=cot)
        overwrites1 = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            message.guild.me: discord.PermissionOverwrite(read_messages=True)
            }
        new_channel = await create_channel(message, channel_name=cot, overwrites=overwrites1)
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = True
        await new_channel.set_permissions(new_role, overwrite=overwrite)
        member=message.author
        role=discord.utils.get(message.guild.roles, name=cot)
        await member.add_roles(role)
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)
    if message.content.startswith("/join"):
        cot=message.content
        cot=cot.replace('/join ','')
        member=message.author
        role=discord.utils.get(message.guild.roles, name=cot)
        await member.add_roles(role)
        text = '権限を付与しました'
        await message.channel.send(text)
    if message.content.startswith("/del "):
        cot=message.content
        cot=cot.replace('/del ','')
        role=discord.utils.get(message.guild.roles, name=cot)
        channel = discord.utils.get(client.get_all_channels(), name=cot)
        text = 'もうすぐ消えるよ'
        await message.channel.send(text)
        await role.delete()
        await channel.delete()
    if message.content.startswith("/r "):
        list=[]
        cot=message.content
        cot=cot.replace('/r ','')
        list1=cot.split("d")
        faces=int(list1[1])
        repeat=int(list1[0])
        if repeat<=50:
            for i in range(repeat):
                list.append(random.randint(1,faces))
            wa=str(sum(list))
            cot1="+".join(map(str,list))
            text=(cot+"=("+cot1+")="+wa)
            await message.channel.send(text)
        else:
            text="ふえぇ\nそんな負荷が高い処理落ちちゃうよぉ"
            await message.channel.send(text)
    if message.content.startswith("/date "):
        list=[]
        cot=message.content
        cot=cot.replace('/date ','')
        list=cot.split("/")
        year=int(list[0])
        mon=int(list[1])
        day=int(list[2])
        days=int(list[3])
        date=datetime.date(year,mon,day)
        #ここまでで開始日時を取得
        day_of_week = ["月","火","水","木","金","土","日"]
        num_weekday=date.weekday()
        oneday=datetime.timedelta(days=1)
        #開始曜日を取得
        with open("伝助用のデータだよ.txt", mode = "w",encoding='utf-8') as densuke:
            densuke.write(date.strftime("%m/%d")+"({})\n".format(day_of_week[num_weekday]))
            for i in range(days-1):
                date+=oneday
                num_weekday=(num_weekday+1)%7
                densuke.write(date.strftime("%m/%d")+"({})\n".format(day_of_week[num_weekday]))
        await message.channel.send(file=discord.File("/atom/伝助用のデータだよ.txt"))

@client.event
async def  on_reaction_add(reaction, user):
    print("on_reaction_add")
    message=reaction.message
    cot3=message.content
    if cot3.startswith("/create"):
        print("a")
        cotlist1=cot3.splitlines()
        cot3=cotlist1[0]
        cot3=cot3.replace('/create ','')
        print("i")
        role=discord.utils.get(message.guild.roles, name=cot3)
        print('fuyo')
        await user.add_roles(role)


client.run(token)
