# imports
import requests
import json

# set values
url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/554351"

# Get cookie values from secret file
with open ("C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Cookies/espn_s2.txt", "r") as myfile:
    espn_s2=myfile.readlines()

with open ("C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Cookies/SWID.txt", "r") as myfile:
    SWID=myfile.readlines()

cookies = {"espn_s2": espn_s2[0], "SWID": SWID[0]}

# get request - league Data
r = requests.get(url, cookies=cookies)
d = r.json()
with open('C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Data/leagueData.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - mMatchup view
reports = ["mMatchup", "mTeam", "mMatchupScore"]
for report in reports:
    r = requests.get(url, params = {"view": report}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Data/" + report + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)

# get request - boxscore2 (player level data)
for weeks in range(1, 10):
    r = requests.get(url + '?view=mMatchup&view=mMatchupScore', params={'scoringPeriodId': weeks, 'matchupPeriodId': weeks}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Data/boxscore2" + str(weeks) + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)
