from django import forms
from .models import Test, test_type


class TestForm(forms.ModelForm):

    test_type = forms.ChoiceField(choices=test_type, required=False)


    class Meta:
        model = Test
        fields = ('test_type', )

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-sm'