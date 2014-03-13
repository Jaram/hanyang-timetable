# Create your views here.

from django.core import serializers
from django.utils import simplejson as json
from django.http import HttpResponse
from hanyang_time_table.courses.models import Course, Dept, Univ

def get_depts(request):
    response = dict( 
        error = True,
        )

    jojik_code = request.GET.get('jojik_code')
    if jojik_code is None :
        return HttpResponse(json.dumps(response), content_type='application/json')

    dept_list = Dept.objects.all().filter(univ__jojik_code = jojik_code)
    if not dept_list:
        return HttpResponse(json.dumps(response), content_type='application/json')

    response = dict(
        error = False,
        dept_list = serializers.serialize('python', dept_list)
        )

    return HttpResponse(json.dumps(response), content_type='application/json')

def get_courses(request):
    response = dict(
        error = True,
        )

    dept_code_list = request.GET.getlist('dept_code_list','')

    if dept_code_list is None:
        return HttpResponse(json.dumps(response), content_type='application/json')

    course_list = Course.objects.all().filter(dept__dept_code__in=dept_code_list)

    if not course_list:
        return HttpResponse(json.dumps(response), content_type='application/json')

    response = dict(
        error = False,
        course_list = serializers.serialize('python', course_list),
        )
    
    return HttpResponse(json.dumps(response), content_type='application/json')
