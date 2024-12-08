import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import numpy as np
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

load_dotenv()
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")


client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT

)
deployment_name = AZURE_OPENAI_DEPLOYMENT_NAME
test_prompt = "Write a tagline for Neostats hackathon. "


def test_model():

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[{"role": "user", "content": test_prompt}],
            temperature=0.7,
        )
        print("Model response:", response.choices[0].message.content)
    except Exception as e:
        print("Error:", str(e))


def get_content(file_path):
    document_analysis_client = DocumentAnalysisClient(
        endpoint="https://neohack.cognitiveservices.azure.com/",  
        credential=AzureKeyCredential("D4Vd1Xljol6cS0q8PoZiQFXz8uH1yYeXCIyhTHU5vdBxBhbeX9JLJQQJ99ALACYeBjFXJ3w3AAALACOGIiVt")  
    )

    # Open the file in binary mode
    with open(file_path, "rb") as file:
        poller = document_analysis_client.begin_analyze_document("prebuilt-layout", document=file)
        result = poller.result()
        return result.content

def variable_to_file(file_path,content):
        with open(file_path, 'w') as file:
            file.write(content)

        print("Information has been written to", file_path)

def data_in_text(file_path):
    try:
        content = get_content(file_path)
        file_path = "content.txt"
        variable_to_file(file_path,content)
        return content

    except Exception as e:
        print(f"Error: {e}")


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))





if __name__ == "__main__":
    test_model()
    file_path = "/Users/rachit/Desktop/Hackathon_GenAi/Amazon-com-Inc-2023-Annual-Report.pdf"
    content = data_in_text(file_path)
    print(type(content))
    content = []
    with open("content.txt") as f:
        state_of_the_union = f.read()
        content.append(state_of_the_union)
    '''
    # Load example document
    with open("content.txt") as f:
        state_of_the_union = f.read()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    texts = text_splitter.create_documents([state_of_the_union])
    print(texts[0])'''

    ## Part 1 Summary
    prompt_template = '''
    Generate an overall Performance Summary of the following annual report:
    Report Data : {report}
    '''
    prompt=PromptTemplate(
    input_variables=['report'],
    template=prompt_template)

    complete_prompt=prompt.format(report=content)
    print(complete_prompt)
    response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a expert assistant in summarizing a annual report document of a company"},
                {"role": "user", "content": complete_prompt}],
            temperature=0.7,
        )
    print("Model response:", response.choices[0].message.content)
    summary_1 = response.choices[0].message.content 
    path = "summary.txt"
    variable_to_file(path,summary_1)


    ## Part 2 
    prompt_template = '''
    Help me calculate the values of 
    1)Current Ratio
    2)Debt-to-Equity Ratio
    3)Return on Equity (ROE)
    4)Return on Assets (ROA)
    5)Gross Profit Margin
    6)Net Profit Margin
    7)Earnings Per Share (EPS) from the report data and return it an json format which can be converted to excel
    Report Data : {report}
    '''
    prompt=PromptTemplate(
    input_variables=['report'],
    template=prompt_template)

    complete_prompt=prompt.format(report=content)
    print(complete_prompt)
    response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a expert assistant in getting the financial metrics of a company"},
                {"role": "user", "content": complete_prompt}],
            temperature=0.7,
        )
    print("Model response:", response.choices[0].message.content)
    summary_2 = response.choices[0].message.content 
    path = "Neo GenAI hackathon'24 -excel- Rachit.txt"
    variable_to_file(path,summary_2)

    ## Part 3
    prompt_template = '''
    Generate an overall Summary of the risk factor provided on the annual report:
    Report Data : {report}
    '''
    prompt=PromptTemplate(
    input_variables=['report'],
    template=prompt_template)

    complete_prompt=prompt.format(report=content)
    print(complete_prompt)
    response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a expert assistant in summarizing a financial report document of a company"},
                {"role": "user", "content": complete_prompt}],
            temperature=0.7,
        )
    print("Model response:", response.choices[0].message.content)
    risk_summary = response.choices[0].message.content 
    path = "riskfactor_summary.txt"
    variable_to_file(path,risk_summary)


    path = "Neo GenAI hackathon'24 -word Rachit.txt"
    with open(file_path, 'w') as file:
            file.write("Performance Summary") 
            file.write(summary_1)
            file.write("Risk Factor Summary\n\n")
            file.write(risk_summary)
        
    print("Information has been written to", path)
    






    


