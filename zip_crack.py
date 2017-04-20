import zipfile as z

zipFile = z.ZipFile("zipTest.zip")

#get dictionary
def get_passwords(pass_file):
    pass_obj = open(pass_file, 'r')
    pass_list = []

    for word in pass_obj.readlines():
        word      = word.strip('\n')
        pass_list.append(word)
    return pass_list

def generate_chars(iter_len):
    char       =  0
    char_combs = []

    while len(str(char)) <= iter_len:
       char_combs.append(str(char))
       char += 1 
    return char_combs

def main():
    
    passwords      = get_passwords('../password-dictionaries/dictionaries/combinedBACKUP')
    numbers        = generate_chars(3)

    for passwrd in passwords:
        try:
            print "Trying password: " + str(passwrd)
            zipFile.extractall(pwd=passwrd)
        except:
            print "Password failed: " + str(passwrd)
        else:
            print "Password " + str(passwrd) + " was successful!"
            exit()

    for passwrd in passwords:
        for number in numbers:
            try:
                print "Trying password: " + str(passwrd) + str(number)
                zipFile.extractall(pwd=passwrd + str(number))
            except:
                print "Password failed: " + str(passwrd) + str(number)
            else:
                print "Password " + str(passwrd) + str(number) + " was successful!"
                exit()


if __name__ == "__main__":
    main()