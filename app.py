from flask import render_template, Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    # get data from database or mqtt whatever...
    title = 'Hi 我是折線圖'
    labels = list(range(1, 20))
    data = [random.randint(-100, 100) for x in labels]

    return render_template('index.html', data={'title': title, 'data': data, 'labels': labels} )

@app.route('/get_new_data/')
def get_new_data():
    # simulate incremental data for ajax call...
    nwe_data = {'value': random.randint(-100, 100)}
    return jsonify(nwe_data)

if __name__ == '__main__':
    app.run()
