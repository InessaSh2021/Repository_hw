import re
from pprint import pprint
import csv

contacts_list = "Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,   +7 (495) 913-04-78,opendata@nalog.ru Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037, Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168, Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет    проектов Управления информационных технологий,,, Лукина Ольга   Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru"

# with open("phonebook_raw.csv") as f:
#   rows = csv.reader(f, delimiter=",")
#   contacts_list = list(rows)
# pprint(contacts_list)

contacts_list2 = re.sub(r"(\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?(доб.)\s(\d{4})\)?)*", r"+7(\2)\3-\4-\5 \7\8", contacts_list) 
print(contacts_list2)
print()

contacts_list3 = re.sub(r"([А-Я][а-я]+[\s|,][А-Я][а-я]+[,|\s][А-Я][а-я]+)|(,[А-Я]{3},)|(,,[А-Я][а-я]+,)|(\+7\(\d{3}\)\d{3}-\d{2}-\d{2}\s([а-я]{3}\.\d{4})*)|(,((\w?\w+\.?(\w+)*|\d+)@\w+\.\w+))|(\n+?|\t|,)|(Лагунцов Иван)|(\w+)", r"\12", contacts_list2)

position_list = re.split('  ', contacts_list3)

phone_list = re.findall('(\+7\(\d{3}\)\d{3}-\d{2}-\d{2}[\sдоб.\d{4}]*)', contacts_list2)

user_email = re.sub(r"(([А-Я][а-я]+)(,?|\s))(([А-Я][а-я]+)\s)([А-Я][а-я]+)|(,([А-Я]+),)|((\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?([а-я].)\s(\d{4})\)?)*)|(\w+.\w+@\w+.ru)|(\w+)|(,,([А-Я][а-я]+),)|.", r"\18 ", contacts_list2)

user_email_list = re.findall('(\w+.\w+@\w+.ru)', user_email)

organization_list = re.findall('([А-Я]{3}|[А-Я][а-я]{5},)', contacts_list2)
del(organization_list[3])

# namelist = re.sub(r"(([А-Я][а-я]+)(,?|\s))(([А-Я][а-я]+)\s)([А-Я][а-я]+)|(,([А-Я]+),)|((\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?([а-я].)\s(\d{4})\)?)*)|(,((\w?\w+\.?(\w+)*|\d+)@\w+\.\w+))|(\w+)|(,,([А-Я][а-я]+),)|.", r"\2 \5 \6 ", contacts_list) 

# namelist = re.findall('[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+', namelist)

name = re.sub(r"(([А-Я][а-я]+)(,?|\s))(([А-Я][а-я]+)\s)([А-Я][а-я]+)|(,([А-Я]+),)|((\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?([а-я].)\s(\d{4})\)?)*)|(,((\w?\w+\.?(\w+)*|\d+)@\w+\.\w+))|(\w+)|(,,([А-Я][а-я]+),)|.", r"\2 \5 \6 ", contacts_list) 

name_list = re.findall('[А-Я][а-я]+', name)


with open('phonebook_raw.csv', 'w') as csvfile:
    fieldnames = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([
      {'lastname': name_list[0], 'firstname': name_list[1], 'surname': name_list[2], 'organization': organization_list[0], 'position': position_list[0], 'phone': phone_list[0], 'email': user_email_list[0]},
      {'lastname': name_list[3], 'firstname': name_list[4], 'surname': name_list[5], 'organization': organization_list[1], 'position': position_list[1], 'phone': phone_list[1], 'email': "нет данных email"},
      {'lastname': name_list[6], 'firstname': name_list[7], 'surname': name_list[8], 'organization': organization_list[2], 'position': "нет данных position", 'phone': phone_list[2], 'email': "нет данных email"},
      {'lastname': name_list[9], 'firstname': name_list[10], 'surname': name_list[11],'organization': organization_list[3], 'position': "нет данных position", 'phone': phone_list[4], 'email': user_email_list[2]},
      # {'lastname': name_list[12], 'firstname': name_list[13], 'surname': name_list[14],'organization': organization_list[4], 'position': "нет данных position", 'phone': phone_list[4], 'email': user_email_list[4]},
      # {'lastname': namelist[5], 'organization': organization_list[5], 'position': "нет данных position", 'phone': phone_list[5], 'email': user_email_list[5]}
      ])

print()
print("writing complete")