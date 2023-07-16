from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import transformers
import torch

import speech_recognition as sr

from pymongo import MongoClient
from datetime import date
import datetime
import subprocess

from elevenlabs import User
from elevenlabs import set_api_key
import assemblyai as aai

import requests
import json
from dotenv import load_dotenv
import os

model = "tiiuae/falcon-7b-instruct"
model=AutoModelForCausalLM.from_pretrained(model, trust_remote_code=True)

load_dotenv()
set_api_key(os.getenv("11ai"))

#voice id : TxGEqnHWrfWFTfGW9XjX from elevenlabs
# this is a standard voice in elevenlabs

aai.settings.api_key = os.getenv("aai")
transcriber = aai.Transcriber()
#transcript = transcriber.transcribe("testassemblyai.wav")

#### boiler plate #####
tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

def generate_chat(prompt):
    sequences = pipeline(
        #"Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
        prompt,
        max_length=200,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )
    for seq in sequences:
        #print(f"Result: {seq['generated_text']}")
        print(f"{seq['generated_text']}")
#### end boiler plate #####

endChat = True
while(endChat):
    print("\033c")
    userInput = input("prompt: ")
    if userInput != "endchat":
        generate_chat(userInput)
    else:
        endChat = False
