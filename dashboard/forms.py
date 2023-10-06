
from django import forms
from django.core.exceptions import ValidationError
from .models import ChildInfo
from datetime import date


class ChildInfoForm(forms.ModelForm):
    class Meta:
        model = ChildInfo
        fields = ['child_name', 'birth_date', 'birth_month', 'birth_year', 'blood_group']

    def clean(self):
        cleaned_data = super().clean()
        birth_date = cleaned_data.get('birth_date')
        birth_month = cleaned_data.get('birth_month')
        birth_year = cleaned_data.get('birth_year')

        if birth_date is not None and birth_month is not None:
            if not (1 <= birth_date <= 31 and 1 <= birth_month <= 12):
                self.add_error('birth_date', 'Enter a valid day (1-31) and month (1-12).')

        if birth_year is not None:
            current_year = date.today().year
            if not (2013 <= birth_year <= current_year):
                self.add_error('birth_year', f'Enter a valid year (2013-{current_year}).')

        return cleaned_data