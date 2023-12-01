import re

with open('input.txt') as file:
  string_list = [line.strip() for line in file]

# calibration value can be found by combining first digit and LAST digit in that order, to form a single 
# two-digit number.

p1_total = 0

number_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in string_list: 
  line_num = ""
  for i in line:
    if i.isdigit():
      line_num += i
      break
  for i in line[::-1]:
    if i.isdigit():
      line_num += i
      break
  p1_total += int(line_num)
  

print(p1_total)


with open('sample2.txt') as file:
  string_list2 = [line.strip() for line in file]

regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
digit_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six":"6", "seven": "7", "eight": "8", "nine": "9"}


p2_total = 0

for line in string_list:
  print(line)
  line_num2 = ""
  all_matches = re.findall(regex, line)
  print(all_matches)
  if all_matches[0].isdigit():
    line_num2 += all_matches[0]
  if not all_matches[0].isdigit():
    line_num2 += digit_dict[all_matches[0]]
  if all_matches[-1].isdigit():
    line_num2 += all_matches[-1]
  if not all_matches[-1].isdigit():
    line_num2 += digit_dict[all_matches[-1]]
  print(line_num2) 
  int_num2 = int(line_num2)
  p2_total += int_num2
print(p2_total)
