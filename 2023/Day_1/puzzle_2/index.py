file = open("input.txt").read().strip()

G_ARRAY = []

for line in file.split('\n'):
  num = ''
  for item, calibration in enumerate(line):
    if calibration.isdigit():
      num += calibration
    for data, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[item:].startswith(value):
        num += str(data + 1)

  final_num = str(num[0]) + str(num[-1])
  G_ARRAY.append(int(final_num))
  final_num = ''

print(sum(G_ARRAY))
