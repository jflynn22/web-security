from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def render():
    arg = ''
    if request.method == 'GET':
        r = make_response(render_template('index-csp-2.html'))
        r.headers.set("X-XSS-Protection", "0")
        r.headers['Content-Security-Policy'] = "script-src 'nonce-UGTMUQb8IEZkXS4y5T6O9A'"
        return r

if __name__=='__main__':
    app.run(debug=True)
