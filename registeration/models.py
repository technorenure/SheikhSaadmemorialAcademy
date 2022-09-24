from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=20)
    is_current = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=20)
    is_current = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return self.name

class StudentClass(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class LocalGovernment(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=200)
    sex = models.ForeignKey(Gender, on_delete=models.CASCADE)
    home_town = models.CharField(max_length=20)
    local_government = models.ForeignKey(LocalGovernment, on_delete=models.CASCADE)
    state_of_origin = models.ForeignKey(State, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=20)
    previous_school_if_any = models.CharField(max_length=20, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    father_Guardian_name = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=255)
    occupation = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    mother_phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ScoreSheet(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ca1 = models.IntegerField(default=0)
    ca2 = models.IntegerField(default=0)
    exam = models.IntegerField(default=0)
    def total(self):
        return self.ca1 + self.ca2 + self.exam


