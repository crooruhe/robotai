from transformers import AutoTokenizer, AutoModelForCausalLM
from elevenlabs import User
from elevenlabs import set_api_key
from dotenv import load_dotenv

import os
import transformers
import torch
import assemblyai as aai

model = "tiiuae/falcon-7b"

load_dotenv()
set_api_key(os.getenv("11ai"))

#voice id : TxGEqnHWrfWFTfGW9XjX from elevenlabs
# this is a standard voice in elevenlabs
aai.settings.api_key = os.getenv("aai")
transcriber = aai.Transcriber()

#transcript = transcriber.transcribe("testassemblyai.wav")

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
sequences = pipeline(
    "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")