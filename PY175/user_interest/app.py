from flask import Flask, render_template, url_for, redirect, g
import yaml

app = Flask(__name__)

@app.before_request
def load_user_data():
    with open('users.yaml', 'r') as f:
        user_interest = yaml.safe_load(f)
    g.contents = user_interest 

@app.route('/')
def index():
    return redirect(url_for('users'))

@app.route('/users')
def users():
    users = g.contents.keys()
    return render_template('users.html', users = users, 
                                        rem_users = users,
                                        data_summary = data_summary())

@app.template_filter('display_interest')
def display_interest(interest_list):
    if not interest_list:
        return "Nothing to see here!!"
    return ', '.join(interest_list) + '.'

@app.route('/<user_name>')
def user(user_name):
    user_data = g.contents[user_name]
    rem_users = [user for user in g.contents.keys() if user != user_name]
    return render_template(
        'user.html',
        user_name = user_name,
        user_data = user_data,
        rem_users = rem_users,
        data_summary = data_summary() 
    )

def data_summary():
    user_count = len(g.contents)
    interest_cnt = len([interest for user in g.contents.values() 
                for interest in user['interests']])
    return (user_count, interest_cnt)

if __name__ == '__main__':
    app.run(port = 5003, debug = True)

