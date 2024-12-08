import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_MODEL_VERSION = os.getenv("AZURE_OPENAI_MODEL_VERSION") 


client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT

)
deployment_name = AZURE_OPENAI_DEPLOYMENT_NAME

'''
completion = client.chat.completions.create(
    model=AZURE_OPENAI_MODEL_VERSION,
    messages=[
        {
            "role": "user",
            "content": "what is a capital of delhi?",
        }
    ]
)'''
      
print('Sending a test completion job')

start_phrase = 'Write a tagline for Neostats hackathon. '
response=client.completions.create(model=deployment_name,
prompt=start_phrase, max_tokens=10)
print(start_phrase+response.choices[0].text)


