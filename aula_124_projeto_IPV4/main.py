from classes import Ip


def main():
    ip1 = Ip('192.168.0.128')
    ip1.ip_splitter()
    print(ip1.ip_x_list)
    ip1.bin_block_creator()


if __name__ == '__main__':
    main()