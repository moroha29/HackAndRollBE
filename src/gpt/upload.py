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
#   training_file="file-qrnxYZ11iDhhE6J3e8sJcIfx",
#   model="gpt-3.5-turbo-1106"
# )



# print(client.fine_tuning.jobs.list(limit=10))
# client.models.delete("ft:gpt-3.5-turbo-1106:personal::8j3o6R3G")

async def fetch_generated() -> str:
  response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal::8j7HEAKl",
    messages=[
      {"role": "system", "content": "PaisehBot is a generative bot that comes up with random slightly embarrassing question relating to an individual personal life and life choices and give options to the questions. Vulgarities are not allowed."},
      {"role": "user", "content": "Give me a paiseh question"}
    ]
  )
  return response.choices[0].message.content
