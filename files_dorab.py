dict = {}
with open('1.txt') as file1:
  number1 = 0     
  for line in file1:
    data1 = file1.read().strip()
    number1 = len(data1)
    dict['1.txt'] = number1

with open('2.txt') as file2:
  number2 = 0
  for line in file2:
    data2 = file2.read().strip()
    number2 = len(data2)
    dict['2.txt'] = number2

with open('3.txt') as file3:
  number3 = 0
  for line in file3:
    data3 = file3.read().strip()
    number3 = len(data3)
    dict['3.txt'] = number3
  
s_values = sorted(dict.values())
s_dict = {}
for i in s_values:
  for j in dict.keys():
    if dict(j) == i:
      s_dict[j] = dict[j]
      break

# val1 = s_dict[list(s_dict.keys())[0]]
# val2 = s_dict[list(s_dict.keys())[1]] 
# val3 = s_dict[list(s_dict.keys())[2]]

def get_key(s_dict, value):
  for key, val in s_dict.items():
    if val == value:
      return key
    
file1 = get_key(s_dict, s_dict[list(s_dict.keys())[0]])
file2 = get_key(s_dict, s_dict[list(s_dict.keys())[1]])
file3 = get_key(s_dict, s_dict[list(s_dict.keys())[2]])
  
filenames = [file1, file2, file3]

with open('file.txt', 'w') as outfile:
  for fname in filenames:
    with open(fname) as infile:
      outfile.write(infile.read())

print('file.txt')