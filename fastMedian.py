def fastMedian(a1, a2, n):
    
    # Case if there are no elements in array
    if (n == 0):
        return -1
    # Case if there are one element in each array -- taken median
    elif (n == 1):
        return ((a1[0] + a2[1])/2)
    # Case if there are two elements in each array, take the middle two elements and divide for the median
    elif (n == 2): 
        return (max(a1[0], a2[0]) + min(a1[1], a2[1])) / 2
    # Case if the arrays are bigger than 2, begin our divide and conquer operations
    else:  
        m1 = findMedian(a1, n)
        m2 = findMedian(a2, n)
        
        # Time to discard parts of a1 and a2 that cannot be the median
        if (m1 <= m2):
            # if median1 is bigger, take out the bigger half of arr1 and the smaller half of arr2
            # Determine if array is odd or even sized and make recursive call accordingly 
            if n % 2 == 0:
                return fastMedian(a1[int(n/2) - 1:], a2[:int(n/2) + 1], int(n/2 + 1)) 
            else: 
                return fastMedian(a1[int(n/2):], a2[:int(n/2) + 1], int(n/2) + 1)
        else: 
            if n % 2 == 0:
                return fastMedian(a1[:int(n/2) + 1], a2[int(n/2) - 1:], int(n/2) + 1) 
            else: 
                return fastMedian(a1[:int(n/2) + 1], a2[int(n/2):], int(n/2) + 1)
        
### helper function to find median given one array  ###
def findMedian(a, n): 
    if n % 2:
        return ((a[int(n/2 - 1)] + a[int(n/2)])/2);
    else:
        return (int(a[n/2])) 

arrayOne = [1, 4, 6, 8, 10] 
arrayTwo = [2, 6, 9, 12, 15] 

arrayLength = len(arrayOne)
ans = int(fastMedian(arrayOne, arrayTwo, arrayLength))
print(ans)

