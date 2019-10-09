from flask import Flask, request, render_template, make_response, Markup
import flask

def fix(arg):
    if ("javascript" in arg or "java" in arg):
        return 'confirm'
    else:
        return arg

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render_welcome():
    # Route the request to the appropriate template
    return make_response(render_template('welcome.html'))

@app.route('/welcome', methods=['GET', 'POST'])
def render_welcome_again():
    # Route the request to the appropriate template
    return make_response(render_template('welcome.html'))

@app.route('/signup', methods=['GET', 'POST'])
def render_signup():
    arg = request.args.get('next')
    arg = fix(arg)
    return make_response(render_template('signup.html', next = arg))

@app.route('/confirm', methods=['GET', 'POST'])
def render_confirm():
    arg = request.args.get('next', 'welcome')
    arg = fix(arg)
    return make_response(render_template('confirm.html', next = arg))

if __name__=='__main__':
    app.run(debug=True)