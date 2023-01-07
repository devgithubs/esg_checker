from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import yfinance as yf



app = Flask(__name__)

msft = yf.Ticker("MSFT")
# show sustainability


df = msft.sustainability

# pd.DataFrame({'A': [0, 1, 2, 3, 4],
#                    'B': [5, 6, 7, 8, 9],
#                    'C': ['a', 'b', 'c--', 'd', 'e']})


@app.route('/', methods=("POST", "GET"))
def index():

    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)



if __name__ == '__main__':
    app.run(debug=True)