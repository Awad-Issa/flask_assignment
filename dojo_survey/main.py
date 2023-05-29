from flask import Flask, render_template, request
app  = Flask(__name__)
@app.route('/')
def regPage():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    city = request.form['city']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('index2.html', name=name,city=city,language=language,comment=comment)





if __name__=='__main__':
    app.run(debug = True)

