import discord
import random

bot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Wartungsarbeiten!'))
    print('Booting complete')

@bot.event
async def on_message(message):
    global sender
    global check

    memes = ['https://cdn.discordapp.com/attachments/800792706833973289/838155560519336021/unknown.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838396797461463050/Frederik2_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838396800490536960/Frederik9_meme.png',
            #'https://cdn.discordapp.com/attachments/808418244628840499/838396800523829309/Frederik8_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838396804164485170/Frederik12_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838398668285280266/Frederik7_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838398670662533160/Frederik13_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838398671766814740/Frederik17_meme.png',
            #'https://cdn.discordapp.com/attachments/808418244628840499/838362650697662474/unknown.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838398917501648916/Frederik10_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838399397205246022/Frederik3_meme.png',
            'https://cdn.discordapp.com/attachments/808418244628840499/838400124023209994/Frederik15_meme.png', 
            'https://cdn.discordapp.com/attachments/808418244628840499/838400508045033512/Frederik18_meme.png']

    explosion = ['https://cdn.discordapp.com/attachments/833098898930139229/838392942107951174/unknown.png',
                 'https://cdn.discordapp.com/attachments/833098898930139229/838393529772408892/unknown.png',
                 'https://cdn.discordapp.com/attachments/833098898930139229/838393572482482216/unknown.png',
                 'https://cdn.discordapp.com/attachments/833098898930139229/838393690305069076/unknown.png',
                 'https://cdn.discordapp.com/attachments/833098898930139229/838484887329570836/unknown.png',
                 'https://cdn.discordapp.com/attachments/833098898930139229/838485814828335154/unknown.png']
    
    if message.content.lower() == '-meme':
        await message.channel.send(random.choice(memes))

    if message.content.startswith('-help'):
        sender = message.author

        embed = discord.Embed(title='Prof. Kieslich Bot Hilfe',
                              description='Der Prefix vom Bot ist "-"\n'
                                          'Hilfe angefordert von {}'.format(message.author.mention),
                              color=0x00f8ff)
        embed.add_field(name='-help', value='Zeigt diese Hilfe an.', inline=False)
        embed.add_field(name='-meme', value='Sendet ein zufälliges Meme von Frederik.', inline=False)
        embed.add_field(name='-special', value='Mit diesem Befehl könnt ihr Auswählen, welches Abonnenten Special euch geschickt werden soll.', inline=False)
        embed.add_field(name='-explosion', value='Sendet ein zufälliges Bild von einer Explosion.', inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/833098898930139229/838490284241191002/Logoentwurf2neuer.jpg')
        embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/808418244628840499/839113433727107102/Profilbild.png' ,text='Programmiert von Sören#2416')
        await message.channel.send(embed=embed)

    if message.content.lower() == '-special':
        
        sender = message.author
        check = True

        await message.channel.send('Welches Abonnenten Special möchtest du haben?' + '\n' + 
                                   'Antworte mit:' + '\n' +
                                   '**100** für das 100 Abonnenten Special' + '\n' +
                                   '**300** für das 300 Abonnenten Special' + '\n' +
                                   '**500** für das 500 Abonnenten Special' + '\n')

    if message.content == '100' and message.author == sender and check == True or message.content == '300' and message.author == sender and check == True or message.content == '500' and message.author == sender and check == True:

        c = message.content.lower()

        if c == '100':
            await message.channel.send('Hier das ' + c + ' Abonnenten Special:')
            await message.channel.send('https://www.youtube.com/watch?v=3duboi876G8')
            check = False

        if c == '300':
            await message.channel.send('Hier das ' + c + ' Abonnenten Special:')
            await message.channel.send('https://www.youtube.com/watch?v=CYvtklljqqk')
            check = False

        if c == '500':
            await message.channel.send('Hier das ' + c + ' Abonnenten Special:')
            await message.channel.send('https://youtu.be/rINQsLJSxFo')
            check = False

    if message.content.lower() == '-explosion':
        await message.channel.send(random.choice(explosion))

    if message.content.lower().startswith('-socials'):
        
        b = ['yt', 'i', 'a', 'youtube', 'y', 'instagram', 'insta', 'all']

        txt = message.content
        input = txt.split(' ')

        if len(input) == 2:
            
            tmp = "".join(input[1])
            
            for word in b:
                if word in message.content.lower():

                    if tmp.lower() == 'yt' or tmp.lower() == 'youtube' or tmp.lower() == 'y':
                        await message.channel.send('https://www.youtube.com/channel/UC5E-DDOyl_CLi5BCbFHv2vQ')
                        break

                    elif tmp.lower() == 'i' or tmp.lower() == 'instagram' or tmp.lower() == 'insta':
                        
                        embed = discord.Embed(color=0xbc2a8d)

                        embed.add_field(name='https://www.instagram.com/prof.kieslichs_chem_lab/?hl=de', value='Mein Instagram')

                        await message.channel.send(embed=embed)
                        break

                    elif tmp.lower() == 'a' or tmp.lower() == 'all':
                        await message.channel.send('**Hier mein YouTube:**')
                        await message.channel.send('https://www.youtube.com/channel/UC5E-DDOyl_CLi5BCbFHv2vQ')

                        embed = discord.Embed(color=0xbc2a8d)

                        embed.add_field(name='https://www.instagram.com/prof.kieslichs_chem_lab/?hl=de', value='Mein Instagram')

                        await message.channel.send('**Hier mein Instagram:**')
                        await message.channel.send(embed=embed)
                        break
                else:
                    await message.channel.send('**Error!** Kein gültiger Parameter angegeben! Wenn du nicht weiter weißt schau bei **-help** oder wende dich an einen **Admin** oder **Moderator**.')

        else:
            await message.channel.send('**Error!** Kein Parameter angegeben! Wenn du nicht weiter weißt schau bei **-help** oder wende dich an einen **Admin** oder **Moderator**.')    


bot.run('ODM4MzQyMTY1MzYwNjcyNzY4.YI5s-w.51EZrDlpcRpehMqkV2SURK8Ud5I')