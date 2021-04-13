def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    select_num(arr)
    print(arr)

def select_num(arr):
    num = int(input("Please enter your number: "))
    x = arr.count(num)

    if  x == 1:
        print('Your number appears',x,"time")
    elif x > 1:
        print("Your number appears",x,"times")
    else:
        print("Sorry, that number doesn't appear in this list")
    
    
bubble_sort([34, 2, 10, 6, 7, 5, 1, 5])