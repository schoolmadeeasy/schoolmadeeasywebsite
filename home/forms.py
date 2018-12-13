from django import forms
from django.forms import ModelForm
from .models import Assignment, AssignmentImage


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        exclude = ('timestamp',)

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.widgets.TextInput(attrs={'placeholder': 'Email',
                                                                     'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['school_name'].widget = forms.widgets.TextInput(attrs={'placeholder': 'School Name',
                                                                           'class': 'form-control'})
        self.fields['class_name'].widget = forms.widgets.TextInput(attrs={'placeholder': 'Class Name',
                                                                           'class': 'form-control'})
        self.fields['title'].widget = forms.widgets.TextInput(attrs={'placeholder': 'Assignment Title',
                                                                     'class': 'form-control'})
        self.fields['notes'].widget = forms.widgets.Textarea(attrs={'placeholder': 'Extra Notes',
                                                                    'class': 'form-control'})


class ImageForm(ModelForm):
    class Meta:
        model = AssignmentImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget = forms.widgets.FileInput(attrs={'class': 'custom-file-input'})
        self.fields['image'].label = None


