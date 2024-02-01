input_str = input()

count_G = 0 if 'G' not in input_str else input_str.count('G')
count_Y = 0 if 'Y' not in input_str else input_str.count('Y')
count_R = 0 if 'R' not in input_str else input_str.count('R')

if count_G >= 4:
    print("rahat baash")
elif (count_Y == 2 and count_R == 2) or count_R >= 3 or count_G == 0:
    print("nakhor lite")
else:
    print("rahat baash")