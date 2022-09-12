"""
Return the sorted version of the list using a quicksort
You must use the first value in a given list as the pivot.
For example, if list was [2,3,1], then the pivot would be the value 2
"""

list = [2,1,45,6,4,99,11]


def sort(list):
    if len(list) <= 1:
        return list
    less = []
    greater = []
    pivot = list[0]

    for x in list:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
    return sort(less) + [pivot] + sort(greater)


