from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_excel('dados_api.xlsx')
data_list = df.to_json(orient='records')


@app.route('/')
def home():
    return '<h3>TO CHECK INPUT ADD "/input" TO THE URL.</h3>'


@app.route('/input/')
def input():
    return jsonify(data_list)


app.run()
