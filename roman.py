
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
num_rom_list = []
#check input
# I=1,V=5,X=10,L=50,C=100,D=500,M=1000
# IV	4
# IX	9
# XL	40
# XC	90
# CD	400
# CM    900

#roman to number
if user_input.isalpha():
    for i in a:
        for rom, num in roman_list.iteritems():
            if i == rom:
                b = int(num)
                rom_num_list.append(b)
            else:
                pass
    length = len(rom_num_list)
    total = rom_num_list[0]
    if length > 1:
        for j in range(1,len(rom_num_list)):
            total = total + int(rom_num_list[j])
            if rom_num_list[j-1] < rom_num_list[j]:
                cal = rom_num_list[j] - rom_num_list[j-1]
                total = total - rom_num_list[j] - rom_num_list[j-1]
        overall = total + cal
    else:
        overall = b
    print overall

#NUMBER TO ROMAN
elif user_input.isdigit() and int(user_input) < 5000:
    if int(user_input) in roman_list.values():
        for rom, num in roman_list.iteritems():
            if int(user_input) == num:
                b = rom
    else:
        for i in a:
            rom_num_list.append(i)
    if len(num_rom_list) > 1:
        num_input = int(''.join(rom_num_list))
        for i in range(1,1000):
            if int(num_input) - 1000 >= 0:
                num_rom_list.append("M")
                num_input = num_input - 1000
            elif int(num_input) - 900 >= 0:
                num_rom_list.append("CM")
                num_input = num_input - 900
            elif num_input - 500 >=  0 :
                num_rom_list.append("D")
                num_input = num_input - 500 
            elif int(num_input) - 400 >= 0:
                num_rom_list.append("CD")
                num_input = num_input - 400
            elif num_input - 100 >= 0:
                num_rom_list.append("C")
                num_input = num_input - 100
            elif int(num_input) - 90 >= 0:
                num_rom_list.append("XC")
                num_input = num_input - 90
            elif num_input - 50 >= 0:
                num_rom_list.append("L")
                num_input = num_input - 50
            elif int(num_input) - 40 >= 0:
                num_rom_list.append("XL")
                num_input = num_input - 40
            elif num_input - 10 >= 0:
                num_rom_list.append("X")
                num_input = num_input - 10
            elif int(num_input) - 9 >= 0:
                num_rom_list.append("IX")
                num_input = num_input - 9
            elif num_input - 5 >= 0:
                num_rom_list.append("V")
                num_input = num_input - 5
            elif int(num_input) - 4 >= 0:
                num_rom_list.append("IV")
                num_input = num_input - 4
            elif num_input - 1 >= 0:
                num_rom_list.append("I")
                num_input = num_input - 1
            elif num_input == 0:
                break
            else:
                pass
        print ''.join(num_rom_list)
    else:
        print b
else:
    print "Invalid input~"