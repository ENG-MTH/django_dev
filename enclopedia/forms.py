from django import forms

class TaskForm(forms.Form):
    name= forms.CharField(
        label='Name',
        required= True
    )