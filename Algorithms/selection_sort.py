def selection_sort(arr):

    for i in range(len(arr)):   
        min_index = i 


        for j in range(i+ 1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j;  

        arr[i], arr[min_index] = arr[min_index], arr[i] 

    print(arr)
    print("The largest value is £",arr[0])
   
selection_sort([150.00, 200.00, 154.98, 335.01, 475.12, 558.87, 216.38])