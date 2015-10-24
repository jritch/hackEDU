from django.db import models

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	answer_text = models.CharField(max_length=200)

class Student(models.Model):
	name  = models.CharField(max_length=200)   

class Session(models.Model):
	timestamp = models.DateTimeField(auto_now=True)

class Answer(models.Model):
	student_id = models.ForeignKey(Student)
	question_id = models.ForeignKey(Question)
	session_id = models.ForeignKey(Session)
	answer_text = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now=True)
