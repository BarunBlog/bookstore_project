from django.db import models

Genre_Choices = (
    ('Romantic', 'Romantic'),
    ('Horror', 'Horror'),
    ('Action', 'Action'),
    ('Fiction', 'Fiction'),
    ('Narrative', 'Narrative'),
    ('Novel', 'Novel'),

)

class Author(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    genre = models.CharField(max_length=100, choices=Genre_Choices)


    class Meta:
        verbose_name_plural = 'Books'
        

    def __str__(self):
        return self.titme