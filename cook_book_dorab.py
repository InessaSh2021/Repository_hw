def cook_book():
    with open('recipes.txt', encoding='cp1251') as file:
      dish_list = []
      ingr_dict = {}        
      for line in file.read().strip():             
        dish = line.strip()
        dish_list.append(dish)
        num = int(file.readline().strip())
        for dish in dish_list:
          name, _, *arguments = line.split('\n')
          temp_list = []
          for argument in arguments:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, argument.split(' | '))
            temp_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            ingr_dict[dish] = temp_list        
    return dish_list, ingr_dict 