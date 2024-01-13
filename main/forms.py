from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # check = forms.BooleanField(required=False)


class CreateNewNote(forms.Form):
    notetitle = forms.CharField(label="Note Title", max_length=200)
    notetext = forms.CharField(label="Enter Note", max_length=1000, required=False)
