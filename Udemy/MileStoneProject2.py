#Card Class
values={'two':2,'Three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'Ace':14}
class card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.values=values[rank]
    def __str__(self):
        return self.rank+" of "+self.suit
three_of_clubs=card('clubs','Three')
two_hearts=card('hearts','two')
print(two_hearts)

print(values[two_hearts.rank])
print(two_hearts.values<three_of_clubs.values)