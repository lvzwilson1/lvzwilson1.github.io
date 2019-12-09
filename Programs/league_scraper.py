# imports
import requests
import json
import numpy as np
import pandas as pd

# set values
url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/'
datadir = 'C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Data/'

response_codes = []
message_body = []

# get request - league Data
for leagueID in range(500000, 510000):
  leagueURL = url + str(leagueID)
  r = requests.get(leagueURL)
  response_codes.append(r.status_code)
  message_body.append(r.text)
  
  if r.status_code == 200:
    d = r.json()
    filename_str = datadir + "/leagueData_" + str(leagueID) + ".txt"
    with open(filename_str, 'w') as outfile:
      json.dump(d, outfile)

  print(leagueID)

IDs = list(range(500000, 510000))

d = {'ID': IDs, 'statusCode': response_codes, 'textResponse': message_body}
df = pd.DataFrame(d)

messages = set(message_body)
print(messages)
