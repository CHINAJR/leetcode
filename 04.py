class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        if n % 2 == 1:
        	return findkth(nums1,nums2,0,0,n//2+1)
        else:
        	return (findkth(nums1,nums2,0,0,n//2)+findkth(nums1,nums2,0,0,n//2+1))/2

def findkth(num1,num2,starta,startb,k):
    	n1 = len(num1)
    	n2 = len(num2)

    	if starta >= n1:
    		return num2[startb+k-1]

    	if startb >= n2:
    		return num1[starta+k-1]

    	if k == 1:
    		return min(num1[starta],num2[startb])

    	mid = k//2-1
    	#print(mid)
    	#print(num1[starta+min(mid,n1-mid)])
    	#print(num2[startb+min(mid,n2-mid)])
    	if starta + mid >= n1:
    		k1 = num1[-1]
    		a1 = k-n1
    	else:
    		k1 = num1[starta+mid]
    		a1 = k-k//2
    	if startb + mid >= n2:
    		k2 = num2[-1]
    		a2 = k-n2
    	else:
    		k2 = num2[startb+mid]
    		a2 = k-k//2
            



    	if k1 > k2 :
    		startb = k//2+startb
    		#print(22222)
    		return findkth(num1,num2,starta,startb,a2)

    	else:
    		starta = k//2+starta
    	return findkth(num1,num2,starta,startb,a1)
