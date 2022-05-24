from django.db import models
from django.contrib.auth.models import User

class Genres(models.Model):
    name = models.TextField()

class BookJournalBase(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.ForeignKey(Genres,related_name='books',on_delete=models.CASCADE)

class Journal(BookJournalBase):
    TYPES = (
        (1,'Bullet'),
        (2,'Food'),
        (3,'Travel'),
        (4,'Sport'),
    )


    type = models.IntegerField(choices=TYPES)
    publisher = models.ForeignKey(User,related_name="journals",on_delete=models.CASCADE)

