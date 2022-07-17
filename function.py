from riotwatcher import LolWatcher
import json

def get_user_informations(user_region, user):

    api_key = 'RGAPI-768271ad-868d-4f83-8a46-39dfc9bf7d53'
    watcher = LolWatcher(api_key)

    me = watcher.summoner.by_name(user_region, user)
    #print(me)

    # Return the rank status for Doublelift
    my_ranked_stats = watcher.league.by_summoner(user_region, me['id'])
    #print(my_ranked_stats)

    my_matches = watcher.match.matchlist_by_puuid(user_region, me['puuid'])
    #print(my_matches)

    # fetch last match detail
    last_match = my_matches[-1]
    match_detail = watcher.match.by_id(user_region, last_match) #'EUW1_5839753103'
    #print(match_detail)

    # ? Data Dragon part 

    #latest = watcher.data_dragon.versions_for_region(User_region)['n']['champion']
    #static_champ_list = watcher.data_dragon.champions(latest, False, 'fr_FR')

    #latestItem = watcher.data_dragon.versions_for_region(User_region)['n']['item']
    #static_items_list = watcher.data_dragon.items(latest, 'fr_FR')

    #print(match_detail['info']['participants'][0])


    # ! Create and add to dict section - Account Informations


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

    # ! Create and add to dict section - Matchs Informations

    i = 100
    for element in my_matches:
        match_detail = watcher.match.by_id(user_region, element)
        game_length = match_detail['info']['gameDuration']
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

        file_name = 'AccountMatchInfos_',str(i),'.json'
        joined_file_name = "".join(file_name)
        #print(joined_file_name)

        with open(joined_file_name, 'w', encoding='utf8') as mon_fichier:
            json.dump(participants, mon_fichier, ensure_ascii=False)
        
        i+=1


    with open('AccountInfos.json', 'w', encoding='utf8') as mon_fichier:
        json.dump(UserInformations, mon_fichier, ensure_ascii=False)