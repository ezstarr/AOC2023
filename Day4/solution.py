with open('input.txt') as file:
  strings: list[str] = [line.strip() for line in file]

total= 0
total_matches = []
arr_cards = []

for string in strings:
  card, numbers = string.split(':')
  win_nums, have_nums = numbers.split('|')
  win_list = win_nums.split()
  have_list = have_nums.split()

  # check if have_list is in win_nums.
  points = 1
  line_match_list = []
  for num in have_list:
    if num in win_list:
      line_match_list.append(num)
  
  # list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

  num_of_matches = len(line_match_list)
  # print(line_match_list)
  for point in range(len(line_match_list)):

    # print(point)
    points *=2
  points //= 2

  # print(f"points: {points}")
  new_pts = 0
  int_points = int(points)
  # print(int_points)
  total += int_points
  # print(f"length: {len(line_match_list)}")
  total_matches.append(len(line_match_list))

# print(total)
# print(total_matches)


  arr_cards.append(1)

matches = total_matches #  [4, 2, 2, 1, 0, 0]
print("arr_cards: ", arr_cards)
print("matches: ", matches)

for i, card in enumerate(arr_cards):
  print("i: ", i)
  print(arr_cards)
  for j in range(matches[i]):  
    print("j: ", j)
    
    # for each value in matches, add 1 to the next value in arr_cards
    arr_cards[j+i+1] += arr_cards[i]


""" if j works for i of 0, but is off for i of 1, what could we add to fix that?
we already have two copies of the second card, so we need to add it twice, one for each copy
"""

    # num_of_copies = matches[i] 
    # arr_cards[i+1] += 1

ar = [1, 2, 2, 2, 2, 1, 1]  # i = index of array

matc =[4, 2, 2, 1, 1, 0, 0]   # j = iterating through index of cards

total_cards = 0
for card in arr_cards:
  total_cards += card
print(total_cards)
