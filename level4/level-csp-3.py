from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render():
    arg = ''
    if request.method == 'GET':
        arg = request.args.get('timer', '')
        if (arg == ''):
            r = make_response(render_template('index.html'))
            r.headers["Content-Security-Policy"] = "script-src 'nonce-LHkHnVoKDfNINMT5iWQtpw' 'nonce-tyVzu4RLVwqpsJ3Nw34dpA'"
            r.headers.set("X-XSS-Protection", "0")
        else:
            print(arg)
            arg = Markup(arg.encode('utf-8'))
            r = make_response(render_template('timer-csp-3.html', timer = arg))
            r.headers["Content-Security-Policy"] = "script-src 'nonce-LHkHnVoKDfNINMT5iWQtpw' 'nonce-tyVzu4RLVwqpsJ3Nw34dpA'"
            r.headers.set("X-XSS-Protection", "0")
        return r


if __name__=='__main__':
    app.run(debug=True)
