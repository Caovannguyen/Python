class HinhChuNhat:

    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
        # return dien_tich

    def chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
        # return chu_vi

    def to_string(self):
        # chieu_rong = str(self.chieu_rong)
        # chieu_dai = str(self.chieu_dai)
        # dien_tich = str(self.dien_tich())
        # chu_vi = str(self.chu_vi())
        # return chieu_rong, chieu_dai, dien_tich, chu_vi
        return 'Chieu rong: %s - chieu dai: %s - chu vi: %s - dien tich: %s' % (
            self.chieu_rong, self.chieu_dai, self.chu_vi(), self.dien_tich())

    def write_info(self):
        f = open('hcn.txt', 'w')
        # for i in self.to_string():
        #     f.write(i + '\n')
        f.write(self.to_string())


# hcn = HinhChuNhat(10, 5)
# hcn.write_info()
# print(hcn.to_string())




