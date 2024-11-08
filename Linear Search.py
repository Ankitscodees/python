import sys

def linear_search(arr, num_find):
    # This function is used to search whether the given
    position = -1
    for index in range(0, len(arr)):
        if arr[index] == num_find:
            position = index
            break

    return (position)

# main code
if __name__=='__main__':
    
    arr = [10, 7, 2, 13, 4, 52, 6, 17, 81, 49]
    num = 52
    found = linear_search(arr, num)
    if found != -1:
        print('Number %d found at position %d'%(num, found+1))
    else:
        print('Number %d not found'%num)
