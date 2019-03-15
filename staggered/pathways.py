import random

from opal.core.pathway import PagePathway, RedirectsToPatientMixin, Step

from staggered.models import Demographics

class AddPatient(RedirectsToPatientMixin, PagePathway):
    display_name = 'Add Patient'
    slug         = 'add-patient'
    steps        = [
        Step(
            model=Demographics
        )
    ]

    def save(self, data, **kwargs):
        """
        We're ignoring identifiers, so handle that.
        Set the first stage implicitly.
        """
        data['demographics'][0]['hospital_number'] = str(random.randint(100000, 999999))
        patient, episode = super().save(data, **kwargs)
        episode.set_stage(episode.category.get_stages()[0], kwargs['user'], {})
        episode.save()
        return patient, episode


class MoveForwardPathway(RedirectsToPatientMixin, PagePathway):
    display_name       = 'Move Forwards'
    slug               = 'move-forwards'
    finish_button_text = 'Onwards!'
    finish_button_icon = 'fa fa-step-forward'
    steps        = [
        Step(
            display_name="The API requiring this argument is thoroguly obnoxious",
            template="move_forwards_step.html"
        )
    ]

    def save(self, data, user=None, patient=None, episode=None):
        stages = episode.category.get_stages()
        current_stage_index = stages.index(episode.stage)
        if current_stage_index +1 == len(stages):
            raise ValueError('WHAT ?')
        episode.set_stage(stages[current_stage_index + 1], user, {})
        episode.save()
        return patient, episode


class MoveBackardPathway(RedirectsToPatientMixin, PagePathway):
    display_name       = 'Move Back'
    slug               = 'move-backwards'
    finish_button_text = 'Reverse!'
    finish_button_icon = 'fa fa-step-backward'
    steps        = [
        Step(
            display_name="The API requiring this argument is thoroguly obnoxious",
            template="move_backwards_step.html"
        )
    ]

    def save(self, data, user=None, patient=None, episode=None):
        stages = episode.category.get_stages()
        current_stage_index = stages.index(episode.stage)
        if current_stage_index -1 < 0:
            raise ValueError('WHAT ?')
        episode.set_stage(stages[current_stage_index - 1], user, {})
        episode.save()
        return patient, episode
