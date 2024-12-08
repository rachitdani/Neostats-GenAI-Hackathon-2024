# AI-Powered Financial Summaries for company annual report

## Overview
Developing a generative AI model using Azure OpenAI Services to produce concise, accurate, and professional financial summaries from provided financial reports in PDF format. The goal is to create a solution capable of generating a 1-page summary for any public company’s financial report, highlighting key financial metrics and summarizing risk factors.

## Use Case Description
### Challenge
1. An overall Performance Summary
2. Calculated figures in a table for the following financial ratios:
   - Current Ratio
   - Debt-to-Equity Ratio
   - Return on Equity (ROE)
   - Return on Assets (ROA)
   - Gross Profit Margin
   - Net Profit Margin
   - Earnings Per Share (EPS)
3. A Summary of Risk Factors provided in the annual report.

### Input Data
- Annual Financial Report of Amazon for the year 2023 in PDF format you can also input any other annual report of a company

### Model Usage
Participants must use the provided OpenAI model credentials (Azure OpenAI GPT-4 and Azure AI Document Intelligence) to perform tasks:
- **Azure OpenAI**: Utilize the AzureOpenAI API to generate text summaries and perform specific text-based tasks.
- **Azure AI Document Intelligence**: Extract and interpret data from PDF documents, including tables and text.

## Requirements and Scope
- Participants will develop their solutions within a 3-hour time frame (10 am – 1 pm).
- The solution should produce:
  1. A file containing the calculated figures for the financial ratios.
  2. A document with the overall performance summary and risk factor summary.


## Folder Structure
```
├── rough/                                      # Directory containing the rough files creating for testing the working of a task
├── notebooks/                                  # Jupyter notebooks for data preprocessing and model testing
├── annual report.pdf                           # The file used for summarising text
├── content.txt                                 # It contains the extracted pdf data in a text file to save cost so everytime the intelligence api is not called
├── .env                                        # Contains the envirnonment variables used in the code
├── summary.txt                                 # Output file which contains the generalised summary of the input file
├── Neo GenAI hackathon'24 -excel- Rachit.txt   # Output file which contains the metrics obtained from the data
├── riskfactor_summary.txt                      # Output file which contains the risk summary derived from the input file
├── README.md                                   # This file
└── requirements.txt                            # List of required Python packages
```

## How to Use
### 1. Set up your environment
1. Clone this repository:
   ```bash
   git clone https://github.com/rachitdani/Neostats-GenAI-Hackathon-2024.git
   cd Neostats-GenAI-Hackathon-2024
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Obtain API keys
- Obtain the Azure OpenAI API key and Azure AI Document Intelligence API key from your Azure portal.
- Set the keys as environment variables in the env file:
   ```bash
   AZURE_OPENAI_API_KEY="your_openai_api_key"
   AZURE_OPENAI_ENDPOINT="your_openai_endpoint"
   AZURE_OPENAI_DEPLOYMENT_NAME = "your_openai_model_name"
   AZURE_OPENAI_API_VERSION = "your_version_number" 
   DOCUMENTINTELLIGENCE_API_KEY="your_document_intelligence_api_key"
   DOCUMENTINTELLIGENCE_ENDPOINT="your_document_intelligence_endpoint"
   DOCUMENTINTELLIGENCE_API_VERSION = "your_document_intelligence_model_name"
   DOCUMENTINTELLIGENCE_API_NAME = "your_document_intelligence_model_name"
   ```

### 3. Run the Scripts
1. **Data Ingestion**: Use your particular file to ingest the financial report, extract relevant tables, and text and change the path in the 'main.py'.
2. **Generate Summaries**: Run `main.py` to generate performance summaries using Azure OpenAI and generate text files.


---
