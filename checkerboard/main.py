from flask import Flask, render_template
app = Flask(__name__)  


@app.route('/')        
def mainchekboard():
    return render_template('index.html')

@app.route('/4') 
def halfchekboard():
    return render_template('index2.html')

@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
def checkerboard(x=8, y=8):
    return render_template('index3.html', rows=x, cols=y)

if __name__=="__main__":  
    app.run(debug=True)   

