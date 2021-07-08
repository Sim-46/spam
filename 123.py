def main():
    key = configini('login')
    print(key)


def configini(name):
    conf = open('config.txt', 'r')
    login = str(conf.readline())
    password = str(conf.readline())
    key = str(conf.read())

    if name == 'login':
        return login
    elif name == 'password':
        return password
    else:
        return key

    conf.close()


if __name__ == '__main__':
    main()
