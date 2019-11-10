from django import forms
from .models import Scenario, Plugin

class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ( 'name', 'summary', 'description', 'scenario',
                   'require', 'author', )

class PluginForm(forms.ModelForm):
    class Meta:
        model = Plugin
        fields = ( 'name', 'summary', 'description', 'plugin',
                   'target', 'author', )

# Ends here.
