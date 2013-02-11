# Base Handler to be imported by all other web handlers
# Provides render functions for template use
# Provides write function for easy writing to screen
# Create during Udacity.com Web App Course

import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.response.out.write(self.render_str(template, **kw))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

