from timecard.models import Employee, Role, Skill, Market
from django.contrib import admin


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'employee_name', 'employee_surname', 'employee_role', 'employee_skill', 'employee_market')
    search_fields = ('project_id',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'role_abbreviation', 'permission')
    search_fields = ('role_abbreviation',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
    search_fields = ('skill_name',)


class MarketAdmin(admin.ModelAdmin):
    list_display = ('market_name',)
    search_fields = ('market_name',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Market, MarketAdmin)