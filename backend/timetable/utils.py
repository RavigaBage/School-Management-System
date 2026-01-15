from timetable.models import AcademicYear


def get_active_academic_year():
    return AcademicYear.objects.filter(is_active=True).first()