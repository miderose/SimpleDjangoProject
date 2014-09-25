from django.db import models

MARCHE_TELEFONINI = (
    ('Apple', 'Apple'),
    ('Nokia', 'Nokia'),
    ('Samsung', 'Samsung'),
    ('Blackberry', 'Blackberry'),
    ('Altro...', 'Altro...')
)



class Persona(models.Model):
    '''Modello Persona.
    Ogni persona puo' leggere piu' libri, e possedere un solo telefonino.'''

    nome = models.CharField(max_length=256)
    cognome = models.CharField(max_length=256)
    data_nascita = models.DateField()
    libri = models.ManyToManyField("Libro")
    telefonino = models.ForeignKey("Telefonino")

    def __unicode__(self):
        return "%s %s" % (self.nome, self.cognome)

    class Meta():
        verbose_name_plural = "Persone"



class Libro(models.Model):
    '''Modello Libro'''
    titolo = models.CharField(max_length=256)

    def __unicode__(self):
        return self.titolo

    class Meta():
        verbose_name_plural = "Libri"



class Telefonino(models.Model):
    '''Modello Telefonino'''
    marca = models.CharField(max_length=256, choices=MARCHE_TELEFONINI)
    modello = models.CharField(max_length=256)

    def __unicode__(self):
        return "%s %s" % (self.marca, self.modello)

    class Meta():
        verbose_name_plural = "Telefonini"
