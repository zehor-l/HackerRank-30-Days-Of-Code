
    def removeDuplicates(self,head):
        #Write your code here
        if (head == None or head.next == None):
            return head
        if head.data == head.next.data:
            head.next = head.next.next;
            self.removeDuplicates(head)
        else:
            self.removeDuplicates(head.next)
        return head;