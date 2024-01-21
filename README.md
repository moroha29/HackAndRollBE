# HackAndRollBE

# Server
## To initialize the server run the following command
```bash
uvicorn src.main:app --reload
```

# Machine Learning
**Note:** Everything is stored inside the gpt file while the JSON files for storing are stored in the src. There is a category feature but not fully implemented due to fine tuning costs with gpt3.5 and the amount of data needed to fit in.
## Rough steps for doing a fine tuning model
  - filter.py has the filter to make the .JSONL from the extracted data of the PaisehBot from telegram stored in the result.json in a specific format for feeding into the fine tuning model
  - put in the filtered.JSONL into checker.py to check if the JSONL is in a valid format to feed into the api
  - upload the file to GPT before using it to fine tune the model then run the prompt to generate out a question geneerated by GPT with the options
