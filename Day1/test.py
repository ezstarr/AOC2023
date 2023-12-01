import re

with open('sample2.txt') as file:
  string_list2 = [line.strip() for line in file]

word_to_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }


total = 0
for line in string_list2:
    matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    total += int(
        # dict.get()'s 2nd argument is the value that is 
        # returned if the specified key does not exist in the dict

        # if the key for word_to_num doesnt exist, return index 0 of matches.

        word_to_num.get(matches[0]) != matches[0]
        word_to_num.get(matches[0], matches[0]) +
        word_to_num.get(matches[-1], matches[-1])
    )


print(total)

print(word_to_num.get("1", "Default Text"))
# print(matches[0])
# print(word_to_num.get(matches[0], matches[0]))