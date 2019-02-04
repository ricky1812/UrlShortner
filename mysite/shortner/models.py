from django.db import models
import string
import random
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Bitly(models.Model):
    website=models.CharField(max_length=200)
    keys=models.CharField(max_length=10, unique=True, blank=True)
    def __str__(self):
        self.keys=random_generator()
        return self.website
    def save(self, *args, **kwargs):
        if self.keys==None or self.keys=="":
            self.keys=random_generator()
            super(Bitly, self).save(*args, **kwargs)
    
    
   


# Create your models here.
