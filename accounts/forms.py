from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    department = forms.CharField(max_length=100)
    section = forms.CharField(max_length=50, required=False)  # section is optional for teachers
    year = forms.IntegerField(required=False, widget=forms.Select(choices=[(i, f"Year {i}") for i in range(1, 6)]))  # Year selection for students

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role', 'department', 'section', 'year']
        
        #here init method is used to modify the behaviour of user model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Hide 'section' and 'year' fields for teachers
        if self.instance and self.instance.role != CustomUser.STUDENT:
            self.fields['section'].widget = forms.HiddenInput()  # Hide section field for teachers
            self.fields['year'].widget = forms.HiddenInput()  # Hide year field for teachers
            self.fields['section'].required = False  # Don't require section for teachers
            self.fields['year'].required = False  # Don't require year for teachers

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        section = cleaned_data.get('section')
        year = cleaned_data.get('year')

        # If the user is a student, THEN 'section' and 'year' fields are provided
        if role == CustomUser.STUDENT:
            if not section:
                raise forms.ValidationError("Section is required for students.")
            if not year:
                raise forms.ValidationError("Year is required for students.")

        return cleaned_data





