from flask import Flask, request, render_template, make_response, Markup
import flask

current_page = 'welcome'

def fix(arg):
    print(arg)
    if ("javascript" in arg or "java" in arg):
        return 'confirm'
    else:
        return arg

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render():
    global current_page
    arg = ''
    if request.method == 'GET':
        if current_page == "signup":
            arg = request.args.get('next', '')
            arg = Markup(arg.encode("utf-8"))
            arg = fix(arg)
            r = make_response(render_template('signup.html', next = arg))
            r.headers.set("X-XSS-Protection", "0")
            current_page = 'confirm'
        elif current_page == 'confirm':
            arg = request.args.get('next', 'welcome')
            arg = Markup(arg.encode("utf-8"))
            arg = fix(arg)
            r = make_response(render_template('signup.html', next = arg))
            r = make_response(render_template('confirm.html', next = arg))
            r.headers.set("X-XSS-Protection", "0")
            current_page = 'welcome'
        else:
            r = make_response(render_template('welcome.html'))
            r.headers.set("X-XSS-Protection", "0")
            current_page = 'signup'
        return r


if __name__=='__main__':
    app.run(debug=True)