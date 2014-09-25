from django.shortcuts import render_to_response
from django.template.context import RequestContext
from MainApp.models import Telefonino, Persona


def telefonini(request):
    context = {}

    context['titolo_pagina'] = "Telefonini"

    telefonini_list = Telefonino.objects.all()

    context['telefonini_list'] = telefonini_list

    return render_to_response('telefonini.html', context_instance=RequestContext(request, context))



def persone(request):
    context = {}

    context['titolo_pagina'] = "Persone"

    persone_list = Persona.objects.all()

    context['persone_list'] = persone_list

    return render_to_response('persone.html', context_instance=RequestContext(request, context))



def persona(request, persona_id):
    context = {}

    p = Persona.objects.get(id=persona_id)

    context['titolo_pagina'] = "Persona: %s" % p

    context['persona'] = p

    return render_to_response('persona.html', context_instance=RequestContext(request, context))



def index(request):
    context = {}

    context['titolo_pagina'] = "Home Page"

    return render_to_response('index.html', context_instance=RequestContext(request, context))

