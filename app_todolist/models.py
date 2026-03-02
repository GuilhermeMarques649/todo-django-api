from django.db import models

# Create your models here.
class Tarefa(models.Model):
      
    DIAS_SEMANA = [
        ("SEG", "Segunda"),
        ("TER", "Terça"),
        ("QUA", "Quarta"),
        ("QUI", "Quinta"),
        ("SEX", "Sexta"),
        ("SAB", "Sábado"),
        ("DOM", "Domingo"),
    ]
    PERIODO = [
        ("MAN", "Manhã"),
        ("TAR", "Tarde"),
        ("NOT", "Noturno")
    ]
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100, blank=True)
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA)
    periodo = models.CharField(max_length=3, choices=PERIODO, default="MAN")
    concluida = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo