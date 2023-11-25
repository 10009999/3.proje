import discord
import random
import time
from bot_token import token
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
mn=['Biliyor muydun? Minecrafttaki herobrineın 1.16 sürümüne kadar oyunda olduğu veya hiç oyunda olmadığı söyleniyor.','Biliyor muydun? Eğer minecraftın java sürümünde yüksek bir yerden düşüyorsan, oyundan çıkıp, yeniden girersen, düştüğünde hasar almazsın. Ama dikkat et. bunu çarpmaya birkaç blok kaldığında yapmalısın.','Biliyor muydun? Minecrafttaki prizmarin blokları renk değiştirebilir! Ama çoooooooooooooook yavaş şekilde. ','Biliyor muydun? Minecrafttaki iskeletlerin yayı her iki elinde de olabilir. Ama yüksek ihtimalle sağ elindedir. sol elinde olma ihtimali yaklaşık %11 dir.','Biliyor muydun? Minecrafttaki evokerlar, mavi yünlü koyunları hep büyüyle kırmızıya boyarlar.','Biliyor muydun? Minecraftta, phontomların o berbat ve hepimizi rahatsız eden sesleri aslında bir çocuğun uyurken gece çıkardığı seslerin üzerine aşırı ses efekti eklenmiş hali!','Biliyor muydun? Minecraftta, Yapraklar, evet evet yapraklar, 6 bloğa kadar redstone sinyali iletebilir! Böylece, Minecraftta arkadaşlarına, yapraklarla süslenmiş bir ev gibi görünen, tuzaklar yapabilirsiniz. Keşke bende tuzak kurabilsem ama maalesef benim hiç robodostum yok. :( ','Biliyor muydun? Minecraftta, blaze çubuğu ve patlamış nakarat meyveleriyle çalışma masasında end çubuğu üretebilirsin!!!','Biliyor muydun? Minecraftta, cadılar sağlık iksiri içerken burunlarını kaldırır!','Biliyor muydun? Minecraftta, bir endermanin gözlerine yanlışlıkla baktıysanız, bakmaya devam edin. Birkaç dakika sonra enderman pes edip ışınlanacak ve enderman saldırısına uğramayacaksınız!','Biliyor muydun? Minecraftta, cadı öldürdüğünüzde düşük bir ihtimalle, çubuk çıkabilir. Bu bir filmde cadıların çubuktan oluştuğu düşünüldüğüne bir göndermedir.','Biliyor muydun? Minecraftta, bir tavşana "Katil tavşan" diye ad verirseniz, o tavşanın gözleri kırmızılaşıcak ve size saldırmaya başlayacaktır. Bu, bir filmde birilerinin bir tavşanı çok küçümsemesi ve bir süre sonra o tavşanın, şövalyeleri bile yiyebilmesi ve sonra da daha büyük şeyler yiyebilmesine (buna minecraftta değinilmemiş.) yapılan bir göndermedir.','Biliyor muydun? Minecraftta, müzik kutusu yaparken elmas kullanmamızın nedeni, Edisonun da sesle ilgili bir çalışmasında, müzik çalabilmesi için iğnenin ucunun elmastan yapmasına yapılan bir göndermedir.','Biliyor muydun? Minecraftta, endde, müzikler açıksa, müzik ilk önce normal minecraft müziği olur. Ama zamanla bu müzik bozulmaya ve korkunçlaşmaya başlar. Bunun, minecrafttaki endin uğradığı o korkunç değişime uygun olması düşünüldüğü ihtimali var!']
sr=['https://www.youtube.com/watch?v=iaS4RX-JSK0','https://www.youtube.com/watch?v=HeR6x4_kunY&list=OLAK5uy_nc8SP3djtU6V5bYtxvpgR2M7pVp-Y_K9U','https://www.youtube.com/watch?v=VW-77qHDHeA','https://www.youtube.com/watch?v=qHHF7wYI8fI','https://www.youtube.com/watch?v=7e3CdhH7H7o','https://www.youtube.com/watch?v=_W1E9g8m2ac','https://www.youtube.com/watch?v=LXuNaiOXZoI','https://www.youtube.com/watch?v=PtHsrH-baIY','https://www.youtube.com/watch?v=6UJ1l_vlQyg','https://www.youtube.com/watch?v=Hmqpr_TtoZo','https://www.youtube.com/watch?v=UtOA_Lc6luc','https://www.youtube.com/watch?v=9kQJmTkQ_Ts','https://www.youtube.com/watch?v=48SuFtm4YC0','https://www.youtube.com/watch?v=9ImWiUJLOXc','https://www.youtube.com/watch?v=5hl-J5G84GQ']
zzz='Chatbot açık.'
@client.event
async def on_ready():
    print(f'Aktifleştirme ve veri aktarma başarılı! Aktifleştirilen ve veri aktarılan yazılımın ismi: {client.user}')
