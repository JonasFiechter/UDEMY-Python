def master(function):
    print('inside_master')
    def slave(*args, **kwargs):
        print('decorated_slave')
        function(*args, **kwargs)
    return slave

@master
def say_hi(msg):
    print(msg)


if __name__ == '__main__':
    say_hi('ARGUMENT FOR say_hi')