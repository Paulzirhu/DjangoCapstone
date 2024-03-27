from django.db import models

class BandMember(models.Model):
    """Model representing a band member."""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        """String for representing the BandMember object."""
        return self.name

class Album(models.Model):
    """Model representing an album."""
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/')
    description = models.TextField()

    def __str__(self):
        """String for representing the Album object."""
        return self.title

class Show(models.Model):
    """Model representing a show."""
    date = models.DateField()
    location = models.CharField(max_length=100)
    # Add more fields as needed

class Merchandise(models.Model):
    """Model representing merchandise."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
