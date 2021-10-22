from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super secret key. none shall pass'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1

    return render_template("index.html", count = session['count'])

@app.route('/destroy_session', methods=['POST'])
def destroy():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
