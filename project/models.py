from django.contrib.auth.models import AbstractUser
from django.db import models


class Base(models.Model):
    """
    Base abstract model class providing common timestamp fields.

    This model serves as a base class for other models, adding automatic
    timestamp tracking for creation and modification times.

    Attributes:
        created (DateTimeField): Automatically set to current timestamp when object is created.
            This field is read-only and cannot be modified after creation.
        modified (DateTimeField): Automatically updated to current timestamp whenever object is saved.
            Updates on every save() operation.

    Meta:
        abstract (bool): True - indicates this is an abstract base class that will not be created as a table.
    """

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
