G_ARRAY: list[int] = []
  
with open('input.txt', 'r') as f:
  calibration: str = f.readlines();
  for word in calibration:
    num: str = '';
    final_num: str = '';
    for letter in word:
      if ( letter.isdigit() ):
        num += letter;
    final_num = num[0] + num[-1]
    G_ARRAY.append(int(final_num));
  f.close()

print(G_ARRAY)
print(sum(G_ARRAY))
