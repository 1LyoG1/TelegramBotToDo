import telebot
import requests

Api_Key = '5315323489:AAFFQToswWdBHwQcFGjqcszoSucy4IQhPmU'
bot = telebot.TeleBot(Api_Key)

print("Iniciado!")

def ReturnToDoList():

    try:
        responseToDoAPI = requests.get("https://telegrambotapitodo.herokuapp.com/todolist")
        responseToDoListAPI = responseToDoAPI.json()['rows']
        ToDoList = ''
        for ToDo in responseToDoListAPI:
            ToDoList += ToDo['name'] + "\n"
        return ToDoList
    except:
        return 'Ocorreu um erro interno! Não foi possivel localizar sua lista, tente novamente mais tarde!'



@bot.message_handler(commands=['Create'])
def create(message):
    bot.send_message(message.chat.id,ReturnToDoList())

@bot.message_handler(commands=['Delete'])
def delete(message):
    bot.send_message(message.chat.id, "Qual item da lista deseja deletar?")


def VerifyMessage(message):
    return True

@bot.message_handler(func=VerifyMessage)
def DefaultResponse(message):
    TextResponse = """
    Olá, bem vindo a sua lista de tarefas descomplicada!
    Escolha uma opção (Clique no item)
    /Create Criar item na lista.
    /Delete Deletar item na lista"""
    bot.reply_to(message,TextResponse)


bot.polling()