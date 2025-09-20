from django.db import models


class Role(models.Model):
    class Hierarchy(models.IntegerChoices):
        OM = 1
        TL = 2
        WFM = 3
        QA = 4
        TC = 5
        AGENT = 6
    
    role_name = models.CharField(max_length=100)
    role_abbreviation = models.CharField(max_length=5)
    permission = models.IntegerField(choices=Hierarchy)

    def __str__(self):
        return f"{self.role_abbreviation}"


class Skill(models.Model):
    class SkillName(models.TextChoices):
        RESOLUTION_ONE = 'R1', 'Resolutions 1'
        RESOLUTION_TWO = 'R2', 'Resolutions 2'
        SUPERHOST = 'DSS', 'Dedicated SuperHost Suport'
        EXPERIENCE = 'EXP', 'Experience'

    skill_name = models.CharField(max_length=3, choices=SkillName)

    def __str__(self):
        return f"{self.skill_name}"


class Market(models.Model):
    class Language(models.TextChoices):
        ITALIAN = 'ITA', 'Italian'

    market_name = models.CharField(max_length=3, choices=Language, default=Language.ITALIAN)

    def __str__(self):
        return f"{self.market_name}"


class Employee(models.Model):
    project_id = models.IntegerField(unique=True)
    employee_name = models.CharField(max_length=100)
    employee_surname = models.CharField(max_length=150)
    employee_role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='employee_role')
    employee_skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='employee_skill')
    employee_market = models.ForeignKey(Market, on_delete=models.PROTECT, related_name='employee_market')

    def __str__(self):
        return f"{self.employee_name} {self.employee_surname} - {self.employee_role} {self.employee_skill} {self.employee_market}"