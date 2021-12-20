def get_shop_list_by_dishes(dishes, person_count):
  cooking_list = {}  
  for dish in dishes:
    if dish in cook_book:
      print(dish)
      for ingr in cook_book[dish]:
        if ingr['ingr_name'] not in cooking_list:
          val = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
          cooking_list[ingr['ingr_name']] = val
        else:
          cooking_list[ingr['ingr_name']]['quantity'] += int(ingr['quantity']) * person_count
  return(cooking_list)
print(get_shop_list_by_dishes(['ќмлет', 'ќмлет'], 2))