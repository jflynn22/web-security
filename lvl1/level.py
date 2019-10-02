from flask import Flask, request, render_template, make_response, Markup
import flask

'''
This is the fix
'''
def fix(input_string):
    for letter in input_string:
        if letter == '<':
            input_string = input_string.replace(letter, '&lt')
        elif letter == '>':
            input_string = input_string.replace(letter, '&rt')
    return input_string

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render():
    arg = ''
    if request.method == 'GET':
        arg = request.args.get('query', '')
        arg = Markup(arg.encode("utf-8"))
        arg = fix(arg)
        r = make_response(render_template('webpage.html', arg = arg))
        r.headers.set("X-XSS-Protection", "0")
        return r


if __name__=='__main__':
    app.run(debug=True)
