from flask import * 
 
app = Flask(__name__)
 
@app.route("/",methods=['POST','GET'])
@app.route("/login",methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['form-username'] != 'admin' or request.form['form-password'] != 'admin': 
            error= "sorry"
        else:
            return redirect(url_for('index'))
    return render_template('login.html',error=error)
  
@app.route("/index")
def index():
	return render_template('index.html')
 
if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=80, 
        debug=True)
