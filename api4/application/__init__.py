# it was said
from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/post/desc', methods=['POST'])
def post_desc():
    a_str = request.data.decode('utf-8')
    rpg_plus_stat = a_str.split(",")
    if rpg_plus_stat[0] == 'Hero' and rpg_plus_stat[1] == 'HP: 1200 MP: 500':
        desc = 'Strong and versatile skillset, tasked with slaying the Demon King. Special Trait: Wielder of excalibur, the only sword that can harm the Demon King.'
    elif rpg_plus_stat[0] == 'Dragon Rider' and rpg_plus_stat[1] == 'HP: 1500 MP: 200':
        desc = 'Raised by dragons, you are the right hand man of the Hero. Special Trait: Able to communicate with Dragons, Dragon Burst: Brief transformation into a dragon boosting stats. HP --> 2000 MP --> 500.'
    elif rpg_plus_stat[0] == 'Knight' and rpg_plus_stat[1] == 'HP: 2000 MP: 100':
        desc = 'Born from nobility, you resent the Hero as you think he stole your true role as the Hero. Special Trait: Super armor on heavy attacks.'
    elif rpg_plus_stat[0] == 'Healer' and rpg_plus_stat[1] == 'HP: 600 MP: 1000':
        desc = 'Caring and Supportive, you support the team of the Hero with healing and stat boosts. Special Trait: Any allies in a 10 meter radius of you recivies regeneration of 3 percent health per second. Special Move: Guardian Touch: All allies have their stats boosted by 50%.'
    elif rpg_plus_stat[0] == 'Royal Jester' and rpg_plus_stat[1] == 'HP: 100 MP: 1':
        desc = 'You have no special role, your job is simply to ammuse the royal king and thus you were exiled from the castle and you joined the party of the Hero. Special Move: Laugh of the Jester, if you make your enemies laugh they turn to stone.'
    elif rpg_plus_stat[0] == 'Thief' and rpg_plus_stat[1] == 'HP: 800 MP: 250':
        desc = 'Quick and nimble, your job is to steal from the caravan of the Hero. No special traits.'
    elif rpg_plus_stat[0] == 'Assassin' and rpg_plus_stat[1] == 'HP: 1000 MP: 300':
        desc = 'Silent and deadly, your role is to assassinate the royal king and other key figures you are employed to elimate. Special Trait 1: Invisibility, grants you to not be seen for a brief period of time. Special Trait 2: Slient footsteps.'
    elif rpg_plus_stat[0] == 'Mage' and rpg_plus_stat[1] == 'HP: 300 MP: 3000':
        desc = 'A strong intellect but a frail body, you have mastered the various disciplines of magic. Special Move: Magic Burst, expend all MP in an Area Of Effect Attack, attack power scales with remaining MP i.e. 100% will give more damage than 50% MP.'
    elif rpg_plus_stat[0] == 'Metal Slime' and rpg_plus_stat[1] == 'HP: 5000 MP: 0':
        desc = 'UNLUCKY, your role is simply to provide the Hero and his party with bonus EXP that is if they can hit you! Special Traits: 80,000 EXP, extremely high evasion.'
    else:
        desc =  desc = 'Born from Malice and Evil, your task is to kill the Hero and every other human you see. Special Trait: You cannot be harmed at all unless you are struck by excalibur, in which case you take twice the damage.'
    return Response(desc, mimetype='text/plain')   

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')
