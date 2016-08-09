    # -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random

 
TOKEN = '269047766:AAFZf48dvh7ZUHZnpkNJ9dEe0JDxSrzNzH0' # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(func=lambda m: m.content_type == 'text' and "cine" in m.text)
def command_cinema(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Aqui tienes la cartelera!') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    bot.send_message( cid, 'http://www.ecartelera.com/cines/225,0,1.html')
    
@bot.message_handler(func=lambda m: m.content_type == 'text' and "adios" in m.text)
def command_adios(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'No huyas cobarde!') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    
@bot.message_handler(commands=['estado']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_estado(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'virtualizado') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.   

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text == "budget")
def command_aflu(m):
    cid = m.chat.id
    bot.send_message(cid, 'getbud')
    
import re
@bot.message_handler(func=lambda m: m.from_user.id in lista_id) #Con esto hago que solo responda a un usuario
def command_trolling(m):
    cid = m.chat.id
    text = re.sub('[aeouáéíóú]','i', m.text)
    bot.send_message(cid, text)
    
@bot.message_handler(commands=['shame'])
def command_shame(m):
    cid = m.chat.id
    for i in range(): # 10 se puede cambiar por el numero de mensajes
        bot.send_message(cid,'repetir', m.text[8:])
        
@bot.message_handler(func=lambda m: m.content_type == 'text' and "panes" in m.text)
def command_panes(m): 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    numero = random.randrange(10) 
    frases ={1:"Vámonos al cine",
    2:"Creo que estaría bien jugar a juegos de mesa",
    3:"Nos vamos de cenita?",
    4:"Hoy quiero ser un paladin a la taza, juguemos a rol",
    5:"Vamos a tomar cafe?",
    6:"Convirtamonos en entrenadores pokemon!!!",
    7:"Yo no puedo quedar, tengo que sacar de paseo al dragon",
    8:"A mi no me mires, solo soy un chica",
    9:"Que cocine el de arriba"
    }
    mensaje = frases[numero]
    bot.send_message( cid, mensaje)

@bot.message_handler(func=lambda m: m.content_type == 'text' and "Dios" in m.text)
def command_dios(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Oye @GCritico, creo que te invocan') # Con la función 'send_message()' del bot,

@bot.message_handler(commands=['humor'])
def command_humor(m): 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    numero = random.randrange(10) 
    frases ={1:'La mamá le dice a la niña ciega: "Si te vuelves a portar mal, te cambio los muebles de lugar."',
    2:"¿Qué hacen 2 epilépticos en una cabina de teléfono?. La fiesta de la espuma. ",
    3:"¿Qué diferencia hay entre el amor y el sida?. Pues que el sida es para toda la vida. ",
    4:"¿Qué hace un leproso tocando la guitarra?. Carne picada.",
    5:"Mamá, mamá, ¿me das una galleta?.""Niño, están encima del frigorífico.""Mamá, es que no tengo brazos..." "Si no hay brazos, no hay galletas. ",
    6:"¿Qué tiene dos patas y sangra mucho?. Medio perro.",
    7:"¿Como abren los botellines de cerveza los negros de Africa?. Con las costillas. ",
    8:"¿Por qué los niños africanos no ven ""Pokemon""?.Porque lo echan después de comer. ",
    9:"¿Cuál es el morbo de tirarse a una anoréxica?. Ver cómo le sale la chepa. "
    }
    mensaje = frases[numero]
    bot.send_message( cid, mensaje)
    
####################################################
lista_id = [31117172, 13215837]
###################################################

#Lo siguiente es para que el bot diga no entiendo XXXX del texto
#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def command_defer(m):
    # this is the standard reply to a normal message
#    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")
#m.text.replace('a','i').replace('e','i').replace('o','i').replace('u','i').replace('i','i')
#@bot.message_handler(func=lambda m: m.from_user.id == 14070833)
#@bot.message_handler(func=lambda m: m.from_user.id in tu_lista_de_ids)

#############################################
    
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.