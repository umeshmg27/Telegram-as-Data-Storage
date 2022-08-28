import asyncio
import telegram
# from tele_chat_id import chat_id

class Bot_Init:
    BOT_Token = "5695104380:AAEYwBtwWL50nhIILGbexMJATGxaGcKw5wA"

    def __init__(self,Bot_Token,username) :
        self.bot = telegram.Bot(Bot_Token)
        self.username = username
        
        
    async def chat_id(self):
        chat_data = await self.bot.get_updates()                
        current_user_data = [chat_id['message']['chat']['id'] if (chat_id['message']['chat']['username'] == self.username) else "Error" for chat_id in chat_data ]
        self.chat_id=  current_user_data[-1]


    async def send_message(self,message):
        async with self.bot:
            await self.bot.send_message(chat_id=self.chat_id,text=message)

    async def send_document(self,file_path):
        async with self.bot:
            await self.bot.send_document(chat_id=self.chat_id,document=open(file_path,'rb'))

    async def send_audio(self,file_path):
        async with self.bot:
            await self.bot.send_audio(chat_id=self.chat_id,audio=open(file_path,'rb'))

    async def send_video(self,file_path):
        async with self.bot:
            await self.bot.send_video(chat_id=self.chat_id,video=open(file_path,'rb'))
    
    

    


    






async def main():
    BOT_Instance = Bot_Init("5695104380:AAEYwBtwWL50nhIILGbexMJATGxaGcKw5wA",'Charlie371')
    await BOT_Instance.chat_id()
    await BOT_Instance.send_message("ohh Yeaahh")
    await BOT_Instance.send_document("./test.csv")
    await BOT_Instance.send_audio("./Kesariya.mp3")
    await BOT_Instance.send_video("./Kesariya Status.mp4")
    



if __name__ == '__main__':
    asyncio.run(main())