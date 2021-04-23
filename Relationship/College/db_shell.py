from College.models import *

# exec(open("H:\\snehal\\Django\\Relationship\\College\\db_shell.py").read())

# c1 = College(name='VIT', address='Pune', fees=85000)
# c1.save()


# c1 = College.objects.get(id=3)
# Principle.objects.create(name='snehal', exp=7, college=c1)

colg = College.objects.get(id=1)
# print(colg)
# print(colg.id)
# print(colg.address)
# print(colg.principle.exp)  

# princi = Principle.objects.get(name='snehal')
# print(princi.college.id)

# dept_list = list(colg.dept.all())
# print(dept_list)

# dept_obj = Department.objects.all()[3]
# print(dept_obj)

# dept_obj = Department.objects.get(id=1)
# print(dept_obj.college)

# dept_list = list(colg.dept.all())
# print(dept_list)

# colg = College.objects.get(id=1)

# d = {colg.name:[]}
# for dept in dept_list:
#     d1 = {"dept id": dept.id, 'dept name': dept.name}
#     d[colg.name].append(d1)
# print(d)

# depts = Department.objects.filter(college__id=1)
# print(depts)

# depts = Department.objects.filter(college__name='COEP')
# print(depts)

# dept = Department.objects.get(name='IT')
# print(dept.teacher.all())

# t1 =Teacher.objects.get(name='AAS')
# print(t1.dept)

# teachers = Teacher.objects.filter(dept__college__id=2)
# print(teachers)

# sub_obj = Subject.objects.get(name='python')
# print(sub_obj.teacher)

# teach_obj = Teacher.objects.get(name='xyz')
# print(teach_obj.subj.all())

# subjs = Subject.objects.filter(teacher__dept__college__id=1).order_by('-name')
# print(subjs)

# stud_obj = Student.objects.get(id=1)
# print(stud_obj.subject.all())


# stud_obj = Student.objects.filter(subject__teacher__name='hhh')
# print(stud_obj)



# subjs = Student.objects.get(name='AA')
# print(subjs.subject.all())

