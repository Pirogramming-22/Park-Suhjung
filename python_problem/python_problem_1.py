num =0
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

def play_a():
    global num 
    nums=check_num()

    for i in range (num,num+nums):
        print(f"playerA : {i+1}")
        if i + 1 == 31: 
            print("playerA win!")
    num=num+nums


def play_b():
    global num 
    nums=check_num()

    for i in range (num,num+nums):
        print(f"playerB : {i+1}")
        if i + 1 == 31: 
            print("playerB win!")
    num=num+nums

while num<31:
    play_a()
    if num<31:
        play_b()
