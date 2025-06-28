from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_member(self, user):
        return CourseMember.objects.filter(course_id=self, user_id=user).exists()

class CourseMember(models.Model):
    ROLE_OPTIONS = (
        ('std', 'Student'),
        ('tch', 'Teacher')
    )
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.CharField(max_length=3, choices=ROLE_OPTIONS)

    def __str__(self):
        return f"{self.course_id} : {self.user_id}"