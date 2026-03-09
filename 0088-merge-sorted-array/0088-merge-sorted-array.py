class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for k in range(len(nums2)):
                nums1[k]=nums2[k]
            return nums1
        elif n==0:
            return nums1
        else:
            i=0;j=0;dummy=[]
            while True:
                if i==m:
                    dummy+=nums2[j:]
                    print(dummy)
                    for m in range(len(dummy)):
                        nums1[m]=dummy[m]
                    return nums1
                elif j==n:
                    len_num1 = len(nums1)-m
                    dummy += nums1[i:]
                    for n in range(len_num1):
                        dummy.pop(-1)
                    for o in range(len(dummy)):
                        nums1[o]=dummy[o]
                    return nums1
                elif nums1[i]<=nums2[j]:
                    dummy.append(nums1[i])
                    i+=1
                else:
                    dummy.append(nums2[j])
                    j+=1

            



        