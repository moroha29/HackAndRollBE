from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional

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


async def fetch_generated() -> Optional[dict]:
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:personal::8j7HEAKl",
        messages=[
            {
                "role": "system",
                "content": "PaisehBot is a generative bot that comes up with random slightly embarrassing question relating to an individual personal life and life choices and give options to the questions. Vulgarities are not allowed.",
            },
            {"role": "user", "content": "Give me a paiseh question"},
        ],
    )

    raw_question = response.choices[0].message.content

    if raw_question is None or len(raw_question) < 10:
        return None
    raw_question: str

    x = raw_question.split(" Options:")
    if len(x) != 2:
        return None
    question, options = x
    if not question.startswith("Question:"):
        return None
    question = question[9:]
    raw_options = options.split(" || ")
    options = set()
    for o in raw_options:
        x = o.split(" - ")
        if len(x) == 2:
            o = x[1]
        if not o or o.isspace():
            continue
        options.add(o.strip().lower())
    options.add("check results")
    options = list(options)

    return {
        "question": question,
        "options": options,
    }
