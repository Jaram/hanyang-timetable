# -*- coding:utf-8 -*-

from django.db import models

class Univ(models.Model):

    univ_code = models.CharField(max_length = 30, primary_key = True)
    jojik_code = models.CharField(max_length = 30)

    name = models.CharField(max_length = 60, null = True)

    
class Dept(models.Model):
    # relationships
    univ = models.ForeignKey(Univ, )

    # 
    dept_code = models.CharField(max_length = 30, primary_key = True)

    # 
    name_ko = models.CharField(max_length = 150, null = True)
    
    #
    name_en = models.CharField(max_length = 150, null = True)

    #



class Course(models.Model):
    # format Name : TypeOrigin -> TypeDB / Meaning.
    # Name in data set with TypeOrigin, but stores in with TypeDB in DB

    # django does not support multi column primary key
    # django gives id = AutoField(primary_key=True) automatically to the object    # that did not set primary key explicitly

    # relationships
    dept = models.ForeignKey('Dept', null = True)

    # suupNo : string -> integer / unique key of the course
    course_no = models.CharField(max_length = 20)

    # course_number2 = models.IntegerField()

    # suupYear : string -> integer / year of the course
    year = models.IntegerField(null = True)

    # suupTerm : string -> integer / semester of the course
    semester = models.IntegerField(null = True)
    
    # haksuNo : string -> string / course identifier
    course_identifier = models.CharField(max_length = 10, null = True)
    
    # gwamokNm : string -> string / name of the course
    name_ko = models.CharField(max_length = 150, null = True)
    
    # gwamokEnm : string -> string / english name of the course
    name_en = models.CharField(max_length = 150, null = True)
    
    # isuGbCd : string -> integer / classification of the course
    classification = models.IntegerField(null = True)

    # banGrade : string -> integer / grade for the course
    grade = models.IntegerField(null = True)

    # yungyukGb : string -> string / course domain
    # used for cultural subjects
    course_domain = models.CharField(max_length = 20, null = True)

    # ilbalCommonGb : string -> boolean / divider for major subject and cultural subject
    # 1-> false -> cultural, 2 -> true -> major 
    is_major = models.BooleanField()

    # hakjeom : string -> integer / credit for the course
    credit = models.IntegerField(null = True)

    # hakwiGb : string -> integer / degree for the course
    degree = models.IntegerField(null = True) 

    # daepyoGangsaNo : string -> string / instructor's number
    representative_instructor_no = models.CharField(max_length = 20, null = True)
    
    # daepyoGangsaNm : string -> string / instructor's name
    instructor_name = models.CharField(max_length = 40, null = True)
    
    # ???    gyogangsaNms:이경아

    # suupTimes : string -> string? / course time
    time = models.CharField(max_length = 150, null = True)
    
    # suupRoomNms : string -> string / class room
    classroom = models.CharField(max_length = 60, null = True)

