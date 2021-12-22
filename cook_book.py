from pprint import pprint

cook_book = {}

with open('recipes.txt', encording='UTF-8') as f:
  for line in f:
    name = line.strip()
    quantity = int(file.readline().strip())
    ingr_dict = {}
    dish = []
    for ingredients in range(quantity):
      ing = f.readline().split('|')
      ingr_dicht['ingr_name'] = ing[0].strip()
      ingr_dicht['quantity'] = ing[1].strip()
      ingr_dicht['measure'] = ing[2].strip()
      dish.append(ingr_dicht)
  f.readline()
  cook_book[name] = dish
pprint(cook_book)
