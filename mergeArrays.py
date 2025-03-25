def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        pos=m
        p2=0
        while p2<n:
            nums1[pos]=nums2[p2]
            p2+=1
            pos+=1
        nums1.sort()
        return nums1
        
