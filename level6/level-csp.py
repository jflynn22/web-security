from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/')
def render():
    r = make_response(render_template('index-csp.html'))
    r.headers["Content-Security-Policy"] = "script-src 'self'"
    r.headers.set("X-XSS-Protection", "0")
    return r


if __name__=='__main__':
    app.run(debug=True)
