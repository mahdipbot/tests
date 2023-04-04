# -- Imports :
import telebot
import requests
import languages as ln
import mysql.connector
lang = ln.language
import login
# --Bot :
admin = 5836106012
bot = telebot.TeleBot("5896569615:AAFq45Wo2r9hYfbYlvNHqT3GAAnP3OVHPjo")
# Database :
mydb = mysql.connector.connect(
    user='coderunner',
    password='Mahdi1386',
    host='coderunner.mysql.pythonanywhere-services.com',
    database='coderunner$users')
cursor = mydb.cursor()
# Start bot:
@bot.my_chat_member_handler(func=lambda chat: chat.new_chat_member.status == "member")
def say_hello(chat):
    try:
        cursor.execute("SELECT CHAT_ID from USERS")
        myresult = cursor.fetchall()
        for i in myresult:
            chat_id = int(i[0])
        if chat.chat.id != chat_id:
            sql = "INSERT INTO USERS (CHAT_ID, FIRST_NAME) VALUES (%s, %s)"
            val = (chat.chat.id, chat.chat.title)
            cursor.execute(sql, val)
            mydb.commit()
        else:
            pass
    except:
        sql = "INSERT INTO USERS (CHAT_ID, FIRST_NAME) VALUES (%s, %s)"
        val = (chat.chat.id, chat.chat.title)
        cursor.execute(sql, val)
        mydb.commit()
@bot.message_handler(chat_types=["group","supergroup"])
def start(message):
    if message.text.startswith(tuple(lang.keys())):
        for i in lang.keys():
            if message.text.startswith(i):
                number = lang[i]
                code = message.text.replace(i,"")
        url = 'https://rextester.com/rundotnet/Run'
        data = {
        'LanguageChoiceWrapper': f'{number}',
        'Program': f'{code}'}
        response = requests.post(url, data=data)
        try:
            text = response.json()["Errors"]
            if text != None:
                bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
            else:
                text = response.json()["Result"]
                text = "🔰 Output :\n\n"+f"`{text}`"+ "\n\n-> @programming2007"
                bot.reply_to(message, text, parse_mode='markdown')
        except:
            text = response.json()["Errors"]
            bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
@bot.edited_message_handler(chat_types=["group","supergroup"])
def edited(message):
    if message.text.startswith(tuple(lang.keys())):
        for i in lang.keys():
            if message.text.startswith(i):
                number = lang[i]
                code = message.text.replace(i,"")
        url = 'https://rextester.com/rundotnet/Run'
        data = {
        'LanguageChoiceWrapper': f'{number}',
        'Program': f'{code}'}
        response = requests.post(url, data=data)
        try:
            text = response.json()["Errors"]
            if text != None:
                bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
            else:
                text = response.json()["Result"]
                text = "🔰 Output :\n\n"+f"`{text}`"+ "\n\n-> @programming2007"
                bot.reply_to(message, text, parse_mode='markdown')
        except:
            text = response.json()["Errors"]
            bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
@bot.message_handler(chat_types=["private"])
def start2(message):
    lang = ln.language
    if message.text.startswith(tuple(lang.keys())):
        for i in lang.keys():
            if message.text.startswith(i):
                number = lang[i]
                code = message.text.replace(i,"")
        url = 'https://rextester.com/rundotnet/Run'
        data = {
        'LanguageChoiceWrapper': f'{number}',
        'Program': f'{code}'}
        response = requests.post(url, data=data)
        try:
            text = response.json()["Errors"]
            if text != None:
                bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
            else:
                text = response.json()["Result"]
                text = "🔰 Output :\n\n"+f"`{text}`"+ "\n\n-> @programming2007"
                bot.reply_to(message, text, parse_mode='markdown')
        except:
            text = response.json()["Errors"]
            bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
    elif message.text == "/start":
        try:
            cursor.execute("SELECT CHAT_ID from USERS")
            myresult = cursor.fetchall()
            for i in myresult:
                chat_id = int(i[0])
            if message.chat.id != chat_id:
                sql = "INSERT INTO USERS (CHAT_ID, FIRST_NAME) VALUES (%s, %s)"
                val = (message.chat.id, message.from_user.first_name)
                cursor.execute(sql, val)
                mydb.commit()
                bot.reply_to(message,f"""Hi *{message.from_user.first_name}* :)
Welcome to *𝐶𝑂𝐷𝐸 𝐶𝑂𝑀𝑃𝐼𝐿𝐸𝑅* bot
    • You can run your code's with me :
        How ?
   • Please send `help`

• writen by : @programming2007
        """,parse_mode="markdown")
            else:
                bot.reply_to(message,f"""Hi *{message.from_user.first_name}* :)
Welcome to *𝐶𝑂𝐷𝐸 𝐶𝑂𝑀𝑃𝐼𝐿𝐸𝑅* bot
    • You can run your code's with me :
        How ?
   • Please send `help`

• writen by : @programming2007
        """,parse_mode="markdown")
        except:
            sql = "INSERT INTO USERS (CHAT_ID, FIRST_NAME) VALUES (%s, %s)"
            val = (message.chat.id, message.from_user.first_name)
            cursor.execute(sql, val)
            mydb.commit()
            bot.reply_to(message,f"""Hi *{message.from_user.first_name}* :)
Welcome to *𝐶𝑂𝐷𝐸 𝐶𝑂𝑀𝑃𝐼𝐿𝐸𝑅* bot
    • You can run your code's with me :
        How ?
   • Please send `help`

• writen by : @programming2007
        """,parse_mode="markdown")
    elif message.text in ("Languages","languages"):
        lang = ln.language
        lange = []
        x = lang.keys()
        for i in x :
            lang = f"💢 {i}"
            lange.append(lang)
        s = "\n".join(lange)
        bot.reply_to(message, f"{s}\n\n-> @programming2007")
    elif message.text in ("help","Help"):
        bot.reply_to(message, """
Usage:
( language )
( your code )

...

Examples:
    `py
  print("Hello World")`
    `lua
  print "Hello World"`

type `languages` for list of supported languages.

-> @programming2007
        """,parse_mode="markdown")
    elif message.from_user.id == admin:
        if message.text.startswith("sendall "):
            text = message.text.replace("sendall ","")
            cursor.execute("SELECT CHAT_ID from USERS")
            myresult = cursor.fetchall()
            for i in myresult:
                chat_id = int(i[0])
                bot.send_message(chat_id, text)
    elif message.text.startswith(tuple(lang.keys())):
        for i in lang.keys():
            if message.text.startswith(i):
                number = lang[i]
                code = message.text.replace(i,"")
        url = 'https://rextester.com/rundotnet/Run'
        data = {
        'LanguageChoiceWrapper': f'{number}',
        'Program': f'{code}'}
        response = requests.post(url, data=data)
        try:
            text = response.json()["Errors"]
            if text != None:
                bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
            else:
                text = response.json()["Result"]
                text = "🔰 Output :\n\n"+f"`{text}`"+ "\n\n-> @programming2007"
                bot.reply_to(message, text, parse_mode='markdown')
        except:
            text = response.json()["Errors"]
            bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
