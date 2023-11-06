import openai
import time
import csv
from tqdm import tqdm

def gpt(inp):
    # Set your OpenAI API key here
    api_key = 'APIKEY'

    # Initialize the OpenAI API client
    openai.api_key = api_key
    # Send a message to ChatGPT
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      request_timeout=15,

      messages=[
            {"role": "system", "content": "You are a Dungeon Master, doing a master narration in DND context."},
            {"role": "user", "content": inp},
        ]
    )

    # Extract and print the model's reply
    model_reply = response.choices[0].message.content.strip()
    if not model_reply:
        print(response)
    # Store the model's reply in the responses array
    # responses.append({"User": user_input, "ChatGPT": model_reply})
    return model_reply

# Specify the file path
file_path = "prompts_DND.csv"  # Replace with your file's path

with open(file_path, 'r', newline='') as file:
    file_cont = csv.reader(file)
    retries = 10
    min_num = 1148
    while retries > 0:
        try:
            a = -1
            for line in tqdm(file_cont, total=11250000):
                a += 1
                if a > min_num:
                    min_num = a
                    text = f"Explain without repeating the adjectives: {line[0]}. In one Paragraph."
                    res = gpt(text)
                    li = [line[0], res]
                    with open('prompt0.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(li)

        except Exception as e:
            if e:
                print(e)
                print('Timeout error, retrying...')
                retries -= 1
                time.sleep(5)
            else:
                raise e





