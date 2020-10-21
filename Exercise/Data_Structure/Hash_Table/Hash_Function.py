class HashTable:
    def __init__(self):
        self.size=10
        self.keys=[None]*self.size
        self.values=[None]*self.size
    def hsashfunction(self,key):
        sum=0
        for pos in range(0,len(key)):
            sum=sum+ord(key[pos])
        return sum%self.size
    def put(self,key,data):
        index=self.hsashfunction(key)
        #If there any collision occure
        while self.keys[index] is not None:
            if self.keys[index]==key:
                self.values[index]==data #update
                return
            #Rehash try to find another slot
            index=(index+1)%self.size
        #Insert
        self.keys[index]=key
        self.values[index]=data
    def get(self,key):
        index = self.hsashfunction(key)
        # If there any collision occure
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        #It means key is not present in the array
        return None
table=HashTable()
table.put("Apple:",100)
table.put("Orange:",50)
table.put("Lichi:",150)
table.put("Straberry:",200)
table.put("Mango:",110)
print(table.get("Lichi:"))