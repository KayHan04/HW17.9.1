try:
    numbers = list(map(int, input('Введите числа через пробел').split()))
    print(f"Числа введены верно,{numbers}")
except ValueError:
    print('Ввод содержит строку, либо не целое число!')
try:
    num = int(input("Введите число: "))
    print("Введенное число:", num)
except ValueError:
    print("Ввод содержит строку, либо не целое число!")

# print(sorted(numbers))
#################################################

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers[:]
    else:
        middle = len(numbers) // 2
        left = merge_sort(numbers[:middle])
        right = merge_sort(numbers[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(numbers))

###################################################
def binary_search(numbers, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if numbers[middle] == element:
        return middle
    elif element < numbers[middle]:

        return binary_search(numbers, element, left, middle - 1)
    else:
        return binary_search(numbers, element, middle + 1, right)

element = int(input())
numbers = [i for i in range(1, 100)]  # 1,2,3,4,...

print(binary_search(numbers, element, 0, 99))
