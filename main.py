import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        index_template = the_jinja_env.get_template("templates/index.html")
        self.response.write(index_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
