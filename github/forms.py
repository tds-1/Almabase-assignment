from django import forms

class searchForm(forms.Form):
    organisation = forms.CharField(label='Enter organisation name',\
        widget=forms.TextInput(attrs={'placeholder': 'Organisation'}), max_length = 100)
    n = forms.IntegerField(label = 'n',\
        widget=forms.TextInput(attrs={'placeholder': 'Enter N'}))
    m = forms.IntegerField(label = 'm',\
        widget=forms.TextInput(attrs={'placeholder': 'Enter M'}))
    def __init__(self, *args, **kwargs):
        super(searchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
