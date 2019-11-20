# imports
import requests
import json

# set values
url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/554351"

# Get cookie values from secret file
with open ("C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Cookies/espn_s2.txt", "r") as myfile:
    espn_s2=myfile.readlines()

with open ("C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Cookies/SWID.txt", "r") as myfile:
    SWID=myfile.readlines()

cookies = {"espn_s2": espn_s2[0], "SWID": SWID[0]}

# get request - league Data
r = requests.get(url, cookies=cookies)
d = r.json()
with open('C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Data/leagueData.txt', 'w') as outfile:
    json.dump(d, outfile)

# get request - mMatchup view
reports = ["mMatchup", "mTeam", "mMatchupScore", "kona_player_info", "mSettings"]
for report in reports:
    r = requests.get(url, params = {"view": report}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Data/" + report + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)

# get request - boxscore2 (player level data - for each team)
for weeks in range(1, 12):
    r = requests.get(url + '?view=mMatchup&view=mMatchupScore', params={'scoringPeriodId': weeks, 'matchupPeriodId': weeks}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Data/boxscore2" + str(weeks) + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)

# get request - kona_view (player level data for the entire year, not team specific)
for weeks2 in range(1, 12):
    r = requests.get(url + '?view=kona_player_info', params={'scoringPeriodId': weeks2}, cookies=cookies)
    d = r.json()
    filename = "C:/Users/lvwilson/Documents/GitHub/lvzwilson1.github.io/Ignore/Data/kona_player_info_" + str(weeks2) + ".txt"
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)
