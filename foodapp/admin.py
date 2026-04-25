from django.contrib import admin
from .models import User, Candidate, Skill, CandidateSkill, Category, Item, Customer, SupportCase, Order, OrderItem, Employee, PayrollEntry

admin.site.register(User)
admin.site.register(Candidate)
admin.site.register(Skill)
admin.site.register(CandidateSkill)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(SupportCase)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(PayrollEntry)