from riotwatcher import LolWatcher, ApiError
import json

# ! Variables section

# golbal variables
api_key = 'RGAPI-d10ba149-0c45-4012-b06d-51bef6644a86'
watcher = LolWatcher(api_key)
User = 'Avoid My Grab'
User_region = 'euw1'

# ! Init user section

#User = input("Enter your user id : ")
#User_region = input("Enter your game region : ")

me = watcher.summoner.by_name(User_region, User)
#print(me)

# Return the rank status for Doublelift
my_ranked_stats = watcher.league.by_summoner(User_region, me['id'])
#print(my_ranked_stats)

my_matches = watcher.match.matchlist_by_puuid(User_region, me['puuid'])
print(my_matches)

# fetch last match detail
last_match = my_matches[-1]
match_detail = watcher.match.by_id(User_region, last_match) #'EUW1_5839753103'
print(match_detail)

latest = watcher.data_dragon.versions_for_region(User_region)['n']['champion']
static_champ_list = watcher.data_dragon.champions(latest, False, 'fr_FR')

latestItem = watcher.data_dragon.versions_for_region(User_region)['n']['item']
static_items_list = watcher.data_dragon.items(latest, 'fr_FR')

#print(match_detail['info']['participants'][0])


# ! Create and add to dict section


game_length = match_detail['info']['gameDuration']

UserInformations = {}
UserInformations['id'] = me['id']
UserInformations['accountId'] = me['accountId']
UserInformations['puuid'] = me['puuid']
UserInformations['name'] = me['name']
UserInformations['profileIconId'] = me['profileIconId']
UserInformations['revisionDate'] = me['revisionDate']
UserInformations['summonerLevel'] = me['summonerLevel']
UserInformations['leagueId'] = my_ranked_stats[0]['leagueId']
UserInformations['queueType'] = my_ranked_stats[0]['queueType']
UserInformations['tier'] = my_ranked_stats[0]['tier']
UserInformations['rank'] = my_ranked_stats[0]['rank']
UserInformations['leaguePoints'] = my_ranked_stats[0]['leaguePoints']
UserInformations['wins'] = my_ranked_stats[0]['wins']
UserInformations['losses'] = my_ranked_stats[0]['losses']

#print(UserInformations)

participants = []
for row in match_detail['info']['participants']:
    #print(row)
    participants_row = {}
    participants_row['puuid'] = row['puuid']
    participants_row['profileIcon'] = row['profileIcon']
    participants_row['championName'] = row['championName']
    participants_row['championId'] = row['championId']
    participants_row['lane'] = row['lane']
    participants_row['kills'] = row['kills']
    participants_row['deaths'] = row['deaths']
    participants_row['assists'] = row['assists']
    participants_row['item0'] = row['item0']
    participants_row['item1'] = row['item1']
    participants_row['item2'] = row['item2']
    participants_row['item3'] = row['item3']
    participants_row['item4'] = row['item4']
    participants_row['item5'] = row['item5']
    participants_row['item6'] = row['item6']
    participants_row['goldEarned'] = row['goldEarned']
    participants_row['detectorWardsPlaced'] = row['detectorWardsPlaced']
    participants_row['win'] = row['win']

    #participants_row['item0'] = static_items_list['data'][str(row['item0'])]['name']
    #participants_row['item1'] = static_items_list['data'][str(row['item1'])]['name']
    #participants_row['item2'] = static_items_list['data'][str(row['item2'])]['name']
    #participants_row['item3'] = static_items_list['data'][str(row['item3'])]['name']
    #participants_row['item4'] = static_items_list['data'][str(row['item4'])]['name']
    #participants_row['item5'] = static_items_list['data'][str(row['item5'])]['name']
    #participants_row['item6'] = static_items_list['data'][str(row['item6'])]['name']

    participants.append(participants_row)

#print(participants)  

game_duration = {"gameDuration" : game_length, "gameMode" : match_detail['info']['gameMode'], "gameType" : match_detail['info']['gameType']}
participants.append(game_duration)


with open('AccountMatchInfos.json', 'w', encoding='utf8') as mon_fichier:
	json.dump(participants, mon_fichier, ensure_ascii=False)

with open('AccountInfos.json', 'w', encoding='utf8') as mon_fichier:
	json.dump(UserInformations, mon_fichier, ensure_ascii=False)

#print(static_items_list['data']['8001'])
