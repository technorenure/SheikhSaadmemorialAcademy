from django.contrib import admin
from . models import *

admin.site.register([Section,Session,Term,Subject,StudentClass,LocalGovernment,State,Student, Gender])
