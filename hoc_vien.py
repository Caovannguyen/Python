class HocVien():
    def __init__(self, ma, ten, diem_toan, diem_ly, diem_hoa):
        self.ma = ma
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_diem_trung_binh(self):
        diem_trung_binh = (self.diem_hoa + self.diem_ly + self.diem_toan)/3
        return diem_trung_binh

    def to_string(self):
        # ma = str(self.ma)
        # ten = str(self.ten)
        # diem_toan = str(self.diem_toan)
        # diem_ly = str(self.diem_ly)
        # diem_hoa = str(self.diem_hoa)
        # diem_trung_binh = str(self.tinh_diem_trung_binh())
        return 'ma: %s - ten: %s - diem_toan: %s - diem_ly: %s - diem_hoa: %s - diem_trung_binh: %.2f' %(
            self.ma, self.ten, self.diem_toan, self.diem_ly, self.diem_hoa, self.tinh_diem_trung_binh())

    def write_info_hocvien(self):
        f = open('hocvien.txt', 'a+')
        f.write(self.to_string())

# a = HocVien('1', 'Hoang', 5, 6, 7)
# a.write_info_hocvien()


while True:
    choice = input('Nhap thong tin hv (y/n)?')
    if choice and choice.lower() != 'y':
        break
    code = input('Nhap ma hv')
    name = input('Nhap ten hv')
    toan = float(input('Nhap diem toan'))
    ly = 6.0
    hoa = 7.0
    hv = HocVien(code, name, toan, ly, hoa)
    hv.write_info_hocvien()
