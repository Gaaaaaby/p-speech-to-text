from cgitb import enable
from email.mime import audio
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from google.cloud import speech


client = speech.SpeechClient.from_service_account_file('key.json')

app = FastAPI()

# Setting middlewares
# reference: https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = speech.SpeechClient.from_service_account_file('key.json') 

@app.get('/')
def root():
    return {'Message': "Site is running, visit to -> localhost:8000/docs"}



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_name = file 
    contents = await file_name.read()
    audio_file = speech.RecognitionAudio(content=contents)

    config = speech.RecognitionConfig(sample_rate_hertz=44100, enable_automatic_punctuation=True,
    language_code='en-US',audio_channel_count = 2)
    response = client.recognize(config=config, audio=audio_file)

    #for result in response.results:
    #    print("Transcript: {}".format(result.alternatives[0].transcript))
    return {"Text : {}".format(response.results[0].alternatives[0].transcript)}







# including api routes
# app.include_router(api_router, prefix=settings.API_V1_STR)

