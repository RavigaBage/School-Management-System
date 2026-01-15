from django.contrib import admin
from .models import (
    AcademicYear,
    Term,
    SchoolClass,
    Department,
    Subject,
    Teacher,
    TeachingAssignment,
    WeekDay,
    TimeSlot,
    TimetableEntry
)

# Academic Year
@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_display_links = ('name',)

# Term
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year', 'start_date', 'end_date')
    list_display_links = ('name',)

# School Class
@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_id', 'teacher_id', 'academic_year')
    list_display_links = ('name', 'class_id')

# Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

# Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department')
    list_display_links = ('name', 'code')

# Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'specialization', 'user')
    list_display_links = ('staff_id', 'first_name', 'last_name')

# Teaching Assignment
@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject', 'school_class', 'academic_year', 'is_active')
    list_display_links = ('teacher', 'subject', 'school_class')

# WeekDay
@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_display_links = ('name',)

# TimeSlot
@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'is_break')
    list_display_links = ('start_time', 'end_time')

# Timetable Entry
@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'term', 'weekday', 'time_slot', 'room_number', 'status')
    list_display_links = ('school_class', 'term')
