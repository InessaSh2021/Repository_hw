�����
3
���� | 2 | ��
������ | 100 | ��
������� | 2 | ��

���� ��-��������
4
���� | 1 | ��
���� | 2 | �
��� | 3 | ��.�
������ ���� | 60 | ��

���������� ���������
3
��������� | 1 | ��
������ | 3 | ����
��� ����� | 100 | �

�������
5
�������� | 500 | �
����� ������� | 1 | ��
����� | 2 | ��
������ ����� | 1 | ��.�
������� | 2 | ��



from pprint import pprint

with open('recipes.txt', encording='utf-8') as file:
        cook_book = dicht()        
        for line in file:
                dishes = line.strip()
                counter = int(file.readline().strip())
                ingr_dicht = dicht()
                temp_list = []
                for ingredients in range(quantity):                        
                        ingr = f.readline().split('|')
                        ingr_dicht['ingr_name'] = ing[0].strip()
                        ingr_dicht['quantity'] = ing[1].strip()
                        ingr_dicht['measure'] = ing[2].strip()
                        temp_list.append(ingr_dicht)
                f.readline()
                cook_book[dishes] = temp_list          

pprint(cook_book)