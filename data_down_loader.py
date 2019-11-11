# imports
import requests
import json

# set values
url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/554351"

cookies = {XXXX}

# get request - mMatchup view
r = requests.get(url, params = {"view": "mMatchup"}, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/mMatchup.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - mTeam view
r = requests.get(url, params = {"view": "mTeam"}, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/mTeam.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - league Data
r = requests.get(url, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/leagueData.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - boxscore
r = requests.get(url, params = {"view": "mMatchupScore"}, cookies=cookies)
d = r.json()

with open('C:/Users/lvwilson/Desktop/fantasy/untitled/boxscore.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - boxscore2
for weeks in range(1, 10):
    r = requests.get(url + '?view=mMatchup&view=mMatchupScore', params={'scoringPeriodId': weeks, 'matchupPeriodId': weeks}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Desktop/fantasy/untitled/boxscore2" + str(weeks) + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)
    print(weeks)


