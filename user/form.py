from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "input-large span10", "placeholder":"type username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "input-large span10", "placeholder":"type password"}))

    def is_valid(self):
        if len(self.data["username"].strip()) > 100:
            return False

        return True
