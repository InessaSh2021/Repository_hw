import re
from pprint import pprint
import csv

contacts_list = "�������� ���� ������������,,,���,������� ���������� � ������� ������ �������������� � ������������ �������� ������ ���������� ��������������� ��������� � ������� ���������� ���,   +7 (495) 913-04-78,opendata@nalog.ru ���������� ������� �����������,,,���,,+74959130037, �������,�������� ����������,,���,,8 495-913-0168, ����������,�������,�����������,���,c������� ������ ��������    �������� ���������� �������������� ����������,,, ������ �����   ������������,,,������,,+7 (495) 983-36-99 ���. 2926,Olga.Lukina@minfin.ru ������� ������� ������������,,,������,,8(495)748-49-73,1248@minfin.ru �������� ���� ����������,,,������,,+7 (495) 913-11-11 (���. 0792),�������� ����,,,,,,Ivan.Laguntcov@minfin.ru"

# with open("phonebook_raw.csv") as f:
#   rows = csv.reader(f, delimiter=",")
#   contacts_list = list(rows)
# pprint(contacts_list)

contacts_list2 = re.sub(r"(\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?(���.)\s(\d{4})\)?)*", r"+7(\2)\3-\4-\5 \7\8", contacts_list) 
print(contacts_list2)
print()

contacts_list3 = re.sub(r"([�-�][�-�]+[\s|,][�-�][�-�]+[,|\s][�-�][�-�]+)|(,[�-�]{3},)|(,,[�-�][�-�]+,)|(\+7\(\d{3}\)\d{3}-\d{2}-\d{2}\s([�-�]{3}\.\d{4})*)|(,((\w?\w+\.?(\w+)*|\d+)@\w+\.\w+))|(\n+?|\t|,)|(�������� ����)|(\w+)", r"\12", contacts_list2)

position_list = re.split('  ', contacts_list3)

phone_list = re.findall('(\+7\(\d{3}\)\d{3}-\d{2}-\d{2}[\s���.\d{4}]*)', contacts_list2)

user_email = re.sub(r"(([�-�][�-�]+)(,?|\s))(([�-�][�-�]+)\s)([�-�][�-�]+)|(,([�-�]+),)|((\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?([�-�].)\s(\d{4})\)?)*)|(\w+.\w+@\w+.ru)|(\w+)|(,,([�-�][�-�]+),)|.", r"\18 ", contacts_list2)

user_email_list = re.findall('(\w+.\w+@\w+.ru)', user_email)

organization_list = re.findall('([�-�]{3}|[�-�][�-�]{5},)', contacts_list2)
del(organization_list[3])

# namelist = re.sub(r"(([�-�][�-�]+)(,?|\s))(([�-�][�-�]+)\s)([�-�][�-�]+)|(,([�-�]+),)|((\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?([�-�].)\s(\d{4})\)?)*)|(,((\w?\w+\.?(\w+)*|\d+)@\w+\.\w+))|(\w+)|(,,([�-�][�-�]+),)|.", r"\2 \5 \6 ", contacts_list) 

# namelist = re.findall('[�-�][�-�]+\s[�-�][�-�]+\s[�-�][�-�]+', namelist)

name = re.sub(r"(([�-�][�-�]+)(,?|\s))(([�-�][�-�]+)\s)([�-�][�-�]+)|(,([�-�]+),)|((\+7|8)\s?\(?(\d{3})\)?[-| ]?(\d{3})[-| ]?(\d{2})[-| ]?(\d{2})(\s\(?([�-�].)\s(\d{4})\)?)*)|(,((\w?\w+\.?(\w+)*|\d+)@\w+\.\w+))|(\w+)|(,,([�-�][�-�]+),)|.", r"\2 \5 \6 ", contacts_list) 

name_list = re.findall('[�-�][�-�]+', name)


with open('phonebook_raw.csv', 'w') as csvfile:
    fieldnames = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([
      {'lastname': name_list[0], 'firstname': name_list[1], 'surname': name_list[2], 'organization': organization_list[0], 'position': position_list[0], 'phone': phone_list[0], 'email': user_email_list[0]},
      {'lastname': name_list[3], 'firstname': name_list[4], 'surname': name_list[5], 'organization': organization_list[1], 'position': position_list[1], 'phone': phone_list[1], 'email': "��� ������ email"},
      {'lastname': name_list[6], 'firstname': name_list[7], 'surname': name_list[8], 'organization': organization_list[2], 'position': "��� ������ position", 'phone': phone_list[2], 'email': "��� ������ email"},
      {'lastname': name_list[9], 'firstname': name_list[10], 'surname': name_list[11],'organization': organization_list[3], 'position': "��� ������ position", 'phone': phone_list[4], 'email': user_email_list[2]},
      # {'lastname': name_list[12], 'firstname': name_list[13], 'surname': name_list[14],'organization': organization_list[4], 'position': "��� ������ position", 'phone': phone_list[4], 'email': user_email_list[4]},
      # {'lastname': namelist[5], 'organization': organization_list[5], 'position': "��� ������ position", 'phone': phone_list[5], 'email': user_email_list[5]}
      ])

print()
print("writing complete")