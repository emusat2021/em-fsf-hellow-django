from django.db import models

# Create your models here.


class Item(models.Model):
    # will just have characters or text in it.
    #To prevent the creation of todo items without a name. 
    # The null equals false attribute here
    # prevents items from being created without a name programmatically
    # and blank equals false will make the field required on forms.
    # This way we're certain that a todo item can't be created without a name
    name = models.CharField(max_length=50, null=False, blank=False) 
    # dd a default value of false here just to make sure
    # that to-do items are marked as not done by default
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
