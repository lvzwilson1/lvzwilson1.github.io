# imports
import requests
import json

# set values
url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/554351"

cookies = {"espn_s2": "AEAdhzG%2FqHqQvSozP7tIGsj2D3W0gBiJd57XgcsY5eYs9BXTEmMhCbwOu0c8mAxSb9hkgu9bwLonKukAs3NJA0hNXTBzx%2BCD0i7wLtRgKHg%2Bmyb19XQ5i2S%2F7oigMX8JyFnukDDbx6IN4BCQHQE1N2sPf66Td3D8GQovg1yVmbOZJEF1kWEsSIVUar6xmxvq15aM2nQNP%2FTgFC6fQgR3rDRXzsNXeWGULoTM8lA4D2QcFDMEsuJhhzXKxhtMsDg%2FkYwN98MgRAOzozfZoj1BLiPZ",
           "SWID": "{8E969096-152C-432E-9690-96152CF32E34}"}

# get request - mMatchup view
r = requests.get(url, params = {"view": "mMatchup"}, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/mMatchup.txt', 'w') as outfile:
    json.dump(d, outfile)
print("Downloaded Matchup Data")

# get request - mTeam view
r = requests.get(url, params = {"view": "mTeam"}, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/mTeam.txt', 'w') as outfile:
    json.dump(d, outfile)
print("Downloaded Team Data")

# get request - league Data
r = requests.get(url, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/leagueData.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - boxscore
print("Downloading Detailed Boxscore data")
r = requests.get(url, params = {"view": "mMatchupScore"}, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/boxscore.txt', 'w') as outfile:
    json.dump(d, outfile)
print("Downloaded Bozscore Data")

# get request - boxscore2
for weeks in range(1, 10):
    r = requests.get(url + '?view=mMatchup&view=mMatchupScore', params={'scoringPeriodId': weeks, 'matchupPeriodId': weeks}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Desktop/fantasy/untitled/boxscore2" + str(weeks) + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)
    print(weeks)
print("Downlaoded!")
