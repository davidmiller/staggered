"""
Plugin API
"""
from opal.core import plugins

class Plugin(plugins.OpalPlugin):
    head_extra = [
        'staggered_extra_head.html'
    ]
    stylesheets = [
        'css/staggered.css'
    ]
