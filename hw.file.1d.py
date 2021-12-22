Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт



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