@bot.edited_message_handler(chat_types=["private"])
def edited2(message):
    lang = ln.language
    if message.text.startswith(tuple(lang.keys())):
        for i in lang.keys():
            if message.text.startswith(i):
                number = lang[i]
                code = message.text.replace(i,"")
        url = 'https://rextester.com/rundotnet/Run'
        data = {
        'LanguageChoiceWrapper': f'{number}',
        'Program': f'{code}'}
        response = requests.post(url, data=data)
        try:
            text = response.json()["Errors"]
            if text != None:
                bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
            else:
                text = response.json()["Result"]
                text = "🔰 Output :\n\n"+f"`{text}`"+ "\n\n-> @programming2007"
                bot.reply_to(message, text, parse_mode='markdown')
        except:
            text = response.json()["Errors"]
            bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
    elif message.text == "/start":
        try:
            cursor.execute("SELECT CHAT_ID from USERS")
            myresult = cursor.fetchall()
            for i in myresult:
                chat_id = int(i[0])
            if message.chat.id != chat_id:
                sql = "INSERT INTO USERS (CHAT_ID, FIRST_NAME) VALUES (%s, %s)"
                val = (message.chat.id, message.from_user.first_name)
                cursor.execute(sql, val)
                mydb.commit()
                bot.reply_to(message,f"""Hi *{message.from_user.first_name}* :)
Welcome to *𝐶𝑂𝐷𝐸 𝐶𝑂𝑀𝑃𝐼𝐿𝐸𝑅* bot
    • You can run your code's with me :
        How ?
   • Please send `help`

• writen by : @programming2007
        """,parse_mode="markdown")
            else:
                bot.reply_to(message,f"""Hi *{message.from_user.first_name}* :)
Welcome to *𝐶𝑂𝐷𝐸 𝐶𝑂𝑀𝑃𝐼𝐿𝐸𝑅* bot
    • You can run your code's with me :
        How ?
   • Please send `help`

• writen by : @programming2007
        """,parse_mode="markdown")
        except:
            sql = "INSERT INTO USERS (CHAT_ID, FIRST_NAME) VALUES (%s, %s)"
            val = (message.chat.id, message.from_user.first_name)
            cursor.execute(sql, val)
            mydb.commit()
            bot.reply_to(message,f"""Hi *{message.from_user.first_name}* :)
Welcome to *𝐶𝑂𝐷𝐸 𝐶𝑂𝑀𝑃𝐼𝐿𝐸𝑅* bot
    • You can run your code's with me :
        How ?
   • Please send `help`

• writen by : @programming2007
        """,parse_mode="markdown")
    elif message.text in ("Languages","languages"):
        lang = ln.language
        lange = []
        x = lang.keys()
        for i in x :
            lang = f"💢 {i}"
            lange.append(lang)
        s = "\n".join(lange)
        bot.reply_to(message, f"{s}\n\n-> @programming2007")
    elif message.text in ("help","Help"):
        bot.reply_to(message, """
Usage:
( language )
( your code )

...

Examples:
    `py
  print("Hello World")`
    `lua
  print "Hello World"`

type `languages` for list of supported languages.

-> @programming2007
        """,parse_mode="markdown")
    elif message.from_user.id == admin:
        if message.text.startswith("sendall "):
            text = message.text.replace("sendall ","")
            cursor.execute("SELECT CHAT_ID from USERS")
            myresult = cursor.fetchall()
            for i in myresult:
                chat_id = int(i[0])
                bot.send_message(chat_id, text)
    elif message.text.startswith(tuple(lang.keys())):
        for i in lang.keys():
            if message.text.startswith(i):
                number = lang[i]
                code = message.text.replace(i,"")
        url = 'https://rextester.com/rundotnet/Run'
        data = {
        'LanguageChoiceWrapper': f'{number}',
        'Program': f'{code}'}
        response = requests.post(url, data=data)
        try:
            text = response.json()["Errors"]
            if text != None:
                bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
            else:
                text = response.json()["Result"]
                text = "🔰 Output :\n\n"+f"`{text}`"+ "\n\n-> @programming2007"
                bot.reply_to(message, text, parse_mode='markdown')
        except:
            text = response.json()["Errors"]
            bot.reply_to(message, f"‼️ Error\n<code>{text}</code>", parse_mode='html')
bot.infinity_polling()