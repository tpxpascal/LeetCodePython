# coding=utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        loop1 = (x for x in nums1)
        loop2 = (y for y in nums2)
        
        size1 = len(nums1)
        size2 = len(nums2)
        total = size1 + size2
        length = 0
        flag = 0
        if total % 2 == 1:
            length = (total + 1) / 2
            flag = 1
        else:
            length = total / 2 + 1
            flag = 0
        
        flag1 = 0
        flag2 = 0
        
        content = []
        a = loop1.next()
        b = loop2.next()    
        for index in range(length):
            if ((a < b) and (flag1 == 0)) or (flag2 == 1):
                content.append(a)
                try:
                    a = loop1.next()
                    continue
                except (StopIteration):
                    flag1 = 1
                    b = loop2.next()
                    continue
            if ((a >= b) and (flag2 == 0)) or (flag1 == 1):
                content.append(b)
                try:
                    b = loop2.next()
                    continue
                except (StopIteration):
                    flag2 = 1
                    a = loop1.next()
                    continue
        if flag == 1:
            return content[-1]
        else:
            return (content[-1] + content[-2]) / 2.0
        
if __name__ == '__main__':
    print "Module Test start."
    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [1, 2, 3, 6]
    list4 = [7, 8, 9, 10]
    list5 = [1, 2]
    list6 = [1, 2, 3]
    item = Solution()
    
    print item.findMedianSortedArrays(list1, list2)
    print item.findMedianSortedArrays(list3, list4)
    print item.findMedianSortedArrays(list5, list6)
