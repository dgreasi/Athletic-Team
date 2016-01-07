from datetimewidget.widgets import DateWidget, TimeWidget
from django import forms
from EventsApp.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'start', 'end', 'location', 'name','event_content','ACTIVATE']
        widgets = {
            'date': DateWidget(usel10n=True, bootstrap_version=3),
            'start': TimeWidget(usel10n=True, bootstrap_version=3),
            'end': TimeWidget(usel10n=True, bootstrap_version=3),
        }