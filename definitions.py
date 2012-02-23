#from report_tool.models import Pupil
#from django.contrib.admin.models import LogEntry
#
#def get_ds_hs():
#    return Pupil.objects.all()
#
#def get_student_in_class(_class_name):
#    return Pupil.objects.filter(class_id__name = _class_name)
#
#def get_admin_log():
#    return LogEntry.objects.all()

#def tk_hl_hk_dh_hk1():

try:
    from school.models import *
except :
    print ''

def mark_for_class(request):
#    return Mark.objects.filter(student_id__class_id__name = '6 A1')
    return Mark.objects.filter(subject_id__class_id__id = int(request.session.get('class_id')),term_id__number=int(request.session.get('termNumber')),current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')

def student_list(request, class_name):
    return Pupil.objects.filter(class_id__name = class_name)

def get_class_list(request):
    return Class.objects.filter(year_id__id = int(request.session.get('year_id')),year_id__school_id__id = int(request.session.get('school_id'))).order_by('name')

def get_subject_list_by_class(request):
    return Subject.objects.filter(name=request.session.get('subject_name'),class_id__year_id__id = int(request.session.get('year_id'))).order_by('class_id')

def get_subject_list_by_teacher(request):
    return Subject.objects.filter(name=request.session.get('subject_name'),class_id__year_id=int(request.session.get('year_id')),teacher_id__isnull=False).order_by('teacher_id__first_name','teacher_id__last_name')

