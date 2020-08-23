from django.db import models

class MessageBoard(models.Model) :
    writer = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    content = models.TextField()
    writedate = models.DateTimeField(auto_now_add=True)
    cnt = models.IntegerField(default=0)

