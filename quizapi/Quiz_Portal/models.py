from django.db import models
from userauth.models import User

question_type   = (('MCQ','MCQ'),('True_Flase','True_False'),('Description','Description'))

class Quiz(models.Model):
    quiz_code   = models.CharField(max_length=9, unique=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    time        = models.TimeField(auto_now=True)
    tags        = models.CharField(max_length=100)
    open_till   = models.TimeField()
    type        = models.CharField(max_length=50, choices=question_type)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    quiz        = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question    = models.TextField(max_length=500, default='Write your questions here.')
    q_image     = models.ImageField(upload_to='uploads/', max_length=1000, blank=True, null=True)
    option1     = models.CharField(max_length=100, blank=True, null=True)
    option2     = models.CharField(max_length=100, blank=True, null=True)
    option3     = models.CharField(max_length=100, blank=True, null=True)
    correct     = models.CharField(max_length=100, blank=True, null=True)
    true_false  = models.BooleanField()
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.quiz.name) + '-->'+str(self.quiz.type)
    
class Answers(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz        = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choosen     = models.CharField(max_length=100, blank=True, null=True)
    true_false  = models.BooleanField()
    description = models.TextField(max_length=1000, blank=True, null=True)
    a_image     = models.ImageField(upload_to='uploads/', max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.user.email)
    