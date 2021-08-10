from django import forms


class PersonalityFactors(forms.Form):
    p_factors = forms.CharField(label="فاکتور های شخصیت شما:", max_length=4, min_length=4,
                                widget=forms.TextInput(attrs={'placeholder': 'INTJ'}))