from .models import Perfil
from social.pipeline.partial import partial
from django.shortcuts import redirect

@partial
def fill_profile(strategy, details, user=None, is_new=False, *args, **kwargs):
    try:
        if user and user.perfil:
            return
    except:
        strategy.session_set('user_id', user.id)
        return redirect('fill_profile')
