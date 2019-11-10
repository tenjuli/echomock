from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import ScenarioForm, PluginForm
from .models import Scenario, Plugin

def index(request):
    if request.method == 'POST':
        form = ScenarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ecomockapp/')

    form = ScenarioForm()
    obj = Scenario.objects.all()

    latest_scenario_list = Scenario.objects.order_by ('-release_date')[:5]
    return render(request, 'ecomockapp/index.html', {
        'form': form,
        'obj': obj,
        'latest_scenario_list': latest_scenario_list
    })

# from django.urls import reverse
# from django.views import generic

# class IndexView(generic.ListView):
#     template_name = 'ecomockapp/index.html'
#     context_object_name = 'latest_scenario_list'

#     # def get_queryset(self):
#     #     """Return the last five published scenarios."""
#     #     return Scenario.objects.order_by('-release_date')[:5]

#     # def index(request):
#     def get_queryset(self, request):
#         if request.method == 'POST':
#             form = ScenarioForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect('/ecomockapp/')

#         form = ScenarioForm()
#         obj = Scenario.objects.all()

#         latest_scenario_list = Scenario.objects.order_by ('-release_date')[:5]
#         return render(request, 'ecomockapp/index.html', {
#             'form': form,
#             'obj': obj,
#             'latest_scenario_list': latest_scenario_list
#     })

def plugin(request):
    if request.method == 'POST':
        form = PluginForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ecomockapp/plugin')

    form = PluginForm()
    obj = Plugin.objects.all()

    latest_plugin_list = Plugin.objects.order_by ('-release_date')[:5]
    return render(request, 'ecomockapp/plugin.html', {
        'form': form,
        'obj': obj,
        'latest_plugin_list': latest_plugin_list
    })

# Ends here.
