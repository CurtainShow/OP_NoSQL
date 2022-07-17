from flask import Flask, redirect, url_for, render_template, request
from riotwatcher import LolWatcher
import json
from function import get_user_informations
import time

# golbal variables
api_key = 'RGAPI-768271ad-868d-4f83-8a46-39dfc9bf7d53'
watcher = LolWatcher(api_key)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":

        # ! Get User Informations
        user = request.form["nm"]
        user_region = request.form["region"]

        #get_user_informations(user_region, user)

        # ! Get The Information About User After Calling API
        json_file = open('AccountInfos.json')
        data = json.load(json_file)

        # ! Parsing the dictionarry user
        user_puuid = data['puuid']
        user_profile_icon = data['profileIconId']
        user_level = data['summonerLevel']
        user_ranked = " ".join((data['tier'], data['rank']))
        user_ranked_stats = str(data['leaguePoints']) #, str("LP"), "/".join(str(data['wins']), str(data['losses']))
        user_ranked_stats_wins = data['wins']
        user_ranked_stats_losses = data['losses']


        # ! Get The Information About User Game After Calling API
        json_file_game_1 = open('AccountMatchInfos_100.json')
        data_game_1 = json.load(json_file_game_1)

        # ! Parsing the dictionarry user games
        match_type = data_game_1[10]['gameMode']

        match_duration = data_game_1[10]['gameDuration']
        ty_res = time.gmtime(match_duration)
        res = time.strftime("%M:%S",ty_res)

        result_game = ''
        user_kill = ''
        user_death = ''
        user_assists = ''
        ward = ''

        champion1 = data_game_1[0]['championName']
        champion2 = data_game_1[1]['championName']
        champion3 = data_game_1[2]['championName']
        champion4 = data_game_1[3]['championName']
        champion5 = data_game_1[4]['championName']
        champion6 = data_game_1[5]['championName']
        champion7 = data_game_1[6]['championName']
        champion8 = data_game_1[7]['championName']
        champion9 = data_game_1[8]['championName']
        champion10 = data_game_1[9]['championName']


        for user_in_match in data_game_1:
            try:
                #print(user)
                game_user_puuid = user_in_match['puuid']
                if game_user_puuid == user_puuid:
                    result_game = user_in_match['win']
                    if user_in_match['win'] == True:
                        result_game = "Victoire"
                        color = '#b8e994;'
                        color_background = "style = background-color:"
                        final = color_background + color
                        x_1 = "".join(final)
                    elif user_in_match['win'] == False:
                        result_game = "Défaite"
                        color_red = '#fab1a0 !important ;'
                        color_background_red = "style = background-color:"
                        final_red = color_background_red + color_red
                        x_1 = "".join(final_red)

                    user_kill = user_in_match['kills']
                    user_death = user_in_match['deaths']
                    user_assists = user_in_match['assists']

                    ward = user_in_match['detectorWardsPlaced']
            except KeyError:
                pass

        kda = (user_kill + user_assists) / user_death






        # ! Get The Information About User Game After Calling API
        json_file_game_2 = open('AccountMatchInfos_101.json')
        data_game_2 = json.load(json_file_game_2)

        # ! Parsing the dictionarry user games
        match_type_2 = data_game_2[10]['gameMode']

        match_duration_2 = data_game_2[10]['gameDuration']
        ty_res_2 = time.gmtime(match_duration_2)
        res_2 = time.strftime("%M:%S",ty_res_2)

        result_game_2 = ''
        user_kill_2 = ''
        user_death_2 = ''
        user_assists_2 = ''
        ward_2 = ''

        champion1_2 = data_game_2[0]['championName']
        champion2_2 = data_game_2[1]['championName']
        champion3_2 = data_game_2[2]['championName']
        champion4_2 = data_game_2[3]['championName']
        champion5_2 = data_game_2[4]['championName']
        champion6_2 = data_game_2[5]['championName']
        champion7_2 = data_game_2[6]['championName']
        champion8_2 = data_game_2[7]['championName']
        champion9_2 = data_game_2[8]['championName']
        champion10_2 = data_game_2[9]['championName']


        for user_in_match2 in data_game_2:
            try:
                #print(user)
                game_user_puuid_2 = user_in_match2['puuid']
                if game_user_puuid_2 == user_puuid:
                    result_game_2 = user_in_match2['win']
                    if user_in_match2['win'] == True:
                        result_game_2 = "Victoire"
                        color = '#b8e994;'
                        color_background = "style = background-color:"
                        final = color_background + color
                        x_2 = "".join(final)
                    elif user_in_match2['win'] == False:
                        result_game_2 = "Défaite"
                        color_red = '#fab1a0 !important ;'
                        color_background_red = "style = background-color:"
                        final_red = color_background_red + color_red
                        x_2 = "".join(final_red)

                    user_kill_2 = user_in_match2['kills']
                    user_death_2 = user_in_match2['deaths']
                    user_assists_2 = user_in_match2['assists']

                    ward_2 = user_in_match2['detectorWardsPlaced']
            except KeyError:
                pass

        kda_2 = (user_kill_2 + user_assists_2) / user_death_2





         # ! Get The Information About User Game After Calling API
        json_file_game_3 = open('AccountMatchInfos_102.json')
        data_game_3 = json.load(json_file_game_3)

        # ! Parsing the dictionarry user games
        match_type_3 = data_game_3[10]['gameMode']

        match_duration_3 = data_game_3[10]['gameDuration']
        ty_res_3 = time.gmtime(match_duration_3)
        res_3 = time.strftime("%M:%S",ty_res_3)

        result_game_3 = ''
        user_kill_3 = ''
        user_death_3 = ''
        user_assists_3 = ''
        ward_3 = ''
        x_3=''

        champion1_3 = data_game_3[0]['championName']
        champion2_3 = data_game_3[1]['championName']
        champion3_3 = data_game_3[2]['championName']
        champion4_3 = data_game_3[3]['championName']
        champion5_3 = data_game_3[4]['championName']
        champion6_3 = data_game_3[5]['championName']
        champion7_3 = data_game_3[6]['championName']
        champion8_3 = data_game_3[7]['championName']
        champion9_3 = data_game_3[8]['championName']
        champion10_3 = data_game_3[9]['championName']


        for user_in_match3 in data_game_3:
            try:
                #print(user)
                game_user_puuid_3 = user_in_match3['puuid']
                if game_user_puuid_3 == user_puuid:
                    result_game_3 = user_in_match3['win']
                    if user_in_match3['win'] == True:
                        result_game_3 = "Victoire"
                        color = '#b8e994;'
                        color_background = "style = background-color:"
                        final = color_background + color
                        x_3 = "".join(final)
                    elif user_in_match3['win'] == False:
                        result_game_3 = "Défaite"
                        color_red = '#fab1a0 !important ;'
                        color_background_red = "style = background-color:"
                        final_red = color_background_red + color_red
                        x_3 = "".join(final_red)

                    user_kill_3 = user_in_match3['kills']
                    user_death_3 = user_in_match3['deaths']
                    user_assists_3 = user_in_match3['assists']

                    ward_3 = user_in_match3['detectorWardsPlaced']

            except KeyError:
                pass

        kda_3 = (user_kill_3 + user_assists_3) / user_death_3

    

        return render_template("user.html", 
            user=user, 
            region=user_region, 
            puid=user_puuid, 
            profil_icon = user_profile_icon, 
            user_level = user_level, 
            user_ranked = user_ranked, 
            user_ranked_stats= user_ranked_stats, 
            user_ranked_stats_wins=user_ranked_stats_wins, 
            user_ranked_stats_losses=user_ranked_stats_losses,

            match_type=match_type,
            match_duration=res,
            result_game=result_game,
            user_kill=user_kill,
            user_death=user_death,
            user_assists=user_assists,
            kda=kda,
            ward=ward,
            champion1=champion1,
            champion2=champion2,
            champion3=champion3,
            champion4=champion4,
            champion5=champion5,
            champion6=champion6,
            champion7=champion7,
            champion8=champion8,
            champion9=champion9,
            champion10=champion10,

            match_type_2=match_type_2,
            match_duration_2=res_2,
            result_game_2=result_game_2,
            user_kill_2=user_kill_2,
            user_death_2=user_death_2,
            user_assists_2=user_assists_2,
            kda_2=kda_2,
            ward_2=ward_2,
            champion1_2=champion1_2,
            champion2_2=champion2_2,
            champion3_2=champion3_2,
            champion4_2=champion4_2,
            champion5_2=champion5_2,
            champion6_2=champion6_2,
            champion7_2=champion7_2,
            champion8_2=champion8_2,
            champion9_2=champion9_2,
            champion10_2=champion10_2,

            match_type_3=match_type_3,
            match_duration_3=res_3,
            result_game_3=result_game_3,
            user_kill_3=user_kill_3,
            user_death_3=user_death_3,
            user_assists_3=user_assists_3,
            kda_3=kda_3,
            ward_3=ward_3,
            champion1_3=champion1_3,
            champion2_3=champion2_3,
            champion3_3=champion3_3,
            champion4_3=champion4_3,
            champion5_3=champion5_3,
            champion6_3=champion6_3,
            champion7_3=champion7_3,
            champion8_3=champion8_3,
            champion9_3=champion9_3,
            champion10_3=champion10_3,

            x_1 = x_1,
            x_2=x_2,
            x_3=x_3
        )
        #return redirect(url_for("user", usr=user, region=user_region, puid = user_puid))
    else:
        return render_template("login.html")

@app.route("/<region>/<usr>/<puid>") #> et <>
def user(usr, region, puid):
    return f"<h1>Name : {usr} <br> Region : {region} <br> Puid : {puid}</h1>"


if __name__ == "__main__":
    app.run(debug=True)