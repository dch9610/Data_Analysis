from flask import Flask, render_template, request
from db import *

app = Flask(__name__)

@app.route('/')
def home():    
    return '임시 홈페이지'

@app.route('/busancast')
def busan():
    curPage = 1 if not request.args.get('pageNo')  else int(request.args.get('pageNo'))
    amt     = 30 if not request.args.get('amt')  else int(request.args.get('amt'))
    rows = db_selectcastList()
    return render_template('busancast.html',  busancasts = rows)

if __name__ == '__main__': 
    app.run(debug=True)