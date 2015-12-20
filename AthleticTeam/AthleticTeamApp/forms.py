from datetimewidget.widgets import DateWidget, TimeWidget
from django import forms

from AthleticTeamApp.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['date', 'start', 'end', 'location', 'exercises', 'team_plays', 'team']
        widgets = {
            'date': DateWidget(usel10n=True, bootstrap_version=3),
            'start': TimeWidget(usel10n=True, bootstrap_version=3),
            'end': TimeWidget(usel10n=True, bootstrap_version=3),
        }
