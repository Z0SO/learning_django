from django import forms


class Create_new_task(forms.Form):
    title = forms.CharField(label='Titulo de Tarea', max_length=200)
    description = forms.CharField(label='Text Area', widget=forms.Textarea)
