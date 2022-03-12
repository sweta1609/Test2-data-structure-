import math 


class Node: 
    def _init_(self, data): 
        self.data = data 
        self.next = None
        
def deleteAlternateNodes(head): 
    if (head == None):
        return

    
    prev = head 
    now = head.next

    while (prev != None and now != None): 
        
        
        prev.next = now.next

        
        now = None

        
        prev = prev.next
        if (prev != None): 
            now = prev.next
def push(head_ref, new_data): 
    
     
    new_node = Node(new_data)

    
    new_node.data = new_data 

     
    new_node.next = head_ref 

    
    head_ref = new_node 
    return head_ref
