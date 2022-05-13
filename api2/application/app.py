from flask import Flask, Response
# from random import randint
import random

app = Flask(__name__)

@app.route('/get/rpgrole', methods=['GET'])
def get_rpgrole():
    rpgroles = ['Hero', 'Dragon Rider', 'Knight', 'Healer', 'Demon King', 'Royal Jester', 'Thief', 'Assassin', 'Mage', 'Metal Slime']
    randomnum = random.randint(0,9)
    return Response(rpgroles[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')