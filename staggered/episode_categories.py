from opal.core import episodes

class StaggeredEpisode(episodes.EpisodeCategory):

    display_name    = 'Staggered Episode'
    detail_template = 'detail/staggered.html'

    stages = [
        'future',
        'present',
        'past'
    ]
