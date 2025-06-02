from django.db import models

class Title(models.Model):
    #A book the user is reading.
     text = models.CharField(max_length=200)
     date_added = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        """Return a string representation of the model."""
        return self.text
     
class Entry(models.Model):
    #Something they could relate to in the book
    title= models.ForeignKey(Title, on_delete=models.CASCADE)
    text= models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

    class Metadata:
        verbose_name_plural='entries'

    def __str__(self):
        #Return a simple string representing the entry
        return f"{self.text[:50]}..."   