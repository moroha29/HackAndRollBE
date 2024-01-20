import json

input_json= open('result.json', 'r', encoding="utf-8")

# Transform json input to python objects
input_dict = json.load(input_json)
messages=input_dict['messages']

# Filter python objects with list comprehensions
messages = [x['poll'] for x in messages if 'poll' in x]
final_data=r""""""
for x in messages[-301:]:
    # temp="["
    # for i in x['answers']:temp+=json.dumps(i)+","
    # temp=temp[:-1]+"]"
    temp=x['answers'][0]['text']
    for i in range(len(x['question'])): 
        if "\""==x['question'][i]: x['question']=x['question'][:i]+"'"+x['question'][i+1:]
    for i in range(1,len(x['answers'])):
        temp+=" || "+x['answers'][i]['text']
    final_data+="{\"messages\": [{\"role\": \"system\", \"content\": \"PaisehBot is a generative bot that comes up with random extremely embarrassing question relating to an individual personal life and life choices and give options to the questions.\"}, {\"role\": \"user\", \"content\": \"Give me a paiseh question\"}, {\"role\": \"assistant\", \"content\": \""+"Question:"+x['question']+" Options:"+temp+"\"}]}\n"
# final_data=[{"messages": [{"role": "system", "content": "PaisehBot is a generative bot that comes up with random embarrassing question."}, {"role": "user", "content": "Give me a paiseh question"}, {"role": "assistant", "content": {'question':x['question'],'answers':x['answers']}}]} for x in messages]

# Transform python object back into json
# output_json = json.dumps(final_data[-101:])

with open("filtered.jsonl", "w",encoding="utf-8") as outfile: 
    outfile.write(final_data)

input_json.close()
