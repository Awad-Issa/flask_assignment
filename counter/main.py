from flask import Flask, session, render_template,redirect
app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def count():
    if 'visits' in session :
       session['visits'] += 1 
    else:
       session['visits'] =1
    return render_template('index.html' , visits = session['visits']) 

@app.route('/destroy_session')
def destroy():
        session.clear()
        return redirect('/' , )

if __name__ == "__main__":
    app.run(debug=True)
  