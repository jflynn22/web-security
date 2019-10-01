from flask import Flask, request, render_template, make_response, Markup
import flask
# class MainPage(webapp.RequestHandler):
 
#   def render_template(self, filename, context={}):
#     path = os.path.join(os.path.dirname(__file__), filename)
#     self.response.out.write(template.render(path, context))
 
#   def get(self):
#     self.render_template('index.html')
 
# application = webapp.WSGIApplication([ ('.*', MainPage) ], debug=False)

app = Flask(__name__)
@app.route('/')
def render():
    # arg = ''
    # if request.method == 'GET':
    #     arg = request.args.get('query', '')
    #     arg = Markup(arg.encode("utf-8"))
    #     print(arg)
    #     r = make_response(render_template('webpage.html', arg = arg))
    #     r.headers.set("X-XSS-Protection", "0")
    #     return r
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
