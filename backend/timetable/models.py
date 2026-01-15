from django.db import models
# Create your models here.

class AcademicYear(models.Model):
    name = models.CharField(max_length=20)  # e.g. "2024/2025"
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Term(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)  # Term 1, Term 2, Term 3
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.academic_year}"

class SchoolClass(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)  
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=30, unique=True,null=True, blank=True)
    teacher_id = models.CharField(max_length=30, unique=True,null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100,null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField("accounts.SmsUser", on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=30, unique=True,null=True, blank=True)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.staff_id})"

class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("teacher", "subject", "school_class","academic_year")

    def __str__(self):
        return f"{self.teacher} → {self.subject} ({self.school_class})"

class WeekDay(models.Model):
    name = models.CharField(max_length=20,unique=True)  # Monday
    order = models.PositiveIntegerField(unique=True)   # 1–5

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_break = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class TimetableEntry(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20,  blank=True,null=True)
    teaching_assignment = models.ForeignKey(
        TeachingAssignment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ("draft", "Draft"),
            ("completed", "Completed"),
            ("conflict", "Conflict"),
        ],
        default="draft"
    )


    class Meta:
        unique_together = ("school_class", "term", "weekday", "time_slot")

    def __str__(self):
        return f"{self.school_class} | {self.weekday} | {self.time_slot}"
    
    def has_teacher_conflict(self):
        if not self.teaching_assignment:
            return False

        return TimetableEntry.objects.filter(
            weekday=self.weekday,
            time_slot=self.time_slot,
            teaching_assignment__teacher=self.teaching_assignment.teacher
        ).exclude(pk=self.pk).exists()



