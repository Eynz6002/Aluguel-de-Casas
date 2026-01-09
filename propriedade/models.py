from django.db import models
from usuario.models import Usuario

# Create your models here.
class Propriedade(models.Model):
    foto_default = ''
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    preco = models.IntegerField()
    foto = models.ImageField(upload_to='propriedades/', null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)

    def foto_padrao(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        
        return '/media/padrao/casa_padrao.png'