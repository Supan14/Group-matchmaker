from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    TEXT_C = [
        ("Proj1", "Proj1"),
        ("Proj2", "Proj2"),
        ("Proj3", "Proj3"),
        ("Proj4", "Proj4")
    ]
    GENDER_C = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    OS_C = [
        ("BTech", "BTech"),
        ("MTech", "MTech"),
        ("Other", "Other")
    ]
    SPACES_C = [
        ("Tabs", "Tabs"),
        ("Spaces", "Spaces")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=10000, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(
        max_length=10000, blank=True, null=True, choices=GENDER_C)
    profile_image = models.ImageField(
        upload_to='profile_pic', default="default.jpg", null=True, blank=True)
    bio = models.TextField(null=True)
    tech_stack = models.CharField(max_length=10000, null=True)

    editor = models.CharField(
        max_length=10000, choices=TEXT_C, default=None, null=True, blank=True)
    os = models.CharField(
        max_length=10000, choices=OS_C, default=None, null=True, blank=True)
    spacing = models.CharField(
        max_length=10000, choices=SPACES_C, default=None, null=True, blank=True)

    likeability = models.ManyToManyField(
        User, related_name="likes", blank=True)
    blocked_by = models.ManyToManyField(
        User, related_name="blocked", blank=True)

    def __str__(self):
        return f"{self.full_name} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 200 or img.width > 200:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

    @property
    def num_likes(self):
        return self.likeability.all().count()
