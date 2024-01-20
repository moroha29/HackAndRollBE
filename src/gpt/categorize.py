import json

input_json= open('result.json', 'r', encoding="utf-8")

# Transform json input to python objects
input_dict = json.load(input_json)
messages=input_dict['messages']

# Filter python objects with list comprehensions
messages = [x['poll']['question'] for x in messages if 'poll' in x]

with open("question_bank.json", "w") as outfile: outfile.write(json.dumps(messages))

input_json.close()