@client.event
async def on_message(message):
    global zzz
    if message.author == client.user:
        return
    if message.content.startswith('merhaba') and zzz=='Chatbot açık.':
        await message.channel.send("Merhaba!")
    elif message.content.startswith('Merhaba') and zzz=='Chatbot açık.':
        await message.channel.send("Merhaba!")
    elif message.content.startswith('görüşürüz') and zzz=='Chatbot açık.':
        await message.channel.send('Görüşürüz!!!')
    elif message.content.startswith('görüşürüz!') and zzz=='Chatbot açık.':
        await message.channel.send('Görüşürüz!!!')
    elif message.content.startswith('Görüşürüz!') and zzz=='Chatbot açık.':
        await message.channel.send('Görüşürüz!!!')
    elif message.content.startswith('görüşürüz!!!') and zzz=='Chatbot açık.':
        await message.channel.send('Görüşürüz!!!')
    elif message.content.startswith('Görüşürüz!!!') and zzz=='Chatbot açık.':
        await message.channel.send('Görüşürüz!!!')
    elif message.content.startswith('merhaba!') and zzz=='Chatbot açık.':
        await message.channel.send('Merhaba!')
    elif message.content.startswith('Merhaba!') and zzz=='Chatbot açık.':
        await message.channel.send('Merhaba!')
    elif message.content.startswith('merhaba!!!') and zzz=='Chatbot açık.':
        await message.channel.send("Merhaba!")
    elif message.content.startswith('Merhaba!!!') and zzz=='Chatbot açık.':
        await message.channel.send("Merhaba!")
    elif message.content.startswith('İyi misin chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('iyi misin chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('iyi misin chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('İyi misin Chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('iyi misin Chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('İyi misin chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('İyi misin Chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('iyi misin Chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Sohbet etmek beni nasıl mutsuz etsin ki? Tabii ki iyiyim. Benden değil senden konuşalım. Nasılsın?")
    elif message.content.startswith('nasılsın?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('Nasılsın?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('nasılsın') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('Nasılsın') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('nasılsın chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('nasılsın Chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('Nasılsın chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('Nasılsın Chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('nasılsın chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('nasılsın Chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('Nasılsın Chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('Nasılsın chatbot?') and zzz=='Chatbot açık.':
        await message.channel.send("Seninle sohbet ettiğim için çoooook iyi hissediyorum. Sen nasılsın?")
    elif message.content.startswith('İyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende iyiyim. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('iyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende iyiyim. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('İyiyim!') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende iyiyim. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('iyiyim!') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende iyiyim. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok İyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok iyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok İyiyim!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok iyiyim!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok İyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok İyiyim!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok iyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok iyiyim!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok iyiysen, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Mutluyum') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('mutluyum') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Mutluyum!') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('mutluyum!') and zzz=='Chatbot açık.':
        await message.channel.send("Oh oh ne güzel! Bende mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok Mutluyum') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok mutluyum') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluys and zzz=='Chatbot açık.'an, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok Mutluyum!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben de sohbet ettiği and zzz=='Chatbot açık.'m arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('Çok mutluyum!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok Mutluyum') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben  and zzz=='Chatbot açık.'de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok Mutluyum!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok mutluyum') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok mutluyum!') and zzz=='Chatbot açık.':
        await message.channel.send("Mükemmel diyorsun yani, sen çok mutluysan, ben de sohbet ettiğim arkadaşım (Yani sen) mutlu olduğu için mutluyum. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('bende iyiyim') and zzz=='Chatbot açık.':
        await message.channel.send("Bunu duyduğuma sevindim. Peki şimdi bilgi zamanına hazır mısın? (hazırım/hazır değilim)")
    elif message.content.startswith('çok kötü') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('çok kötüyüm') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('kötüyüm') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('kötü') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('çok kötü hissediyorum') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('kötü hissediyorum') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('çok kötü chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('çok kötüyüm chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('kötüyüm chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('kötü chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('çok kötü hissediyorum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler çok ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('kötü hissediyorum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... Sanırım bir şeyler ters gitmiş. O zaman biraz kafayı dağıtalım. MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('şarkı önerisi verir misin') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('şarkı önerisi verir misin chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('müzik önerisi verir misin') and zzz=='Chatbot açık.':
        await message.channel.send("Tabii ki! İşte şimdi, MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('müzik önerisi verir misin chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Tabii ki! İşte şimdi, MÜZİK ZAMANI!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('şarkı zamanı') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('şarkı zamanı chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('müzik zamanı') and zzz=='Chatbot açık.':
        await message.channel.send("MÜZİK ZAMANI!!! YAŞASIN!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('müzik zamanı chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("MÜZİK ZAMANI!!! YAŞASIN!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana bir müzik açar mısın') and zzz=='Chatbot açık.':
        await message.channel.send("HEMEN AÇILIYORRRRRR!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana bir müzik açar mısın chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("HEMEN AÇILIYORRRRRR!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana bir şarkı açar mısın') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana bir şarkı açar mısın chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana başka bir müzik açar mısın') and zzz=='Chatbot açık.':
        await message.channel.send("HEMEN BAŞKA BİR MÜZİK AÇILIYORRRRRR!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana başka bir müzik açar mısın chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("HEMEN BAŞKA BİR MÜZİK AÇILIYORRRRRR!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana başka bir şarkı açar mısın') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('bana başka bir şarkı açar mısın chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Hmmm... benim şarkım yok. Benim müziklerim var! Ama onlar da çok güzel! Hemen bir tanesini gönderyorum!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send('Bir dene bakalım. umarım sen de seversin. Sen müziğin tadını çıkar, ama bana sevip sevmediğini söylemene gerek yok. Çünkü o kadar güzel ki bu müzikler, eminim bayılacaksın!')
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('hazırım') and zzz=='Chatbot açık.':
        await message.channel.send("BİLGİ ZAMANIIIII!!! Ne hakkında bilgi istiyorsun? İŞTE BİLGİ ALABİLECEĞİN KONULAR: MİNECRAFT HAKKINDA BİLGİ ALMAK İSTİYORSAN 1, CHATBOT HAKKINDA BİLGİ ALMAK İÇİN 2 YAZ. Bilgi zamanından çıkmak istiyorsan 3 yaz. (GELİŞTİRİLİYOR... YAKINDA DAHA FAZLA KONU HAKKINDA DA BİLGİ VEREBİLECEK.)")
    elif message.content.startswith('hazır değilim') and zzz=='Chatbot açık.':
        await message.channel.send('Sanırım birşeyler ters gitti. Tamam, o zaman biraz mola verip ondan sonra hazırım dersen bilgi zamanına devam edebiliriz.')
    elif message.content.startswith('1') and zzz=='Chatbot açık.':
        xxx=random.choice(mn)
        await message.channel.send(xxx)
        await message.channel.send('Yeniden bir bilgi istiyor musun? istiyorsan 1 yaz. Bilgi zamanı ekranına dönmek ve oradan da çıkabilmek istiyorsan 0 yaz.')
    elif message.content.startswith('0') and zzz=='Chatbot açık.':
        await message.channel.send("BİLGİ ZAMANIIIII!!! Ne hakkında bilgi istiyorsun? İŞTE BİLGİ ALABİLECEĞİN KONULAR: MİNECRAFT HAKKINDA BİLGİ ALMAK İSTİYORSAN 1, CHATBOT HAKKINDA BİLGİ ALMAK İÇİN 2 YAZ. Bilgi zamanından çıkmak istiyorsan 3 yaz. (GELİŞTİRİLİYOR... YAKINDA DAHA FAZLA KONU HAKKINDA DA BİLGİ VEREBİLECEK.)")
    elif message.content.startswith('3') and zzz=='Chatbot açık.':
        await message.channel.send('bilgi zamanından çıkıldı.')
        await message.channel.send('Yorulmuş olmalısınız! Biraz mola veriliyor. Yeniden açmak için ise "sohbeti yeniden başlat chatbot" diye yazmalısınız. Yazıp gönderdiğinizde, yeniden açılacaktır. ve açıldığına dair bir mesaj da atacaktır.')
        zzz='Chatbot kapalı.'
    elif message.content.startswith('4') and zzz=='Chatbot açık.':
        await message.channel.send("BAŞKA BİR MÜZİK HEMEN GELİYORRRRR!!!")
        srsr=random.choice(sr)
        await message.channel.send(srsr)
        await message.channel.send("Bir tane daha müzik istiyorsan, 4 yazman yeterli!")
    elif message.content.startswith('2') and zzz=='Chatbot açık.':
        await message.channel.send("Chatbot hakkında bilgi almayı seçtiniz. İşte Chatbotla ilgili bilgiler!")
        await message.channel.send("1. Chatbotu kapatmak için 'sohbeti sil ve kapat chatbot' yazmalısınız.(Chatbot, sohbeti silip kapansa bile, aslında açıktır. Sadece ikinci bir açma komutuna kadar hiç bir şeye cevap vermez. Sadece bu modun ismi öyle.)")
        await message.channel.send("2. Chatbot kapalıyken onu açmak için, 'sohbet başlat chatbot' yazmalısınız.")
        await message.channel.send('Bilgi zamanı ekranına dönmek ve oradan da çıkabilmek istiyorsan 0 yaz.')
    elif message.content.startswith('sohbeti sil ve kapat chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("!!!BU İŞLEMİ ONAYLIYOR MUSUNUZ? BUNUN OLMASI HALİNDE SOHBET EN BAŞA DÖNECEKTİR.(AMA DİSCORDDAKİ MESAJLAR SİLİNMEYECEKTİR.) VE CHATBOT İKİNCİ BİR AÇMA KOMUTUNA KADAR ÇEVRİMİÇİ OLSA BİLE ÇEVRİMDIŞI GİBİ DAVRANACAKTIR. İŞLEMİ ONAYLAMAK İÇİN, 'onaylıyorum' İŞLEMİ İPTAL EDMEK İÇİN İSE, 'iptalet' YAZMALISINIZ.(YENİDEN AÇMAK İÇİN İSE, 'sohbet başlat chatbot' yazmalısınız.')")
    elif message.content.startswith('sohbet başlat chatbot'):
        await message.channel.send("Sohbet şu andan itibaren başlatıldı.")
        zzz='Chatbot açık.'
    elif message.content.startswith('sohbeti yeniden başlat chatbot'):
        await message.channel.send("Sohbet şu andan itibaren yeniden başlatıldı.")
        zzz='Chatbot açık.'
    elif message.content.startswith('onaylıyorum') and zzz=='Chatbot açık.':
        await message.channel.send("Tamamdır. Chatbot kapatıldı!")
        zzz='Chatbot kapalı.'
    elif message.content.startswith('iptalet') and zzz=='Chatbot açık.':
        await message.channel.send("Tamamdır. İşlem iptal edildi!")
    elif message.content.startswith('harikasın chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Ne demek efendim, vazifemiz!")
    elif message.content.startswith('mükemmelsin chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Ne demek efendim, vazifemiz!")
    elif message.content.startswith('olağanüstüsün chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("E o zaman nasıl varoldum??? Şaka şaka!!! Teşekkür ederim güzel sözleriniz için!")
    elif message.content.startswith('vay be bu müzik gerçekten de bir harikaymış dostum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik gerçekten de bir harikaymış dostum') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik gerçekten de harikaymış dostum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik gerçekten de harikaymış dostum') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik bir harikaymış dostum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik bir harikaymış dostum') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik harikaymış dostum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik harikaymış dostum') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('vay be bu müzik gerçekten de bir harikaymış dostum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik gerçekten de bir harikaymış dostum chatbot') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik gerçekten de bir harikaymış dostum') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik gerçekten de bir harikaymış') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik bir harikaymış') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik harikaymış') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müzik harikaymış') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müzik çok güzel') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik çok güzel') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müzik çok güzelmiş') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik çok güzelmiş') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müzik güzelmiş') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('güzelmiş') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müzik güzelmiş') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müziği beğendim') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müziği beğendim') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müziğe bayıldım') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bu müziğe gerçekten bayıldım') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müziğe gerçekten bayıldım') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('müziğe gerçekten de bayıldım') and zzz=='Chatbot açık.':
        await message.channel.send("Beğeniceğini söylemiştim!")
    elif message.content.startswith('bunu çok beğenmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bu müziği çok sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bu müziği sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bu müziği hiç sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bunu sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bunu hiç sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bunu çok sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('bu müziği çok sevmedim') and zzz=='Chatbot açık.':
        await message.channel.send("Ama bunun güzel olduğunu sanıyordum. Neyse, Bir daha ki sefere beğenirsin umarım.")
    elif message.content.startswith('banabirmüziklütfenmüzibot:)(:#') and zzz=='Chatbot açık.':
        await message.channel.send("Bir sorun var! Müzibot'un çalışması için yeniden açılması gerekiyor! ÖNEMLİ NOT: BİRDEN FAZLA BOT AÇIKSA, SADECE EN SON AÇILAN BOT AKTİF MESAJ ATABİLME ÖZELLİĞİNE SAHİPTİR!")
    elif message.content.startswith('banabaşkabirmüziklütfenmüzibot:)(:#') and zzz=='Chatbot açık.':
        await message.channel.send("Bir sorun var! Müzibot'un çalışması için yeniden açılması gerekiyor! ÖNEMLİ NOT: BİRDEN FAZLA BOT AÇIKSA, SADECE EN SON AÇILAN BOT AKTİF MESAJ ATABİLME ÖZELLİĞİNE SAHİPTİR!")
    elif message.content.startswith('bbmlm') and zzz=='Chatbot açık.':
        await message.channel.send("Bir sorun var! Müzibot'un çalışması için yeniden açılması gerekiyor! ÖNEMLİ NOT: BİRDEN FAZLA BOT AÇIKSA, SADECE EN SON AÇILAN BOT AKTİF MESAJ ATABİLME ÖZELLİĞİNE SAHİPTİR!")
    elif message.content.startswith('bbbmlm') and zzz=='Chatbot açık.':
        await message.channel.send("Bir sorun var! Müzibot'un çalışması için yeniden açılması gerekiyor! ÖNEMLİ NOT: BİRDEN FAZLA BOT AÇIKSA, SADECE EN SON AÇILAN BOT AKTİF MESAJ ATABİLME ÖZELLİĞİNE SAHİPTİR!")
    else:
        if zzz=='Chatbot açık.':
            await message.channel.send('Maalesef, bunu cevaplayamıyorum! Lütfen bana sorduğunuz soruları benim cevaplayabilmem için ve yazım kolaylığı için, büyük harf kullanmadan ve noktalama işaretleri kullanmadan yazın.(Ben noktalama işaretlerini ve büyük harfleri kullanabiliyorum.) Eğer sizin böyle bir hatanız yoksa, sorunuz chatbota kaydedilmemiş demektir. Başka şekilde yazmayı deneyin. Örneğin:"çok kötü hissediyorum" yazmak yerine, "çok kötü" yazabilirsiniz. Hâla aynı hatayı veriyorsa, başka sorular sormayı deneyin.')
client.run(token)
