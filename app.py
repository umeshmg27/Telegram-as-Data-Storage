from http.client import HTTPException
from fastapi import FastAPI,status,Response
from main import Bot_Init
import telegram
import os
global_inst = Bot_Init()
app = FastAPI()


@app.get("/me")
def get_me():
    return "Hello User"



@app.post("/BotInitialisation",status_code=status.HTTP_201_CREATED)
async def BotInitilisation(bot_token : str,username: str,response: Response):
    try:
        global_inst.bot = telegram.Bot(bot_token)
        global_inst.username = username
    except:
        raise HTTPException(status_code = status.HTTP_417_EXPECTATION_FAILED, detail="Please provide a valid Bot Token")
    try:

        await global_inst.chat_id_init()
        await global_inst.send_message("message")
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Please ping your bot to initialise conversation")

    return status.HTTP_200_OK


@app.get("/ChatAliveChecker")
async def BotInitilisation(message : str):
    try:    
        await global_inst.send_message(message)
    except:
        raise HTTPException(status_code = status.HTTP_503_SERVICE_UNAVAILABLE, detail= "Please reinitialise your Bot with the Server")


@app.post("/exportfolder")
async def BotInitilisation(f_path : str):
    res = []
    res_error = []
    filetranscount = 0

    # Iterate directory
    
    for file in os.listdir(f_path):
        try:
        # check if current path is a file
            if os.path.isfile(os.path.join(f_path, file)):
                if file.endswith(".pdf"):
                    filetranscount += 1
                    await global_inst.send_document(os.path.join(f_path, file))
                if file.endswith(".jpg" or ".jpeg" or ".png"):
                    await global_inst.send_image(os.path.join(f_path, file))
                    filetranscount += 1
                if file.endswith(".mp4"):
                    await global_inst.send_video(os.path.join(f_path, file))
                    filetranscount += 1
                if file.endswith(".mp3" ):
                    await global_inst.send_audio(os.path.join(f_path, file))
                    filetranscount += 1
        except Exception as Error:
            res_error.append(file)
            continue

    
    return {"filestransferred" : filetranscount, "failedFiles" : res_error}

    
    return res
    # try:
    #     await
    # except:

    

