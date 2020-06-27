from chatterbot import ChatBot #Imports chatbot.
from chatterbot.trainers import ListTrainer #Method to train the chatbot.

bot = ChatBot('BotChat')
trainer = ListTrainer(bot,storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.80,
            'default_response': 'default_value'
        }])

conversation = open('./Resources/Chat.txt','r').readlines()
trainer.train(conversation)

while True:
    userMessage = input('You:')
    if userMessage.lower().strip()!= 'bye':
        reply = bot.get_response(userMessage)
        if reply.confidence == 0:
            reply = 'I am sorry but I do not not understand what you mean?'
    print('ChatBot:',reply)
    if userMessage.lower().strip()=='bye':
        print('ChatBot:Bye')
        break