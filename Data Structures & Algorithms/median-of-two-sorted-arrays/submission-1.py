class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n =len(nums1)
        m =len(nums2)
        (c,i,j)=([],0,0)

        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                c.append(nums1[i])
                i+=1
            else:
                c.append(nums2[j])
                j+=1

        while i<n:
            c.append(nums1[i])
            i+=1

        while j<m:
            c.append(nums2[j])
            j+=1

        if len(c)%2!=0:
            mid =len(c)//2
            return c[mid]/1

        else:
            mid =len(c)//2
            return (c[mid-1]+c[mid])/2