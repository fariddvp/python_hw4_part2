import os
from src.bubble_sort import bubble_sort

def main():

    input_list = []
    input_list = list(map(int, input('Enter your list of numbers and split them with space: ').split(' ')))

    PATH = '/home/farid/Documents/hw4/python_hw4_part2/src/input_file.txt'
    PATH2 = '/home/farid/Documents/hw4/python_hw4_part2/src/sorted_file.txt'


    if not os.path.exists(PATH):
        with open(PATH, 'w+') as file:
            pass
    
    with open(PATH, 'a') as w:
        for num in input_list:
            w.write(str(num) + '\n')

    with open(PATH, 'r') as r:
        ary = [int(line.strip()) for line in r.readlines()]
        

    if not os.path.exists(PATH):
        with open(PATH2, 'w+') as ff:
            pass
    sorted_list = bubble_sort(ary)
    with open(PATH2, 'a') as ww:
        for item in sorted_list:
            ww.write(str(item) + '\n')
        print('Your numbers sorted and save in sorted_file.txt: ')
    
    with open(PATH2, 'r') as rr:
        ary2 = [int(lines.strip()) for lines in rr.readlines()]
        print(ary2)

main()