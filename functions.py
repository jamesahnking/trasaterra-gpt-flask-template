import json
import requests
import os
from openai import OpenAI
from prompt import assistant_instructions

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
AIRTABLE_API_KEY = os.environ['AIRTABLE_API_KEY']
# GOOGLE_CLOUD_API_KEY = os.environ['GOOGLE_CLOUD_API_KEY']

# Init OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)


# Add lead to Airtable
def create_airtable_lead(name, email, website, address, phone, company):

    # Change this to your Airtable API URL
    url = "https://api.airtable.com/v0/appVHNAaGxUtarZKr/Leads"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "records": [{
            "fields": {
                "Name": name,
                "Email": email,
                "Website": website,
                "Address": address,
                "Phone": phone,
                "Company": company
            }
        }]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Lead created successfully - STATUS CODE:", response.status_code)
        # logging.info("Logging Info - Lead created successfully")
        return response.json()
    else:
        print("ERROR: Lead was not created - STATUS CODE:", response.status_code)


# Create or load assistant
def create_assistant(client):
    assistant_file_path = 'assistant.json'

    # If there is an assistant.json file already, then load that assistant
    if os.path.exists(assistant_file_path):
        with open(assistant_file_path, 'r') as file:
            assistant_data = json.load(file)
            assistant_id = assistant_data['assistant_id']
            print("Loaded existing assistant ID.")
    else:
        # If no assistant.json is present, create a new assistant using the below specifications

        # To change the knowledge document, modifiy the file name below to match your document
        # If you want to add multiple files, paste this function into ChatGPT and ask for it to add support for multiple files
        file = client.files.create(file=open("knowledge.docx", "rb"),
                                   purpose='assistants')

        assistant = client.beta.assistants.create(
            # Getting assistant prompt from "prompts.py" file, edit on left panel if you want to change the prompt
            instructions=assistant_instructions,
            model="gpt-4-1106-preview",
            tools=[
                {
                    "type": "retrieval"  # This adds the knowledge base as a tool
                },
                {
                    "type": "function",  # This adds the lead capture as a tool
                    "function": {
                        "name": "create_airtable_lead",
                        "description":
                        "Capture and send the users contact information to Airtable to be saved.",
                        "parameters": {
                            "type":
                            "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "The name of the user."
                                },
                                "email": {
                                    "type": "string",
                                    "description": "The email of the user."
                                },
                                "website": {
                                    "type": "string",
                                    "description":
                                    "The company the user represents."
                                },
                                "address": {
                                    "type":
                                    "string",
                                    "description":
                                    "Address if the company the user represents."
                                },
                                "phone": {
                                    "type": "string",
                                    "description": "The phone number of the user."
                                },
                                "company": {
                                    "type": "string",
                                    "description":
                                    "The company the user represents."
                                },
                            },
                            "required": [
                                "name", "email", "website", "address", "phone",
                                "company"
                            ]
                        }
                    }
                }
            ],
            file_ids=[file.id])

        # Create a new assistant.json file to load on future runs
        with open(assistant_file_path, 'w') as file:
            json.dump({'assistant_id': assistant.id}, file)
            print("Created a new assistant and saved the ID.")

        assistant_id = assistant.id

    return assistant_id
