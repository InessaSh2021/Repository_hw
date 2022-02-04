ingr_dict = cook_book('recipes.txt')
def get_list_dishes(dishes, persons=int):
 
  list_dishes = {}
  for dish in dishes:
    for item in ingr_dict[dish]:
      temp_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
      if list_dishes.get(item['ingredient_name']):
        if dish not in list_dishes:
          new_item = (int(list_dishes[item['ingredient_name']]['quantity']) + int(temp_list[item['ingredient_name']]['quantity']))

          list_dishes[item['ingredient_name']]['quantity'] = new_item       
        else:
          list_dishes[item['ingredient_name']]['quantity'] *= persons
      else:
        print('Такого блюда нет')

  print('Нужно купить:', list_dishes)
  print(list_dishes)

get_list_dishes(['Запеченный картофель', 'Омлет'], 2)
