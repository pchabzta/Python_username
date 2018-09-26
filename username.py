import random
import os


def get_usrn_sub_prefix_string():
    # char_str = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char_str = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(char_str)
    fd1 = random.choice(char_str)
    random.shuffle(char_str)
    fd2 = random.choice(char_str)

    # sd = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    sd = str(random.randint(0, 9))
    ref_str = fd1 + sd + fd2

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

    sd = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    ref_str = fd1 + sd + fd2

    return ref_str


def set_environ_var():
    os.environ['SECRET_KEY'] = '75#^koi!0f__)fr2_3x#4qoatbv0wgp=+4(msc12!cav)gv@3&'


def test__file__():
    import os

    # print(__file__)
    # print(os.path.join(os.path.dirname(__file__)),'...')
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(os.path.abspath(os.path.dirname(__file__)))

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # # print(BASE_DIR)
    # print('os.path.dirname(os.path.dirname(os.path.abspath(__file__))): ',
    #       os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # # print('__file__: ',__file__)
    # print('os.path.dirname(os.path.dirname(os.path.abspath(__file__))): ',os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # print('os.path.abspath(__file__): ',os.path.abspath(__file__))
    # print('os.path.abspath(__file__):',os.path.abspath(__file__))
    # print('os.path.dirname(os.path.abspath(__file__)): ',os.path.dirname(os.path.abspath(__file__)))
    # print('os.path.dirname(__file__): ', os.path.dirname(__file__))
    #
    # print('os.path.dirname(os.path.abspath(__file__): ',os.path.dirname(os.path.abspath(__file__)))
    # --------------------------------------------------------------
    # import sys
    # sys.path.insert(2, "/home/myname/pythonfiles")

    # import sys
    # print('sys.path:',sys.path)
    # p = sys.path
    # for i in p:
    #     print(p)

    cwd = os.getcwd()
    myapp_directory = cwd + '\myappdir'
    print(myapp_directory)

    import sys
    cwd = os.getcwd()
    print('cwd: ',cwd)
    ncwd = os.path.dirname(cwd)
    print('ncwd: ', ncwd)
    new_dir = ncwd + '\Python_USR_PW'
    print('new_dir:', new_dir)
    sys.path.insert(0, new_dir)
    print('sys.path[0]: ',sys.path[0])



if __name__ == '__main__':
    # print(get_usrn_sub_prefix_string())
    print(get_pw_string())

    set_environ_var()

    print(os.environ.get('SECRET_KEY'))

    test__file__()
