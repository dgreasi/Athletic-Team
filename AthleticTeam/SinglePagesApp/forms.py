from django import forms


class EditContactUsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    email = forms.EmailField(label='Email:', required=False)
    phone = forms.CharField(label='Phone:', max_length=30, required=False)
    mobile_phone = forms.CharField(label='Mobile Phone:', max_length=30, required=False)

class EditAboutUsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    first_name = forms.CharField(label='First Name:', max_length=30, required=False)
    last_name = forms.CharField(label='Last Name:', max_length=30, required=False)
    position = forms.CharField(label='Position:', max_length=30, required=False)


class EditSponsorshipsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    first_name = forms.CharField(label='Company:', max_length=30, required=False)
    #add photo
