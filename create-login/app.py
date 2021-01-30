from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("login.html")
database={'angel':'123','ayush':'456','anna':'789'}



@app.route('/login',methods=['POST','GET'])
def login():
    name=request.form['username']
    pwd=request.form['password']
    if name not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name)



if __name__ == '__main__':
    app.run()