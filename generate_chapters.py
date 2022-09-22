import re
import os
import openai
import textwrap
from time import time,sleep


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.0, top_p=1.0, tokens=500, freq_pen=0.0, pres_pen=0.0, stop=['asdfasdf', 'asdasdf']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()  # force it to fix any unicode errors
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            text = re.sub('\s+', ' ', text)
            filename = '%s_gpt3.txt' % time()
            save_file('gpt3_logs/%s' % filename, prompt + '\n\n==========\n\n' + text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(1)


if __name__ == '__main__':
    transcript = open_file('captions.sbv').split('\n\n')
    chunk_size = 20
    chunks = [transcript[i:i + chunk_size] for i in range(0, len(transcript), chunk_size)]
    results = list()
    for chunk in chunks:
        chunk = '\n'.join(chunk)
        print('\n\n',chunk)
        prompt = open_file('prompt.txt').replace('<<TRANSCRIPT>>', chunk)
        response = gpt3_completion(prompt)
        print('\n\n', response)
        results.append(response)
    output = '\n'.join(results)
    print('\n\nFinal Output:\n', output)
    save_file('chapters.txt', output)