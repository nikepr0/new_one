class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=len(head)
        c=0
        while c<l:
            if head[c]<head[c+1]:
                head.swap(c,c+1)
                c+=2
            else:
                c+=1
        return head