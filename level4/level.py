 
#   def get(self):
#     # Disable the reflected XSS filter for demonstration purposes
#     self.response.headers.add_header("X-XSS-Protection", "0")
 
#     if not self.request.get('timer'):
#       # Show main timer page
#       self.render_template('index.html')
#     else:
#       # Show the results page
#       timer= self.request.get('timer', 0)
#       self.render_template('timer.html', { 'timer' : timer })
     
#     return
 
# application = webapp.WSGIApplication([ ('.*', MainPage), ], debug=False)

from flask import Flask, request, render_template, make_response, Markup
import flask

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def render():
    arg = ''
    if request.method == 'GET':
        arg = request.args.get('timer', '')
        arg = Markup(arg.encode("utf-8"))
        print(arg)
        if (arg == ''):
            r = make_response(render_template('index.html'))
            r.headers.set("X-XSS-Protection", "0")
        else:
            r = make_response(render_template('timer.html', timer = arg))
            r.headers.set("X-XSS-Protection", "0")
            # timer= self.request.get('timer', 0)
        return r


if __name__=='__main__':
    app.run(debug=True)
