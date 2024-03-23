def selection_sort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            #print(f'i:{i} - j:{j}')
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("Min is: ",arr[min_index])
    return arr        
    
if __name__ == '__main__':    
    # Example usage:
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print("Sorted array:", arr)