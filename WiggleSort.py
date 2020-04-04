import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quickselect(nums, n):
            start = 0
            end = len(nums)-1
            while True:
                pivot = nums[random.randint(start,end)]
                i,j,k = start, end, start
                while k<=j:
                    if nums[k]<pivot:
                        nums[i],nums[k]= nums[k], nums[i]
                        i+=1
                        k+=1
                    elif nums[k]>pivot:
                        nums[k], nums[j] = nums[j], nums[k]
                        j-=1
                    else:
                        k+=1
                if i<=n-1<=j:
                    return pivot
                elif n-1<i:
                    end = i-1
                else:
                    start = i+1
        
        median = quickselect(nums, (len(nums)+1)//2)
        index = lambda i : (1+2*i)%(len(nums)|1)
        i,j,k =0, len(nums)-1, 0
        while k<=j:
            if nums[index(k)]>median:
                nums[index(k)], nums[index(i)] = nums[index(i)], nums[index(k)]
                i+=1
                k+=1
            elif nums[index(k)]<median:
                nums[index(k)], nums[index(j)] = nums[index(j)], nums[index(k)]
                j-=1
            else:
                k+=1
                