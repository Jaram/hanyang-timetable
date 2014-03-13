from django.conf.urls import patterns, url
from hanyang_time_table.utils.route import mapping
from views import *
urlpatterns = patterns(r'',
                       mapping(r'^depts$', get=get_depts),
                       mapping(r'^courses$', get=get_courses),
                       )
