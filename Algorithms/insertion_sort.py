
def insertion_sort(arr):
    for i in range (len(arr)):
        key = arr [i]
        j = i -1

        while(j>=0 and arr[j]>key):
            arr[j+1] =arr[j]
            j = j-1

            arr[j+1] = key
        
    sort_age(arr)
    print(arr)

def sort_age(arr):
    for i in range(len(arr)):
        if arr[i] >=30 and arr[i] <=40:
            print(arr[i])

    


insertion_sort([17, 21, 97, 66, 5, 30, 33, 45, 58, 67, 38,39, 41, 19, 23])