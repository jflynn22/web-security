#   def get(self):
#     # Disable the reflected XSS filter for demonstration purposes
#     self.response.headers.add_header("X-XSS-Protection", "0")
 
#     # Route the request to the appropriate template
#     if "signup" in self.request.path:
#       self.render_template('signup.html', 
#         {'next': self.request.get('next')})
#     elif "confirm" in self.request.path:
#       self.render_template('confirm.html', 
#         {'next': self.request.get('next', 'welcome')})
#     else:
#       self.render_template('welcome.html', {})
     
#     return
from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render():
    arg = ''
    if request.method == 'GET':
        if "signup" in request.full_path:
            arg = request.args.get('next', '')
            arg = Markup(arg.encode("utf-8"))
            r = make_response(render_template('signup.html', next = arg))
            r.headers.set("X-XSS-Protection", "0")
        elif "confirm" in request.full_path:
            arg = request.args.get('next', 'welcome')
            arg = Markup(arg.encode("utf-8"))
            r = make_response(render_template('confirm.html', next = arg))
            r.headers.set("X-XSS-Protection", "0")
        else:
            r = make_response(render_template('welcome.html'))
            r.headers.set("X-XSS-Protection", "0")
        return r


if __name__=='__main__':
    app.run(debug=True)