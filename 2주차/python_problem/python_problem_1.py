num =0
from random import randint
def check_num():
    while True:
        num_of_nums=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        if not num_of_nums.isdigit():
            print("정수를 입력하세요")
            continue
   

        num_of_nums = int(num_of_nums)
        
        if num_of_nums not in (1,2,3):
            print("1, 2, 3 중 하나를 입력하세요")
            continue


        break
    return(num_of_nums)


def player():
    global num 
    nums=check_num()

    for i in range (num,num+nums):
        print(f"player : {i+1}")
        if i + 1 == 31: 
            print("player wins!")
            break
    num=num+nums


def computer():
    global num 
    nums=randint(1,3)

    for i in range (num,num+nums):
        print(f"computer : {i+1}")
        if i + 1 == 31: 
            print("computer wins!")
            break
    num=num+nums

while num<31:
    computer()
    if num<31:
        
        player()
