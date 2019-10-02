from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/')
def render():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
