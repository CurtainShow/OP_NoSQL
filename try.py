from genericpath import exists
import json
import time

# ! Get The Information About User After Calling API
json_file = open('AccountInfos.json')
data = json.load(json_file)

# ! Parsing the dictionarry user
user_puuid = data['puuid']

# ! Get The Information About User Game After Calling API
json_file_game_1 = open('AccountMatchInfos_100.json')
data_game_1 = json.load(json_file_game_1)

# ! Parsing the dictionarry user games
match_type = data_game_1[10]['gameMode']
match_duration = data_game_1[10]['gameDuration']
match_result = ""

for user in data_game_1:
    try:
        #print(user)
        game_user_puuid = user['puuid']
        if game_user_puuid == user_puuid:
            if user['win'] == True:
                match_result = "Victoire"
            elif user['win'] == False:
                match_result = "Défaite"
    except KeyError:
        pass

print(match_type)
print(match_duration)
print(match_result)