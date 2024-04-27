from hashed_bloomfilter import*

# check email by hashing it using same hash functions to determine if it is spam or not.
def new_mail_check(mail,bloom):
    size=bloom_size(spam_data_)
    
    hash_match=0

    mail=format_input(mail)

    hash_value_1 = hash_fun_01(mail,size)
    hash_value_2 = hash_fun_02(mail,size)
    hash_value_3 = hash_fun_03(mail,size)
 
    if bloom[hash_value_1]==1:
        hash_match+=1
 
    if bloom[hash_value_2]==1:
        hash_match+=1

    if bloom[hash_value_3]==1:
        hash_match+=1
      
    num_hash_func=3

    if hash_match==num_hash_func:   
        print("\nThis email is SPAM!")
    else:
        print("\nThis email is not spam.")


def start_app(): # Main function which takes input from user and classify the email accordingly.
    option=0
    print("Welcome to Spam Email Classifier!")
    while option!=3:
        # Creates the menu for the user to choose from accordingly.
        option=(input("\nChoose an option:\n1.Check single email \n2. Check multiple emails \n3. Exit \n"))
        while option not in ["1", "2", "3" ] :
            print("\nInvalid input. Please specify '1','2' or '3'")
            option=(input("\nChoose an option:\n1.Check single email \n2. Check multiple emails \n3. Exit \n"))
        
        option=int(option)
        if option == 1: #Check Single email
            while True:
                mail=str(input("\nInput the file here that you want to check \n"))
                try:
                    with open(mail) as f:
                        lines = f.readlines()
                        if len(lines)==0:
                            print("\nNo email found!")
                            break
                        elif len(lines) > 1:
                            print("\nMultiple emails found in this file. Select option 2 to check multiple emails.")
                            break
                        else:
                            mail = lines[0].strip()
                            new_mail_check(mail,bloom)
                            break
                except FileNotFoundError:
                    print("\nFile not found. Make sure that you provide the correct file path.")

        if option == 2:  #Check multiple emails
            while True:
                user_input=str(input("\nInput the file here that you want to check. \n"))
                try:
                    with open(user_input) as f:
                        lines = f.readlines()
                        if len(lines)==0:
                            print("\nNo email found!")
                            break
                        else:
                            for line in lines:
                                line = line.strip() 
                                line = line.split(",") 
                                new_mail_check(line[0],bloom)
                            break
                except FileNotFoundError:
                    print("\nFile not found. Make sure that you provide the correct file path.")
        if option == 3: # Exit the program
            return

start_app()

# Copy paste these files to check emails by giving them as input in terminal 
# Single mail 1.txt       #Not spam
# Single mail 2.txt       #Not spam
# Multiple Emails 1.txt   #All are spam
# Multiple Emails 2.txt   #spam, not spam, spam, spam, not spam, spam, spam
# Multiple Email 3.txt    #empty
