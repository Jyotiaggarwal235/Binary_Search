def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
   
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        return -1
  
arr = []
n=int(input('Enter the size of an array='));
x =int(input('Enter the element to be searched='))
print("Enter elements=")
for i in range(0,n):
    m=int(input())
    arr.append(m)
print(arr)
result = binarySearch(arr, 0, n-1, x) 
if result != -1: 
    print ("Element is present at index % d",result+1) 
else: 
    print ("Element is not present in array") 