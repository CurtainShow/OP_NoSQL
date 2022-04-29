import json

def delChamp():
    f = open('/dragontail-12.6.1/12.6.1/data/fr_FR/championFull.json')

    data = json.load(f)
    #for i in data['data']:
        #print(data['data'][i]['id'])
    f.close()

    data2 = data

    del data2['keys']
    for i in data2['data']:
        del data2['data'][i]['allytips']
        del data2['data'][i]['enemytips']
        del data2['data'][i]['blurb']
        del data2['data'][i]['tags']
        del data2['data'][i]['partype']
        del data2['data'][i]['recommended']

    f = open('/dragontail-12.6.1/12.6.1/data/fr_FR/championFull.json', 'w')

    json.dump(data2, f)
    f.close()

def delSumm():
    f = open('/dragontail-12.6.1/12.6.1/data/fr_FR/summoner.json')

    data = json.load(f)
    f.close()

    data2 = data

    for i in data2['data']:
        del data2['data'][i]['maxrank']
        del data2['data'][i]['costBurn']
        del data2['data'][i]['datavalues']
        del data2['data'][i]['effect']
        del data2['data'][i]['effectBurn']
        del data2['data'][i]['vars']
        del data2['data'][i]['summonerLevel']
        del data2['data'][i]['modes']
        del data2['data'][i]['costType']
        del data2['data'][i]['maxammo']
        del data2['data'][i]['range']
        del data2['data'][i]['rangeBurn']
        del data2['data'][i]['resource']
        del data2['data'][i]['cooldown']

    f = open('/dragontail-12.6.1/12.6.1/data/fr_FR/summoner.json', 'w')

    json.dump(data2, f)
    f.close()

def delItem():
    f = open('/dragontail-12.6.1/12.6.1/data/fr_FR/item.json')

    data = json.load(f)
    f.close()

    data2 = data

    del data2['basic']
    del data2['tree']
    del data2['groups']

    for i in data2['data']:
        del data2['data'][i]['gold']
        del data2['data'][i]['tags']
        del data2['data'][i]['maps']
        del data2['data'][i]['stats']
        if 'depth' in data['data'][i]:
            del data2['data'][i]['depth']
        if 'from' in data['data'][i]:
            del data2['data'][i]['from']
        if 'into' in data['data'][i]:
            del data2['data'][i]['into']
        if 'consumed' in data['data'][i]:
            del data2['data'][i]['consumed']
        if 'inStore' in data['data'][i]:
            del data2['data'][i]['inStore']
        if 'hideFromAll' in data['data'][i]:
            del data2['data'][i]['hideFromAll']
        if 'stacks' in data['data'][i]:
            del data2['data'][i]['stacks']
        if 'effect' in data['data'][i]:
            del data2['data'][i]['effect']




    f = open('/dragontail-12.6.1/12.6.1/data/fr_FR/item.json', 'w')

    json.dump(data2, f)
    f.close()
