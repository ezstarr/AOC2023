import typing 

# with open('sample.txt') as file:
with open('input.txt') as file:
  string_list: list[str] = [line.strip() for line in file]


dict_colors: dict[str, int]= {'red': 12, 'green': 13, 'blue': 14}

id_sum: int = 0

# for raw_line in string_list:
#   name, record = raw_line.split(':')
#   game, record_id = name.split(' ')
#   # print(record)  #  3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#   record_fixed = record.replace(';', ',').strip(' ')
#   color_count = record_fixed.split(', ')
#   # print(color_count)
#   impossible: int = 0
#   for a_color in color_count:
#     count, color = a_color.split(' ')
#     int_count = int(count)
#     if int_count > dict_colors[color]:
#       impossible += 1
#   if impossible == 0:
#     id_sum += int(record_id)
    
    
print(id_sum)

# Part 2

# get the maxiumum count for each color in each record
# multiply the three counts together
# add to sum

power_sum: int = 0


for raw_line in string_list:
  name, record = raw_line.split(':')
  game, record_id = name.split(' ')
  # print(record)  #  3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
  record_fixed = record.replace(';', ',').strip(' ')
  color_count = record_fixed.split(', ')
  # print(color_count)
  impossible: int = 0
  blue_greatest = 0
  red_greatest = 0
  green_greatest = 0
  for a_color in color_count:
    count, color = a_color.split(' ')
    if color == 'blue':
      if int(count) > blue_greatest:
        blue_greatest = int(count)
    if color == 'red':
      if int(count) > red_greatest:
        red_greatest = int(count)
    if color == 'green':
      if int(count) > green_greatest:
        green_greatest = int(count)
  record_power = blue_greatest * red_greatest * green_greatest
  power_sum += record_power

print(power_sum)





  # for line_ in new:
    
  #   line_ = str(line_)  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
  #   str_no_space = line_.replace(' ', '')
  # # print(str_no_space) # 6red,1blue,3green;2blue,1red,2green
  #   str_no_space_3sets = str(str_no_space).split(';')  # ['3blue,4red', '1red,2green,6blue', '2green']
  #   for one_set in str_no_space_3sets:
  #     one_set_split = one_set.split(',') 
  #     print(one_set_split)










    # num_of_sets = len(str_no_space_sets)
    # print(num_of_sets)
    # 

  #print(str_no_space_sets) # ['3blue,4red', '1red,2green,6blue', '2green']

  # {
  #   {['3', 'blue'], ['4', 'red']}, {['1', 'red']} }


    # set_1: list[str] = str_no_space_sets[0].split(',') # ['3blue', '4red']
    # set_2: list[str] = str_no_space_sets[1].split(',')
    # set_3: list[str] = str_no_space_sets[2].split(',')
  # print("----------1--------")
  # print(set_1)
  # print("-------------2-----")
  # print(set_2)
  # print("-------------3-----")
  # print(set_3)

  #   split_a = a.split(';')
  #   print(split_a)
  #   set_1.append(split_a[0]) 
  #   print(split_a)
  #   set_2.append(split_a[1])
  #   print(split_a)
  #   set_3.append(split_a[2])
  # set_1_split = str(set_1).split(',') # ['3blue,4red']
  # set_2_split = str(set_2).split(',')
  # set_3_split = str(set_3).split(',')
  # count: str = ""
  # for x in set_1_split:
  #   if x.isdigit():
  #     count += x
  # print(count)

"""
['3blue,4red'] => ['3', 'blue], ['4', 'red']

"""
# for index, line in enumerate(string_list):
#   print(line)
#   print(line[index])
#   # line.remove(f'Game: {index+1}:')
#   # print(line)
#   # for deliminator in deliminators:
#   #   result = line.replace(' ', '').split(deliminator)
#   # print(result)