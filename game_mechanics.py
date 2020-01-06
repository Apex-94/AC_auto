from Character import*

def level_up(self):
    if self.exp >= self.LEVEL_UP:
        self.lvl += 1
        self.LEVEL_UP *= 1.25
        self.LEVEL_UP = int(self.LEVEL_UP)
        self.exp = 0
        stat_choice = input(
            "You have 2 points to spend in your attributes!\nType which attributes you want to raise up: ")
        stat_choice = stat_choice.split(',')
        self.ATTRIBUTES[stat_choice[0]] += 1
        self.ATTRIBUTES[stat_choice[1]] += 1
        self.max_hp = int(self.max_hp * 1.1)
        self.max_mp = int(self.max_mp * 1.1)
        return True
    else:
        return False

def char_Creation():
    def player_name():
        while True:
            #message="Enter your name"
            op = input("Enter your name. ")
            if len(op) == 0:
                print("\nPlease Enter a valid name")
            else:
                confirmation = input("Are you sure you want to keep this name?"
                                     "1 : YES\n"
                                     "2 : NO\n"
                                     "Select your ans : ")
                if confirmation == '1' :
                    return op


    def player_gender():
        while True :
            option = input('\n\n'
                       '(1): Male\n'
                       '(2): Female\n'
                       'Enter A Number:> ')
            if option == '1':
                return 'male'
            elif option == '2':
                return 'female'

    pname = player_name()
    pgender = player_gender()

    def set_attributes():
        #name, hp, kt, level, points
        return Player(
            name=pname,
            hp=100,
            kt=0,
            level=0,
            points=0,
            gender=pgender
        )