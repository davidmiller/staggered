"""
staggered - Our Opal Application
"""
from opal.core import application

from staggered.episode_categories import StaggeredEpisode

class Application(application.OpalApplication):

    default_episode_category = StaggeredEpisode.display_name

    javascripts   = [
        'js/staggered/routes.js',
        'js/opal/controllers/discharge.js'
    ]
