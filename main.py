from flask import Flask
app = Flask('app')

@app.route('/')
def mundo():
  return '<h1>Olá Mundo!</h1>'


  
@app.route('/unifran/')
def unifran():
  return '<h2>Universidade de Franca</h2>'

if __name__=='__main__':
    app.run(host='0.0.0.0)