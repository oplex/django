from django.utils.translation import activate
from django.shortcuts import redirect
from django.conf import settings
from django.shortcuts import render




from django.utils.translation import activate
from django.shortcuts import redirect
from django.conf import settings

def set_language(request):
    language = request.POST.get('language')
    print(f"Selected language: {language}")  # Debugging line
    
    if language in dict(settings.LANGUAGES):
        activate(language)
        print(f"Language activated: {language}")  # Debugging line
        return redirect(f'/{language}/test')  # Make sure to redirect to the correct language-specific URL
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


from django.shortcuts import render

import logging
import traceback
from django.http import HttpResponse

logger = logging.getLogger(__name__)

from django.utils.translation import get_language
from django.shortcuts import render

def my_view(request):
    context = {
        'greeting': _("Welcome to our multilingual site"),
        'LANGUAGE_CODE': get_language(),  # Explicitly pass LANGUAGE_CODE
    }
    return render(request, 'test.html', context)



