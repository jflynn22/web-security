from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render_welcome():
    # Route the request to the appropriate template
    r = make_response(render_template('welcome.html'))
    r.headers['Content-Security-Policy'] = "script-src 'self' http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
    return r

@app.route('/welcome', methods=['GET', 'POST'])
def render_welcome_again():
    # Route the request to the appropriate template
    r = make_response(render_template('welcome.html'))
    r.headers['Content-Security-Policy'] = "script-src 'self' http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
    return r

@app.route('/signup', methods=['GET', 'POST'])
def render_signup():
    arg = request.args.get('next')
    r = make_response(render_template('signup.html', next = arg))
    r.headers['Content-Security-Policy'] = "script-src 'self' http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
    return r

@app.route('/confirm', methods=['GET', 'POST'])
def render_confirm():
    arg = request.args.get('next', 'welcome')
    r = make_response(render_template('confirm-csp.html', next = arg))
    r.headers['Content-Security-Policy'] = "script-src 'self' http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
    return r

if __name__=='__main__':
    app.run(debug=True)