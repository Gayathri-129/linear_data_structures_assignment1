
def find_pairs(array, target_sum):
    pairs = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                pairs.append((array[i], array[j]))

    return pairs


arr = [2, 4, 6, 8, 10, 7, 5]
target = 12

result = find_pairs(arr, target)
print("Pairs with sum", target, ":")
for pair in result:
    print(pair)