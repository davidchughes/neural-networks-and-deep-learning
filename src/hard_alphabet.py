
HardChars = [
['O','1','2','3','4','5','6','7','8','9'],  # 0 = "O" to prevent the dot or slash inside the 0 in all fonts
['Z','1','2','J','4','X','K','7','V','N'],  # 1st set of commonly confused chars
['L','1','2','J','S','5','6','T','8','9'],  # 2nd
['O','U','C','3','G','B','6','E','8','9']]  # 3rd

def num_to_chars(num, group = 0):
  return HardChars[group][num]
