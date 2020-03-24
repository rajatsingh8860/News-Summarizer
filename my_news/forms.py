from django.forms import ModelForm
from .models import Entry,Entry_sport

class EntryForm(ModelForm):
    class Meta:
        model=Entry
        fields=('text',)



    '''def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})'''

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['text'].widget.attrs['cols'] = 130
        self.fields['text'].widget.attrs['rows'] = 20

class EntryForm_sport(ModelForm):
    class Meta:
        model=Entry_sport
        fields=('text_sport',)  

    def __init__(self, *args, **kwargs):
        super(EntryForm_sport, self).__init__(*args, **kwargs) # Call to ModelForm_sport constructor
        self.fields['text_sport'].widget.attrs['cols'] = 130
        self.fields['text_sport'].widget.attrs['rows'] = 20               