from django.db import models


class Entry(models.Model):
    text=models.TextField(max_length=200000)
    date_posted=models.DateTimeField(auto_now_add=True)

class Entry_sport(models.Model):
    text_sport=models.TextField(max_length=200000)
    date_posted_sport=models.DateTimeField(auto_now_add=True)    

    def  __str__(self):
        return 'Entry #{}'.format(self.id)
