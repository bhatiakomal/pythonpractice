CAPACITY=5
class Heap:
    def __int__(self):
        self.heap=[0]*CAPACITY
    def __init__(self):
        self.heap=[0]*CAPACITY
        self.heap_size=0
    def insert(self,item):
        if CAPACITY==self.heap_size:
            return
        self.heap[self.heap_size]=item
        self.heap_size=self.heap_size+1
        #we insert items at the end so there maybe some Voilations
        self.fix_up(self.heap_size-1)
    def fix_up(self,index):
        parent_index=(index-1)//2
        #if parent is smaller than the childern then
        if index>0 and self.heap[index]>self.heap[parent_index]:
            self.swap(index,parent_index)
            self.fix_up(parent_index)
    def swap(self,index1,index2):
        self.heap[index2],self.heap[index1]=self.heap[index1],self.heap[index2]
    def get_max(self):
        return self.heap[0]
    #Remove Maximum Item and retrun max item
    def poll(self):
        max=self.get_max()
        self.swap(0,self.heap_size-1)
        self.heap_size=self.heap_size-1
        self.fix_down(0)
        return max
    def fix_down(self,index):
        index_left=2*index+1
        index_right=2*index+2
        index_largest=index
        #If left child is greater than parent:Largest node is left node
        if index_left<self.heap_size and self.heap[index_left]>self.heap[index]:
            index_largest=index_left
        #if right child is greater than left child:Largest child is the right child
        if index_right<self.heap_size and self.heap[index_right]>self.heap[index_largest]:
            index_largest=index_right
    #If we dont want swap  items themselves:
        if index!=index_largest:
            self.swap(index,index_largest)
            self.fix_down(index_largest)
    def heap_sort(self):
        size=self.heap_size
        for i in range(0,size):
            max=self.poll()
            print(max)
if __name__=="__main__":
    heap=Heap()
    heap.insert(12)
    heap.insert(-12)
    heap.insert(100)
    heap.insert(32)
    heap.insert(0)
    heap.heap_sort()