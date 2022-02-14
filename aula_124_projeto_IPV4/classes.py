class Ip:
    def __init__(self, ip):
        self._ip = ip

    bin_list = [128, 64, 32, 16, 8, 4, 2, 1]
    bin_ip = [[]]
    ip_1 = ''
    ip_2 = ''
    ip_3 = ''
    ip_4 = ''

    ip_1_bin = ''
    ip_2_bin = ''
    ip_3_bin = ''
    ip_4_bin = ''

    ip_x_list = [ip_1, ip_2, ip_3, ip_4]

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    def ip_splitter(self):
        self._ip = list(self._ip)

        for i_x, ip_x in enumerate(self.ip_x_list):
            for i, n in enumerate(self._ip):
                if n == '.':
                    self._ip = self._ip[i + 1:]
                    break
                self.ip_x_list[i_x] += n
        return self.ip_x_list

    def bin_block_creator(self):
        ip_bin_list = [self.ip_1_bin, self.ip_2_bin, self.ip_3_bin, self.ip_4_bin]

        for x_n, ip_x in enumerate(self.ip_x_list):
            for n, i in enumerate(self.bin_list):
                if int(ip_x) > 128:
                    ip_x = int(ip_x) - i
                    ip_bin_list[x_n] += '1'
                elif int(ip_x) == i:
                    ip_bin_list[x_n] += '1'
                elif int(ip_x) < self.bin_list[n - 1] and int(ip_x) > i:
                    ip_x = int(ip_x) - i
                    ip_bin_list[x_n] += '1'
                else:
                    ip_bin_list[x_n] += '0'
            print(f'    {ip_bin_list[x_n]}')

