from django import forms

class MoradorForm(forms.ModelForms):
    class Meta:
        model = Morador
        fields = '__all__'