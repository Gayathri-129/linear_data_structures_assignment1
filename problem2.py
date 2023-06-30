
def reverse_array_in_place(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

reverse_array_in_place(arr)
print("Reversed array:", arr)