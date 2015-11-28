from django import forms


class EditContactUsForm(forms.Form):
    visible = forms.ChoiceField(label='Visible:', choices=(('Visible', 'Visible'), ('', 'Hidden')), required=False)
    email = forms.EmailField(label='Email:', required=False)
    phone = forms.CharField(label='Phone:', max_length=30, required=False)
    mobile_phone = forms.CharField(label='Mobile Phone:', max_length=30, required=False)

