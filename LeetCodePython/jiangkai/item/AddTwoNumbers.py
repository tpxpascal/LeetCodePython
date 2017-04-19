# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        num1 = l1
        num2 = l2
        flag = 0
        result = None
        index = result
        while ((num1 != None) or (num2 != None) or (flag > 0)):
            val1 = 0
            val2 = 0
            if num1 != None:
                val1 = num1.val
            if num2 != None:
                val2 = num2.val
                
            value = val1 + val2 + flag
            curVal = value % 10
            flag = value / 10
            
            if result == None:
                result = ListNode(curVal)
                index = result
            else:
                index.next = ListNode(curVal)
                index = index.next
                
            if(num1 != None):
                num1 = num1.next
            if(num2 != None):
                num2 = num2.next
        return result  

def generateList(numbers):
    result = None
    index = None
    for number in numbers:
        if result == None:
            result = ListNode(number)
            index = result
        else:
            index.next = ListNode(number)
            index = index.next
    return result

def printList(list):
    index = list
    while index != None:
        print index.val,
        index = index.next
    print
        
if __name__ == '__main__':
    print "Module Test start."        
    list1 = generateList([1, 2, 3])
    list2 = generateList([4, 5, 6])
    list3 = generateList([7, 8, 9])
    
    item = Solution()
    
    result1 = item.addTwoNumbers(list1, list2)
    result2 = item.addTwoNumbers(list2, list3)
    result3 = item.addTwoNumbers(list3, list1)
    
    printList(result1)
    printList(result2)
    printList(result3)
