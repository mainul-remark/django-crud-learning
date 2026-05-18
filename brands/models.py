from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    website = models.CharField(max_length=150, blank=True)
    status = models.SmallIntegerField(default=1, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def save(
        self,
        *args,
        # force_insert = False,
        # force_update = False,
        # using = None,
        # update_fields = None,
            **kwargs
    ):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name