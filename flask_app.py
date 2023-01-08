from flask import Flask, request, render_template

import yfinance as yf



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error/')
def error():
    return render_template('error.html')

@app.route('/result/')
def result():
    return render_template('result.html')

@app.route('/about/')
def about():
    return render_template('about.html')



@app.route('/search/', methods =["GET", "POST"])
def search():
  try:
    if request.method == "POST":

      ticker = request.form['ticker']
      symbol = request.args.get('symbol', ticker)

      quote = yf.Ticker(symbol)

      return render_template("result.html", quote=quote)
  except Exception as error:
    # Code to handle the error goes here
    return render_template("error.html", error=error)
  return render_template("result.html")

if __name__ == '__main__':
    app.run()