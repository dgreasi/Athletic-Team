from django import forms



class EditAboutUsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    first_name = forms.CharField(label='First Name:', max_length=30, required=False)
    last_name = forms.CharField(label='Last Name:', max_length=30, required=False)
    position = forms.CharField(label='Position:', max_length=30, required=False)



class EditHistoryForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    info = forms.CharField(label='info:', required=False,max_length=30)

class EditTicketsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    info = forms.CharField(label='info:', required=False,max_length=30)

class EditEventsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    info = forms.CharField(label='info:', required=False,max_length=30)

class EditFacilitiesForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    info = forms.CharField(label='info:', required=False,max_length=30)

class EditSponsorshipsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    first_name = forms.CharField(label='Company:', max_length=30, required=False)
    #add photo
