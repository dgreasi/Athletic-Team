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


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"


