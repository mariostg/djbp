from django.db import models
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProjectUser(AbstractUser):
    """A custom user model extending Django's AbstractUser.

    This model adds a many-to-many relationship with PlantProfile through
    the PlantCollection intermediary model.

    Attributes:
        plants (ManyToManyField): Collection of PlantProfile objects associated with the user
            through PlantCollection model.

    Example:
        Assuming a project with a PlantProfile model, the following code snippet demonstrates
        a ManyToManyField relationship:
        >>> from project.models import ProjectUser, PlantProfile
        >>> plants = models.ManyToManyField(PlantProfile, through="PlantCollection")
        >>> user = ProjectUser.objects.create(username='plantlover')
        >>> user.plants.all()
        <QuerySet []>
    """

    def __str__(self):
        return str(self.username)
