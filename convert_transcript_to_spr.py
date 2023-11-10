import os
from time import sleep
from halo import Halo
import openai
from openai import OpenAI
from pprint import pprint


###     file operations


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)



def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


###     API functions


# Define the chatbot function
def chatbot(conversation, model="gpt-4-1106-preview", temperature=0, max_tokens=2000):
    max_retry = 7
    retry = 0
    while True:
        try:
            client = OpenAI(api_key = open_file('key_openai.txt').strip())            
            
            spinner = Halo(text='Thinking...', spinner='dots')
            spinner.start()
            response = client.chat.completions.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
            spinner.stop()
            
            text = response.choices[0].message.content
            tokens = response.usage.total_tokens
                        
            return text, tokens
        except Exception as oops:
            retry += 1
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            sleep(5)
            if retry >= max_retry:
                exit()


# Define the function to use the ChatGPT API
def use_chatgpt(system_message, user_message):
    conversation = list()
    conversation.append({'role': 'system', 'content': system_message})
    conversation.append({'role': 'user', 'content': user_message})
    text, tokens = chatbot(conversation)
    return text






if __name__ == '__main__':
    # Read the system message
    system_message = open_file('system_spr.txt')

    # Path to the transcripts and sprs folders
    transcripts_folder = 'transcripts'
    sprs_folder = 'sprs'

    # Ensure the sprs folder exists
    #os.makedirs(sprs_folder, exist_ok=True)

    # Process each transcript file
    for filename in os.listdir(transcripts_folder):
        if filename.endswith('.txt'):
            transcript_path = os.path.join(transcripts_folder, filename)
            spr_path = os.path.join(sprs_folder, filename)
            print(transcript_path)

            # Read the transcript content
            user_message = open_file(transcript_path)

            # Get the response from ChatGPT
            text = use_chatgpt(system_message, user_message)
            print(text)

            # Save the response
            save_file(spr_path, text)

            print(f'Processed and saved SPR for {filename}')