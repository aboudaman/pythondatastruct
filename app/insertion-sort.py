# Insertion Sort Algorithm
# Contains 2 loops, outer and inner
# Outer loops goes through the list
# Inner loop conducts the swap

print("Insertion Sort Algorithm")

def insertion_sort(list):
    n = len(list)
    i = 1
    while i < n:
        current = list[i]
        j = i -1
        while j >= 0 and list[j] > current:
            list[j+1] = list[j]
            j-1



