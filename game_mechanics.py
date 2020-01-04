from Character import*

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


    def player_gender(pname):
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
