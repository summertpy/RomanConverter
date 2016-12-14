
roman_list = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

user_input = raw_input("input: ")
a = list(user_input)
rom_num_list = []
total = 0
cal = 0
for i in a:
    for rom, num in roman_list.iteritems():
        #roman to number
        if user_input.isalpha() and i == rom:
            b = int(num)
            rom_num_list.append(b)
        #NUMBER TO ROMAN
        elif user_input.isdigit() and int(i) == num:
            b = rom
            rom_num_list.append(b)
        else:
            pass
print rom_num_list
length = len(rom_num_list)
#roman to number
if user_input.isalpha():
    if length > 1:
        if not length % 2 == 0:
            rom_num_list.append(0)
        for j in range(1,len(rom_num_list),2):
            print j
            if rom_num_list[j] == 0:
                total = total + rom_num_list[j-1]
                print "total1: " + str(total)
            elif rom_num_list[j-1] >= rom_num_list[j]:
                total = total + rom_num_list[j-1] + rom_num_list[j]
                print "total2: " + str(total)
            elif rom_num_list[j-1] < rom_num_list[j]:
                cal = cal + int(rom_num_list[j]) - int(rom_num_list[j-1])
                print "total3: " + str(cal)
            else:
                print "not in condition"
            overall = total + cal
    else:
        overall = b
elif user_input.isdigit():
    if length >= 2:
        overal = 1+1
    else:
        overall = b
                  
print overall

