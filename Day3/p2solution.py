with open('input.txt') as file:
  engine_array: list[str] = [line.strip() for line in file]

# part number = number adjacent to a symbol.
# part number should be included in sum
# sum should be 4361

col_indexes = 0

def find_symbols(arr):
  symbols = []
  symbol_indexes = []
  for i, row in enumerate(arr):
    for k, col in enumerate(row):
      # pass if iter is not a symbol
      if arr[i][k] == '*':
        symbols.append(arr[i][k])
        symbol_indexes.append([i, k])
  return symbol_indexes

def scan_row(a_row, col): # array, row of digit, col of digit
  number_indexes = [] 
  first_number = a_row[col]
  #keep looking left until it's no longer a digit. 
  for i in range(col, -1, -1):
    if a_row[i].isdigit():
      number_indexes.append(i)
    else:
      break
  for i in range(col+1, len(a_row), 1):
    if a_row[i].isdigit():
      number_indexes.append(i)
    else:
      break
  sorted_cols = [i for i in sorted(number_indexes)]
  return sorted_cols

symbol_indexes = find_symbols(engine_array)
print(symbol_indexes)
gear_ratio = 0

for index in symbol_indexes:
  r = index[0]
  c = index[1]
  parts_indexes = set()
  
  # check top:
  if engine_array[r-1][c].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r-1], c)
    for c_ in col_indexes:
      part_index.append((r-1, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)

  # check top-left:
  if engine_array[r-1][c-1].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r-1], c-1)
    for c_ in col_indexes:
      part_index.append((r-1, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)


  # check top-right:
  if engine_array[r-1][c+1].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r-1], c+1)
    for c_ in col_indexes:
      part_index.append((r-1, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)


  # check bottom-right:
  if engine_array[r+1][c+1].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r+1], c+1)
    for c_ in col_indexes:
      part_index.append((r+1, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)


  # check bottom:
  if engine_array[r+1][c].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r+1], c)
    for c_ in col_indexes:
      part_index.append((r+1, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)


  # check bottom-left:
  if engine_array[r+1][c-1].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r+1], c-1)
    for c_ in col_indexes:
      part_index.append((r+1, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)


  # check right:
  if engine_array[r][c+1].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r], c+1)
    for c_ in col_indexes:
      part_index.append((r, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)


  # check left:
  if engine_array[r][c-1].isdigit():  #WORKS
    part_index = []
    col_indexes = scan_row(engine_array[r], c-1)
    for c_ in col_indexes:
      part_index.append((r, int(c_)))
    part_index_tuple = tuple(part_index)
    parts_indexes.add(part_index_tuple)

  if len(parts_indexes) == 2:
    print(parts_indexes)
    gear_products = []
    for each in parts_indexes:
      part_number = ""
      for index in each:
        r = index[0]
        c = index[1]
        part_number += engine_array[r][c]
      gear_products.append(int(part_number))
    multipled = gear_products[0] * gear_products[1]
    gear_ratio += multipled



print(gear_ratio)