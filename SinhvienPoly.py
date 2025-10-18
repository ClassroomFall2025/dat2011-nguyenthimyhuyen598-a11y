class SInhvienPoly:
    def __init__(self, hoten, nganh):
        self.hoten = hoten
        self.nganh = nganh
#tinh diem
    def get_diem(self):
        return 0

    def get_hoc_luc(self):

        if self.get_diem() >= 9 and self.get_diem() <= 10:
            hoc_luc =  "Xuất sắc"
        elif self.get_diem() >= 8:
            hoc_luc = "Giỏi"
        elif self.get_diem() >= 7:
            hoc_luc = "Khá"
        elif self.get_diem() >= 5:
            return "Trung bình"
        elif self.get_diem() > 0:
            hoc_luc = "Chưa đạt"
        else:
            print("Điểm không hợp lệ")
        return hoc_luc
    def xuat (self):
        print(f"{self.hoten},{self.nganh}, {self.get_diem()},{self.get_hoc_luc()}")

class SinhVienIT(SInhvienPoly):
    def __init__(self, hoten, nganh, diemJava, diemHtml, diemCss):
        super().__init__(hoten, nganh)
        self.diemJava = diemJava
        self.diemHtml = diemHtml
        self.diemCss = diemCss

    def get_diem(self):
        return (self.diemJava * 2 + self.diemHtml + self.diemCss) / 4

class SinhVienBiz(SInhvienPoly):
    def __init__(self, hoten, nganh, diemMarketing, diemSales):
        super().__init__(hoten, nganh)
        self.diemMarketing = diemMarketing
        self.diemSales = diemSales

    def get_diem(self):
        return (self.diemMarketing + self.diemSales * 2) / 3