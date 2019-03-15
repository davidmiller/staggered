"""
staggered - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/staggered/routes.js',
        'js/opal/controllers/discharge.js'
    ]