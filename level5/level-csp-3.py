from flask import Flask, request, render_template, make_response, Markup
import flask

current_page = 'welcome'

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render():
    global current_page
    arg = ''
    if request.method == 'GET':
        if current_page == "signup":
            arg = request.args.get('next', '')
            print(arg)
            r = make_response(render_template('signup.html', next = arg))
            r.headers.set("X-XSS-Protection", "0")
            current_page = 'confirm'
        elif current_page == 'confirm':
            arg = request.args.get('next', 'welcome')
            print(arg)
            r = make_response(render_template('confirm-csp-3.html', next = arg))
            r.headers.set("X-XSS-Protection", "0")
            current_page = 'welcome'
        else:
            r = make_response(render_template('welcome.html'))
            r.headers.set("X-XSS-Protection", "0")
            current_page = 'signup'
        r.headers['Content-Security-Policy'] = "script-src 'nonce-ycIG83BS8AZX6e3RXTwOUw'"
        return r


if __name__=='__main__':
    app.run(debug=True)