import os
import urllib

import jinja2
import webapp2
#import htmlmin


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'user': 'This is a user :)'
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)