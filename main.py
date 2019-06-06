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
    "You matter.",
    "Be a voice not an echo.",
    "You are the only one who can limit your greatness.",
    "Make the most of yourself... for that is all there is of you.",
    "It takes courage to grow up and become who you really are.",
    "The two most important days in your life are the day you are born and the day you find out why.",
    "It is never too late to be what you might have been.",
    "Whatever you are, be a good one.",
    "The true success is the person who invented himself.",
    "Give up on being perfect and start working on becoming yourself.",
    "Do something today that your future self will thank you for.",
    "Whatever you do, do with all your might.",
    "You were put on this Earth to achieve your greatest self, to live out your purpose, and to do it courageously.",
    "Definiteness of purpose is the starting point of all achievement.",
    "All our dreams can come true, if we have the courage to pursue them.",
    "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine.",
    "Opportunities don't happen. You create them.",
    "Excuses will always be there for you. Opportunity won't.",
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
