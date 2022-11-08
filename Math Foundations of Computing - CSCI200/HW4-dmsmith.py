'''
Dean Smith
CSCI 200: Math Foundations
Prof. Dickerson
2/28/2022

The following program recursiely adds all the subsets of a given size k into the list
"subsets" which is then returned by the funciton "get_subsets".

Inputs:
- input_array: type: list which is the array of values input by the user.
- k: type: int which is the size of the subsets added to the list subsets

'''

subsets = []

def get_subsets(input_array, k):
    
    if len(input_array) == k:
        if not(input_array in subsets):
            subsets.append(input_array)
    else:
        new_array = []
        for i in range(len(input_array)):
            new_array = input_array[:i] + input_array[i + 1:] 
            get_subsets(new_array, k)

    return subsets


# Using function in practice and printing the subsets to the console.
print(get_subsets(['a','b','c','d'], 2))







    