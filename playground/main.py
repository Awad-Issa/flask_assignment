from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def paly():
    return render_template('index.html')

@app.route('/play/<x>')
def playx(x):
    return render_template('index2.html', repeat=int(x) )

@app.route('/play/<x>/<color>')
def color(x,color):
    return render_template('index3.html', repeat = int(x) , color = color )

if __name__== "__main__":
    app.run(debug=True)













































