from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(forms.ModelForm):
    # Campos que no están en Perfil sino en User
    username = forms.CharField(max_length=150, label="Nombre de usuario")
    email = forms.EmailField(required=True, label="Correo electrónico")
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Perfil
        fields = ["telefono", "edad"]  # estos vienen de tu modelo Perfil

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Crear el usuario base de Django
        user = User(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
        )
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        # Crear el perfil enlazado
        perfil = super().save(commit=False)
        perfil.user = user
        if commit:
            perfil.save()

        return perfil
