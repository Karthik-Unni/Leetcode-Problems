### Q: Find the missing number(s) in array of range [1..N] (sometimes 2 missing)
Soln: 
def find_number(arr, n):
    present = [False] * (n + 1)

    for num in arr:
        present[num] = True

    missing = []

    for i in range(1, n + 1):
        if not present[i]:
            missing.append(i)

    return missing      (This is the missing of two numbers in an array .If its just a number 
    missing we can take the sum and compare and then solve)


### Q: Check if array contains duplicates
    def duplicates(arr):
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return True
        return False
    
    arr=[4,5,6,4]
    print(duplicates(arr))

  Alt: Also we can make it one liner by just checking the length of the original and by including it in the set.

    def duplicates(arr):
      seen = set()
  
      for num in arr:
          if num in seen:
              return True
          seen.add(num)
  
      return False
  
  
### Q: Kth largest element : Brute force 
      def k_largest(arr,k):
    temp=[]
    ans=[]
    for num in arr:
        temp.append(num)
        if len(temp)<k:
            ans.append(-1)
        else:
            temp.sort
            ans.append(temp[-k])
    return ans
Heap:
    import heapq
    
    def kth_largest(arr, k):
        heap = []
        for num in arr:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)   # discard the smallest, keep only top k
        return heap[0]   # smallest of the k largest = the kth largest


    

