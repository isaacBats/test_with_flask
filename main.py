from flask import Flask, request

app = Flask(__name__)


# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
def index():
    return 'Method used: %s' % request.method

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'
# @app.route('/')
# def index():
#     return 'This is the home page!'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good!!</h2>'

@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hey there %s</h2>' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h2>Posy ID id %s</h2>' % post_id

if __name__ == '__main__':
    app.run(debug=True)
