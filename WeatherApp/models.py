from django.db import models


# Таблица с названиями городов, которые вводили в форме
class City(models.Model):
    name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name
