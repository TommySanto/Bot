import telepot
from pprint import pprint
import random
#import urllib

bot = telepot.Bot("545473898:AAF3zg5xM1l4WRBCrblMFOUajb0T1igUzx4")

porno = ['Non è ora di farsi le seghe maiale', 'Porco segaiolo', 'Gesoo ti vede e non ti perdona']
chiapi = ['Aleeeeeeeee', 'Dadoooo', 'Sono natural', 'Fammi fare la serie che divento piccolo']
ibiza = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbV7oBLp9nRLGD9NUMN0AnSixG2aLTSGlq3vIh4azu-bPyXILo', 'http://www.ibiza-voice.com/media/news/ibiza/2010/amnesia/troya/3.jpg']
pag = ['https://media-cdn.tripadvisor.com/media/photo-s/07/48/97/4f/noa-club-beach-bar.jpg',
       'http://jjddj.com/there/wp-content/uploads/2017/01/Noa-020.jpg',
       'http://www.nightlife-cityguide.com/wp-content/uploads/2015/05/vita-notturna-Pag-Noa-Beach-Club-Zrce-Beach-Novalja.jpg']
cocconato = ['https://media-cdn.tripadvisor.com/media/photo-s/02/c6/b8/f0/albergo-ristorante-cannon.jpg', 'http://www.gazzettadasti.it/wp-content/uploads/2017/05/Cocconato-panorama.jpg']

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if 'lesbica' in msg['text'].lower():
        bot.sendMessage(chat_id, 'a lesbica')
    if 'porno' in msg['text'].lower():
        bot.sendMessage(chat_id, random.choice(porno))
    if 'chiapi' in msg['text'].lower():
        bot.sendMessage(chat_id, random.choice(chiapi))
    if 'pag' in msg['text'].lower():
        bot.sendPhoto(chat_id, random.choice(pag))
    if 'ciao' in msg['text'].lower():
        bot.sendMessage(chat_id, 'Ciao splendida')
    if 'ibiza' in msg['text'].lower():
        bot.sendPhoto(chat_id, random.choice(ibiza))
    if 'cocconato' in msg['text'].lower():
        bot.sendPhoto(chat_id, random.choice(cocconato))
        
bot.message_loop(handle)

