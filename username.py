import random


def get_usrn_sub_prefix_string():
    # char_str = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char_str = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(char_str)
    fd1 = random.choice(char_str)
    random.shuffle(char_str)
    fd2 = random.choice(char_str)

    # sd = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    sd = str(random.randint(0, 9))
    ref_str = fd1 + sd+fd2

    return ref_str

def get_pw_string():
    # char_str = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char_str = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(char_str)
    fd1 = random.choice(char_str)
    random.shuffle(char_str)
    fd2 = random.choice(char_str)

    random.shuffle(char_str)
    fd3 = random.choice(char_str)
    # sd = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    sd = str(random.randint(0, 9)) + str(random.randint(0, 9)) +str(random.randint(0, 9))+str(random.randint(0, 9)) + str(random.randint(0, 9)) +str(random.randint(0, 9))
    ref_str = fd1 + sd+fd2

    return ref_str



if __name__ == '__main__':
    # print(get_usrn_sub_prefix_string())
    print(get_pw_string())
