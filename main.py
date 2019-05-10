from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.config["DEBUG"]=True
app.secret_key = 'ugriwdsbcnrghewuyfsahkdvj'

def is_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

def valid_username(string):
    return (len(string) >=3 and len(string) <=20)

def is_password(pas, val):
    return (pas == val and pas != "" and len(pas) >=3)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)  
        
@app.route('/', methods = ['POST','GET'])
def index():
    error1=""
    error2=""
    error3=""

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']
        username = request.form['username']

        if not is_password(password, verify):
            error1 = "passwords don't match or are not at least 3 characters"
        if not is_email(email):
            error2 = "Please enter a valid email"
            if email == "":
                error2 = ""
        if not valid_username(username):
            error3 = "Username must be between 3 and 20 characters"

        if not (error1 + error2 + error3):
            return redirect('/welcome?username=' + username)

    return render_template('index.html', error1=error1,error2=error2,error3=error3)

if __name__ == "__main__":
    app.run()
