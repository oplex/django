
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



