from django.contrib import admin

from members.models import Company, User, Attendance, Sector, Shift, Employee

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'role', 'company')
#     list_filter = ('company__name', 'role')
#     fields = ('company','role','first_name', 'last_name', 'username','password','email', 'is_superuser', )
#
#
# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ('attendee',)
#     list_filter = ('attendee__username','attendee__company__name')


admin.site.register(Sector)
admin.site.register(Shift)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Attendance)
