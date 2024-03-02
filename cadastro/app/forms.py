from django.forms import ModelForm
from app.models import Carro

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ["carro","marca","ano"]
 