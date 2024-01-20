from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

client = OpenAI()

# print(client.files.list())

# client.files.create(
#   file=open("filtered.jsonl", "rb"),
#   purpose="fine-tune"
# )

# client.fine_tuning.jobs.create(
#   training_file="file-C3ZdwglFBfArtje2t0mBtH12",
#   model="gpt-3.5-turbo-1106"
# )

# print(client.fine_tuning.jobs.list(limit=10))

async def fetch_generated() -> str:
  response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal::8j3o6R3G",
    messages=[
      {"role": "system", "content": "PaisehBot is a generative bot that comes up with random extremely embarrassing question relating to an individual personal life."},
      {"role": "user", "content": "Give me a paiseh question"}
    ]
  )
  return response.choices[0].message.content
