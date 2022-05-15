from flask import Flask, render_template, url_for
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/rpgrole/stat/desc', methods=['GET'])
def get_rpgrole():
    rpgrole = requests.get('http://service2:5001/get/rpgrole').text # service 2
    stat = requests.post('http://service3:5002/post/rpgrole', data=rpgrole) # service 3
    a_str = rpgrole + ',' + stat.text # concat between rpg and stat to be passed to service 4
    desc = requests.post('http://service4:5003/post/desc', data=a_str) #service 4
    return render_template('home.html', title='Welcome', rpgrole=rpgrole, stat=stat.text, desc=desc.text)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')