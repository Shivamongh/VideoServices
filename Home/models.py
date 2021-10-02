from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    Course_description = RichTextField()
    Is_premium = models.BooleanField(default=True)
    Course_image = models.ImageField(upload_to='course')
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course, self).save(self, *args, **kwargs)

    def __str__(self):
        return self.course_name

class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_module_name = models.CharField(max_length=100)
    course_description = RichTextField()
    video_url = models.URLField(max_length=300)
    can_view = models.BooleanField(default=False)