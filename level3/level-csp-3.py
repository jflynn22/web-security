from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def render():
    if request.method == 'GET':
        r = make_response(render_template('index-csp-3.html'))
        r.headers.set("X-XSS-Protection", "0")
        r.headers['Content-Security-Policy'] = "script-src 'nonce-eCemQcnSszEjp4JzKsxeMQ' 'unsafe-eval' http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
        return r


if __name__=='__main__':
    app.run(debug=True)