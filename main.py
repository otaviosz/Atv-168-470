from flask import Flask
app = Flask('app')

@app.route('/')
def mundo():
  return '<h1>Olá Mundo!</h1>'


  
@app.route('/unifran/')
def unifran():
  return '<h2>Universidade de Franca</h2>'
app.run(host='0.0.0.0', port=8080)