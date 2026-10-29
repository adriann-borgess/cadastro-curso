from django.db import models

# Create your models here.

class  Modalidade(models.TextChoices):
    PRESENCIAL = 'Presencial', 'Presencial'
    EAD = 'EAD', 'Educação a Distância — EAD'
    HIBRIDO = 'Híbrido', 'Híbrido'

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField(blank=True)
    carga_horaria = models.PositiveIntegerField()
    modalidade = models.CharField(max_length=10, choices=Modalidade.choices)
    data_inicio = models.DateField()
    ativo = models.BooleanField(default=True)
    cadastrado_em =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.codigo} — {self.nome}'