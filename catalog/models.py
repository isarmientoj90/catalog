
# Create your models here.
from django.db import models

from django.urls import reverse  # To generate URLS by reversing URL patterns

class MyModelName(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """

    # Campos
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.field_name
        
        
    
class Dictionary(models.Model):
    
    title = models.CharField(max_length=200)
    #author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    #summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    # isbn = models.CharField('ISBN', max_length=13,
                            # unique=True,
                            # help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      # '">ISBN number</a>')
    # genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # # Genre class has already been defined so we can specify the object above.
    # language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    # class Meta:
        # ordering = ['title', 'author']

    # def display_genre(self):
        # """Creates a string for the Genre. This is required to display genre in Admin."""
        # return ', '.join([genre.name for genre in self.genre.all()[:3]])

    # display_genre.short_description = 'Genre'

    # def get_absolute_url(self):
        # """Returns the url to access a particular book instance."""
        # return reverse('book-detail', args=[str(self.id)])

    # def __str__(self):
        # """String for representing the Model object."""
        # return self.title
