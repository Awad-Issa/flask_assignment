from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo' 

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num,word):
    result = word*num
    return result    


if __name__ == '__main__':  
    app.run()



    