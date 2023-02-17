class tinhlaixuat:
    phantram = 0.01
    def tienlaihangthang(self, tienvay, laixuat, thoigianvay):
        print(f'Lãi xuất năm: {laixuat} %')
        print(f'Lãi xuất tháng: {laixuat/thoigianvay} %')
        print(f'Thời gian vay: {thoigianvay} Tháng')
        ttv = [p for p in str(tienvay)]
        if len(ttv) == 8:
            ttv.insert(2, '.')
            ttv.insert(6, '.')
            tv = ''.join(ttv)
            print(f'Số tiền vay : {tv} VND')
        elif len(ttv) == 7:
            ttv.insert(1, '.')
            ttv.insert(5, '.')
            tv = ''.join(ttv)
            print(f'Số tiền vay : {tv} VND')
        elif len(ttv) == 6:
            ttv.insert(3, '.')
            tv = ''.join(ttv)
            print(f'Số tiền vay : {tv} VND')
        elif len(ttv) == 5:
            ttv.insert(2, '.')
            tv = ''.join(ttv)
            print(f'Số tiền vay : {tv} VND')

        print('-' * 20)

        goc = tienvay / thoigianvay
        goc = int(goc)
        list_a = [j for j in str(goc)]
        if len(list_a) == 8:
            list_a.insert(2, '.')
            list_a.insert(6, '.')
            tgoc = ''.join(list_a)
            print(f'Tiền góc phải đóng: {tgoc} VND/Tháng')
        elif len(list_a) == 7:
            list_a.insert(1, '.')
            list_a.insert(5, '.')
            tgoc = ''.join(list_a)
            print(f'Tiền góc phải đóng: {tgoc} VND/Tháng')
        elif len(list_a) == 6:
            list_a.insert(3, '.')
            tgoc = ''.join(list_a)
            print(f'Tiền góc phải đóng: {tgoc} VND/Tháng')
        elif len(list_a) == 5:
            list_a.insert(2, '.')
            tgoc = ''.join(list_a)
            print(f'Tiền góc phải đóng: {tgoc} VND/Tháng')



        lai = (tienvay * (laixuat * tinhlaixuat.phantram)) / thoigianvay
        lai = int(lai)
        list_b = [i for i in str(lai)]
        if len(list_b) == 8:
            list_b.insert(2, '.')
            list_b.insert(6, '.')
            tlai = ''.join(list_b)
            print(f'Lãi xuất phải đóng: {tlai} VND/Tháng')
        elif len(list_b) == 7:
            list_b.insert(1, '.')
            list_b.insert(5, '.')
            tlai = ''.join(list_b)
            print(f'Lãi xuất phải đóng: {tlai} VND/Tháng')
        elif len(list_b) == 6:
            list_b.insert(3, '.')
            tlai = ''.join(list_b)
            print(f'Lãi xuất phải đóng: {tlai} VND/Tháng')
        elif len(list_b) == 5:
            list_b.insert(2, '.')
            tlai = ''.join(list_b)
            print(f'Lãi xuất phải đóng: {tlai} VND/Tháng')

        tst = goc + lai
        tstd = [t for t in str(tst)]
        if len(tstd) == 8:
            tstd.insert(2, '.')
            tstd.insert(6, '.')
            ttd = ''.join(tstd)
            print(f'TST Đóng/Tháng: {ttd} VND')
        elif len(tstd) == 7:
            tstd.insert(1, '.')
            tstd.insert(5, '.')
            ttd = ''.join(tstd)
            print(f'TST Đóng/Tháng: {ttd} VND')
        elif len(tstd) == 6:
            tstd.insert(3, '.')
            ttd = ''.join(tstd)
            print(f'TST Đóng/Tháng: {ttd} VND')
        elif len(tstd) == 5:
            tstd.insert(2, '.')
            ttd = ''.join(tstd)
            print(f'TST Đóng/Tháng: {ttd} VND')

        print('-'*20)

        coverg = int(goc / 30)
        list_g = [g for g in str(coverg)]
        if len(list_g) == 8:
            list_g.insert(2, '.')
            list_g.insert(6, '.')
            gocn = ''.join(list_g)
            print(f'Tiền góc phải đóng {gocn} VND/Ngày')
        elif len(list_g) == 7:
            list_g.insert(1, '.')
            list_g.insert(5, '.')
            gocn = ''.join(list_g)
            print(f'Tiền góc phải đóng {gocn} VND/Ngày')
        elif len(list_g) == 6:
            list_g.insert(3, '.')
            gocn = ''.join(list_g)
            print(f'Tiền góc phải đóng {gocn} VND/Ngày')
        elif len(list_g) == 5:
            list_g.insert(2, '.')
            gocn = ''.join(list_g)
            print(f'Tiền góc phải đóng {gocn} VND/Ngày')
        elif len(list_g) == 4:
            list_g.insert(1, '.')
            gocn = ''.join(list_g)
            print(f'Tiền góc phải đóng {gocn} VND/Ngày')

        coverl = int(lai / 30)
        list_l = [l for l in str(coverl)]
        if len(list_l) == 8:
            list_l.insert(2, '.')
            list_l.insert(6, '.')
            lain = ''.join(list_l)
            print(f'Lãi xuất phải đóng {lain} VND/Ngày')
        elif len(list_l) == 7:
            list_l.insert(1, '.')
            list_l.insert(5, '.')
            lain = ''.join(list_l)
            print(f'Lãi xuất phải đóng {lain} VND/Ngày')
        elif len(list_l) == 6:
            list_l.insert(3, '.')
            lain = ''.join(list_l)
            print(f'Lãi xuất phải đóng {lain} VND/Ngày')
        elif len(list_l) == 5:
            list_l.insert(2, '.')
            lain = ''.join(list_l)
            print(f'Lãi xuất phải đóng {lain} VND/Ngày')
        elif len(list_l) == 4:
            list_l.insert(1, '.')
            lain = ''.join(list_l)
            print(f'Lãi xuất phải đóng {lain} VND/Ngày')

        tstdn = coverl + coverg
        tstn = [tn for tn in str(tstdn)]
        if len(tstn) == 8:
            tstn.insert(2, '.')
            tstn.insert(6, '.')
            ttdn = ''.join(tstn)
            print(f'TST Đóng/Ngày: {ttdn} VND')
        elif len(tstn) == 7:
            tstn.insert(1, '.')
            tstn.insert(5, '.')
            ttdn = ''.join(tstn)
            print(f'TST Đóng/Ngày: {ttdn} VND')
        elif len(tstn) == 6:
            tstn.insert(3, '.')
            ttdn = ''.join(tstn)
            print(f'TST Đóng/Ngày: {ttdn} VND')
        elif len(tstn) == 5:
            tstn.insert(2, '.')
            ttdn = ''.join(tstn)
            print(f'TST Đóng/Ngày: {ttdn} VND')
        elif len(tstn) == 4:
            tstn.insert(1, '.')
            ttdn = ''.join(tstn)
            print(f'TST Đóng/Ngày: {ttdn} VND')


    def dunogiamdan(self, tienvay, laixuat, thoigianvay):
        goc = tienvay / thoigianvay
        for i in range(0, 12):
            lai = (tienvay - (goc * i)) * laixuat * tinhlaixuat.phantram / thoigianvay
            lai = int(lai)
            print(f'lãi suất tháng {i+1} = ', lai)





thongke = tinhlaixuat()
# sotienvay = int(input('Nhập số tiền vay: '))
# laixuatvay = int(input('Lãi xuất vay: '))
# sothangvay = int(input('Số tháng vay: '))
thongke.tienlaihangthang(1000000, 240, 12)
# thongke.dunogiamdan(120000000, 10, 12)