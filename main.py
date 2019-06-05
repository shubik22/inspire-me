import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

QUOTES = [
    "Smile, it looks good on you.",
    "Find what makes you happy, and do more of that.",
]

def get_quote():
    return random.choice(QUOTES)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        index_template = the_jinja_env.get_template("templates/index.html")
        self.response.write(index_template.render(message=get_quote()))

class QuotePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write(get_quote())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/get-quote', QuotePage),
], debug=True)
