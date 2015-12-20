# from django import forms
#
#
# class ExerciseForm(forms.Form):
#     name = forms.CharField(label="Name:", required=True)
#     type = forms.Select()
#     time = forms.IntegerField(label="Time", required=True)
#     desc = forms.Textarea()
#     obj = forms.SelectMultiple()

    # helper = FormHelper()
    # helper.form_method = 'POST'
    # helper.form_class = 'form-horizontal'
    # helper.label_class = 'col-sm-2'
    # helper.field_class = 'col-sm-4'
    # helper.layout = Layout(
    #     Field('fullname', css_class='input-sm'),
    #     Field('card_number', css_class='input-sm'),
    #     Field('expire', css_class='input-sm'),
    #     Field('ccv', css_class='input-sm'),
    #     Field('notes', rows=3),
    #     FormActions(Submit('purchase', 'purchase', css_class='btn-primary'))
    # )

    # available_types = (('P', 'Personal'), ('T', 'Team'),)
    # available_objectives = (
    #                             ('SPD', 'Speed'),
    #                             ('STA', 'Stamina'),
    #                             ('POW', 'Power'),
    #                             ('MEN', 'Mentality'),
    #                             ('SHO', 'Shoot'),
    #                             ('ATK', 'Attack'),
    #                             ('DEF', 'Defence'),
    #                             ('DRI', 'Dribbling'),
    #                             ('PAS', 'Pass'),
    #                             ('TMW', 'Teamwork'),
    #                        )
    #
    # name = models.CharField(max_length=30, default='')
    # type = models.CharField(max_length=1, choices=available_types, default='P')
    # time = models.SmallIntegerField(default=0)  # time in minutes
    # obj = MultiSelectField(choices=available_objectives, default='')
    # desc = models.TextField(blank=True)
