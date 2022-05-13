from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/rpgrole', methods=['POST'])
def post_rpgrole():
    rpgrole_text = request.data.decode('utf-8')
    if rpgrole_text == 'Hero':
        stat = 'HP: 1200 MP: 500'
    elif rpgrole_text == 'Dragon Rider':
        stat = 'HP: 1500 MP: 200'
    elif rpgrole_text == 'Knight':
        stat = 'HP: 2000 MP: 100'
    elif rpgrole_text == 'Demon King':
        stat = 'HP: 10,000 MP: 5000'
    elif rpgrole_text == 'Royal Jester':
        stat = 'HP: 100 MP: 1'
    elif rpgrole_text == 'Thief':
        stat = 'HP: 800 MP: 250'
    elif rpgrole_text == 'Assassin':
        stat = 'HP: 1000 MP: 300'
    elif rpgrole_text == 'Mage':
        stat = 'HP: 300 MP: 3000'
    elif rpgrole_text == 'Metal Slime':
        stat = 'HP: 5000 MP: 0'    
    else:
        stat = 'HP: 600 MP: 1000'
    return Response(stat, mimetype='text/plain')   

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')


    # rpgrole = requests.get('http://service3:5001/get/rpgroles')
    # fantasyjob_text = fantasyjob.text
    # if fantasyjob_text == 'Hero':
    #     stats = 'HP: 1200 \n MP: 500'
    # elif fantasyjob_text == 'Dragon Rider':
    #     stats = 'HP: 1500 \n MP: 200'
    # elif fantasyjob_text == 'Knight':
    #     stats = 'HP: 2000 \n MP: 100'
    # else:
    #     stats = 'HP: 600 \n MP: 1000'
    # return render_template('home1.html', title='Roles', fantasyjob=fantasyjob_text, stats=stats)