def bubble_sort(arr:list[int]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            print(f'i:{i} - j:{j}')
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':    
    # Example usage:
    arr = [64, 34, 25, 12, 22, 11, 63]
    bubble_sort(arr)
    print("Sorted array:", arr)


