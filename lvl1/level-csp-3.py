from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def render():
    arg = ''
    if request.method == 'GET':
        arg = request.args.get('query', '')
        arg = Markup(arg.encode("utf-8"))
        r = make_response(render_template('webpage-csp-3.html', arg = arg))
        r.headers.set("X-XSS-Protection", "0")
        r.headers['Content-Security-Policy'] = "script-src 'nonce-RiJpMcQWKQRLTKaMPjOajw'"
        return r


if __name__=='__main__':
    app.run(debug=True)
