class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2) / 2 + 1)
        else:
            return self.getKth(nums1, nums2, (len1 + len2) / 2) * 0.5 + \
                   self.getKth(nums1, nums2, (len1 + len2) / 2 + 1) * 0.5
                    
    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        
        if m > n: return self.getKth(B, A, k)
        if m == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        
        p_A = min(k/2 - 1, m - 1)
        p_B = k - 2 - p_A
        
        if A[p_A] == B[p_B]: return A[p_A]
        elif A[p_A] < B[p_B]: return self.getKth(A[p_A + 1:m], B, k - p_A - 1)
        else: return self.getKth(A, B[p_B + 1:n], k - p_B - 1)
        
    