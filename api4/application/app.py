from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/post/desc', methods=['POST'])
def post_desc():
    a_str = request.data.decode('utf-8')
    rpg_plus_stat = a_str.split(",")
    if rpg_plus_stat[0] == 'Hero' and rpg_plus_stat[1] == 'HP: 1200 MP: 500':
        desc = 'Magic and Physical damage role'
    elif rpg_plus_stat[0] == 'Dragon Rider' and rpg_plus_stat[1] == 'HP: 1500 MP: 200':
        desc = 'Flying and Damage role'
    elif rpg_plus_stat[0] == 'Knight' and rpg_plus_stat[1] == 'HP: 2000 MP: 100':
        desc = 'Tank and Damage role'
    elif rpg_plus_stat[0] == 'Demon King' and rpg_plus_stat[1] == 'HP: 10,000 MP: 5000':
        desc = 'DK placeholdertxt'
    elif rpg_plus_stat[0] == 'Royal Jester' and rpg_plus_stat[1] == 'HP: 100 MP: 1':
        desc = 'RJ placeholertxt'
    elif rpg_plus_stat[0] == 'Thief' and rpg_plus_stat[1] == 'HP: 800 MP: 250':
        desc = 'T placeholdertxt'
    elif rpg_plus_stat[0] == 'Assassin' and rpg_plus_stat[1] == 'HP: 1000 MP: 300':
        desc = 'A placeholdertxt'
    elif rpg_plus_stat[0] == 'Mage' and rpg_plus_stat[1] == 'HP: 300 MP: 3000':
        desc = 'M placeholdertxt'
    elif rpg_plus_stat[0] == 'Metal Slime' and rpg_plus_stat[1] == 'HP: 5000 MP: 0':
        desc = 'MS placeholdertxt'
    else:
        desc = 'Support and Healer role'
    return Response(desc, mimetype='text/plain')   

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')