from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                'class': 'form-control item'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
# Function taken from https://www.youtube.com/watch?v=TBGRYkzXiTg&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=20

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control item'
        self.fields['password1'].widget.attrs['class'] = 'form-control item'
        self.fields['password2'].widget.attrs['class'] = 'form-control item'
