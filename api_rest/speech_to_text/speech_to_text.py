"""Libraries that i have to have to use Speech to Text, and IAMAuthenticator to pass my credientials
os - Deal with files
dotenv - Loading api key and url 
json - to return text in its format
"""

#This is not my product, i'm using only for fun and learn with API. Speech to Text is a property from IBM.

import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import os
from dotenv import load_dotenv

from save_file import save_transcription

#Loading local variables
load_dotenv()

#Setting api key and url from Speech to Text
stt_key = os.getenv("STT_KEY")
stt_url = os.getenv("STT_URL")

def speech_to_text(audio_file_path):
    """audio_file_path -> file to make into text
    return -> Transcription"""
    authenticator = IAMAuthenticator(stt_key)
    speech_to_text = ibm_watson.SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(stt_url)

    #try:

    with open(audio_file_path, "rb") as audio_file:
        response = speech_to_text.recognize(
            audio=audio_file,
            model="de-DE_Multimedia",
            #Or you can use other files, check: https://cloud.ibm.com/apidocs/speech-to-text
            content_type="audio/wav"  
            ).get_result()

        response_json = json.dumps(response, indent=4)
  
        
        return response_json 
    #except ValueError as e:
       # print(f"{e}")


#Example for test
#I'm giving an audio file in german, but you can use other languages availables on IBM's STT. don't forget to chance its model.
audio_path = '../audios_example/hallo_welt.wav'  

text = speech_to_text(audio_path)
print(text)
save_transcription(text)