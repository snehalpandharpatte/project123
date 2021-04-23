from aadhar.models import Person, Adhar


# exec(open("H:\\snehal\\Django\\djrelationship\\aadhar\\db_shell.py").read())

# p5 = Person(name='rohini kulkarni',email='rk@gmail.com',mobile='4536718')
# p5.save()

# a5=Adhar(person=p5,signature='fjulkhf524dskluiq3&^$^GUJHVR',adhar_no='25638796123')
# a3.save()

# (denv) H:\snehal\Django\djrelationship>python manage.py shell
# Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from aadhar.models import Person
# >>> p1 = Person(name='smita Joshi',email='smjoshi@gmail.com',mobile='123412')
# >>> p1.save()
# >>> p2=Person(name='Neeta patil',email='nepatil@gmail.com',mobile='0987632')
# >>> p2.save()
# >>> from aadhar.models import Adhar
# >>> a1=Adhar(person=p1,signature='asdf234dsafuiq3&^$^GUJHVR',adhar_no='432198176354')
# >>> a1.save()
# >>> a2=Adhar(person=p2,signature='adfpoiwruywqtrgmnb13241*&^%$',adhar_no='2314928376')
# >>> a2.save()
# >>> p=Person.objects.all()
# >>> p
# <QuerySet [<Person: Person object (1)>, <Person: Person object (2)>, <Person: Person object (3)>, <Person: Person
# object (4)>]>
# >>> a=Adhar.objects.all()
# >>> a
# <QuerySet [<Adhar: Adhar object (1)>, <Adhar: Adhar object (2)>, <Adhar: Adhar object (3)>]>
# >>> a.values()
# <QuerySet [{'id': 1, 'person_id': 2, 'signature': 'afdf', 'adhar_no': '445526669666'}, {'id': 2, 'person_id': 3, 'signature': 'asdf234dsafuiq3&^$^GUJHVR', 'adhar_no': '432198176354'}, {'id': 3, 'person_id': 4, 'signature': 'adfpoiwruywqtrgmnb13241*&^%$', 'adhar_no': '2314928376'}]>
# >> from aadhar.models import Person
# >>> p3 = Person(name='mayuri dathe',email='mdathe@gmail.com',mobile='356879')
# >>> p3.save()
# >>> from aadhar.models import Adhar
# >>> from aadhar.models import Adhar
# >>> a3=Adhar(person=p3,signature='bndhw524dskluiq3&^$^GUJHVR',adhar_no='453678367895')
# >>> a3.save()