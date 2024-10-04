from django.db import models

class GameGenre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    games = models.TextField()  # We'll seperate different games with the commas for now

    def __str__(self):
        return self.title