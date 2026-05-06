from django.db import models
from django.utils import timezone


class Park(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição")
    image = models.ImageField("Imagem", upload_to='parks/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Parque"
        verbose_name_plural = "Parques"


class Trail(models.Model):
    name = models.CharField("Nome", max_length=100)
    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name="Parque")
    difficulty = models.CharField("Dificuldade", max_length=50)
    length_km = models.FloatField("Distância (km)")
    duration_min = models.IntegerField("Duração (min)", blank=True, null=True)
    description = models.TextField("Descrição")
    image = models.ImageField("Imagem", upload_to='trails/', blank=True, null=True)
    is_open = models.BooleanField("Aberta", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Trilha"
        verbose_name_plural = "Trilhas"


class Event(models.Model):
    name = models.CharField("Nome", max_length=100)
    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name="Parque")
    date = models.DateField("Data")
    description = models.TextField("Descrição", blank=True)
    image = models.ImageField("Imagem", upload_to='events/', blank=True, null=True)
    is_open = models.BooleanField("Disponível", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class Availability(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name="Parque")
    open_time = models.TimeField("Horário de abertura")
    close_time = models.TimeField("Horário de fechamento")
    is_open = models.BooleanField("Funcionamento ativo", default=True)

    def currently_open(self):
        if not self.is_open:
            return False

        current_time = timezone.localtime().time()
        return self.open_time <= current_time <= self.close_time

    def __str__(self):
        return f"{self.park.name} ({self.open_time} - {self.close_time})"

    class Meta:
        verbose_name = "Funcionamento"
        verbose_name_plural = "Funcionamentos"


class Waterfall(models.Model):
    name = models.CharField("Nome", max_length=100)
    park = models.ForeignKey(
        Park,
        on_delete=models.SET_NULL,
        verbose_name="Parque",
        null=True,
        blank=True
    )
    location = models.CharField("Localização", max_length=100, blank=True)
    description = models.TextField("Descrição")
    image = models.ImageField("Imagem", upload_to='waterfalls/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cachoeira"
        verbose_name_plural = "Cachoeiras"


class Biodiversity(models.Model):
    name = models.CharField("Nome", max_length=100)
    category = models.CharField("Categoria", max_length=100)
    description = models.TextField("Descrição")
    image = models.ImageField("Imagem", upload_to='biodiversity/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Biodiversidade"
        verbose_name_plural = "Biodiversidade"