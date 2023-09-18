from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='TrekImages')
    imageName = models.CharField(max_length = 40)

    def __str__(self):
        return str(self.image)
    
    # def get_default():
    #     return Photo.objects.get(pk = 1)


class TrekDetail(models.Model):

    # Each choice should be a tuple containing a value and a human-readable label.
    TrekChoices = [('Trek','Treking'),('Camp','Camping'),('Himalaya','Himalaya')]

    imageFK = models.ForeignKey(Photo, on_delete = models.SET_NULL, null=True)
    # We need to specify what operation we need to perform when foreign 
    # key is deleted 
    
    name = models.CharField(max_length=100)
    startDate = models.DateField()
    price = models.IntegerField(default=1299)
    endDate = models.DateField()
    location = models.CharField(max_length=100)

    # This is the way to add choices to data field
    category = models.CharField(max_length=10, choices=TrekChoices, default='Trek')

    desc = models.TextField()
    upcomingBatches = models.TextField()
    iternary = models.TextField()
    trekEventDetails = models.TextField()
    costIncludes = models.TextField()
    thingsToCarry = models.TextField()
    pickupPoints = models.TextField()
    faq = models.TextField()

