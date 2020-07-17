game_list=[0,1,2]
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)
display_game(game_list)

def position_choice():
    choice='wroong'
    while choice not in ['0','1','2']:
        choice=input("Pick a position (0,1,2):")
        if choice not in ['0','1','2']:
            print("Sorry,invalid choice")
    return int(choice)
rslt=position_choice()
print(rslt)

def replacement_choice(game_list,position):
    user_placement=input("Type a string to take a position: ")
    game_list[position]=user_placement
    return game_list
rslt=replacement_choice(game_list,1)
print(rslt)

def gameon_choice():
    choice='wroong'
    while choice not in ['Y','N']:
        choice=input("Keep playing ('Y','N') ")
        if choice not in ['Y','N']:
            print("Sorry,I do not understand ,please choose Y or N")
    if choice=='Y':
        return True
    else:
        return False
rslt=gameon_choice()
print(rslt)