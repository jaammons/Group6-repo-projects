from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"id":"username", "name":"username", "label":"username",
                                                             "maxlength":"100", 'autofocus': True}) )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id":"password", "name":"password", "label":"password",
                                                             "maxlength":"100"}) )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"id":"remember_me"}))

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"id":"username", "name":"username", "maxlength":"100", 
                                                             }) )                                          
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder":"example@gmail.com"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"id":"password", "name":"password", "maxlength":"100"}) )
    confirmation = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"id":"confirmation", "name":"confirmation", 
                                                                  "maxlength":"100"}) )
