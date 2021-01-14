from django.db import models
from versatileimagefield.fields import VersatileImageField
from multiselectfield import MultiSelectField

LANGUAGE_CHOICES = (
    ('vo', 'Original'),
    ('en', 'English'),
    ('uk', 'Ukrainian'),
    ('de', 'German'),
    ('fr', 'French'),
    ('it', 'Italian'),
    ('no', 'Norwegian'),
    ('se', 'Swedish'),
    ('da', 'Danish'),
    ('es', 'Spanish'),
    ('ro', 'Romanian'),
    ('fi', 'Finnish'),
    ('ru', 'Russian'),
    ('ko', 'Korean'),
    ('ta', 'Tamil'),
    ('th', 'Thai'),
    ('lb', 'Luxembourgish'),
    ('nl', 'Dutch'),
    ('sw', 'Swahili'),
    ('ch', 'Chamoru'),
    ('jp', 'Japanese'),
    ('zh', 'Chinese'),
    ('ar', 'Arabic'),
    ('ar', 'Arabic'),
)


class Category(models.Model):
    label = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['label']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Genre(models.Model):
    label = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['label']


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre)
    country = models.CharField(max_length=64, null=True, blank=True)
    production_year = models.PositiveSmallIntegerField(verbose_name='Production Year', blank=True, null=True)
    duration = models.PositiveSmallIntegerField(help_text='in minutes', blank=True, null=True, editable=False)
    imdb_id = models.CharField(max_length=16, verbose_name='IMDb ID')
    languages = MultiSelectField(blank=True, default='', choices=LANGUAGE_CHOICES)
    subtitles = MultiSelectField(blank=True, default='', choices=LANGUAGE_CHOICES)
    release_date = models.DateField(verbose_name='Release Date', null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    cover_url = models.URLField(verbose_name='Cover URL', blank=True, null=True)
    cover_image = VersatileImageField(verbose_name='Cover Image', blank=True, null=True)
    backdrop_url = models.URLField(verbose_name='Backdrop URL', blank=True, null=True)
    backdrop_image = VersatileImageField(verbose_name='Backdrop Image', blank=True, null=True)
    episode_number = models.PositiveSmallIntegerField(verbose_name='Episode Number',
                                                      null=True,
                                                      blank=True)
    update_serial = models.CharField(max_length=14, null=True, blank=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.title
