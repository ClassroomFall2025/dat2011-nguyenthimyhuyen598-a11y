class NhanVien:
    def __init__(self, Ma_nv, Hoten, luong):
        self.Ma_nv = Ma_nv
        self.Hoten = Hoten
        self.luong = luong
# tính thu nhập
    def get_ThuNhap(self):
        return self.luong
# tính thuế thu nhập
    def get_Thue_ThuNhap(self):

        if self.get_ThuNhap() >= 15000000:
            Thue_ThuNhap = self.get_ThuNhap() * 0.12
        elif self.get_ThuNhap() > 9000000: 
            Thue_ThuNhap = self.get_ThuNhap * 0.10
        elif self.get_ThuNhap() > 0:  
            Thue_ThuNhap = "Không phải nộp thuế"
        else:  
            print("Thu nhập không hợp lệ")
        return Thue_ThuNhap
    def xuat (self):
        print(f"{self.Ma_nv},{self.Hoten},{self.luong},{self.get_ThuNhap()},{self.get_Thue_ThuNhap()}")


class TiepThi(NhanVien):
    def __init__(self, Ma_nv, Hoten, luong, doanhSo, Hoahong):
        super().__init__(Ma_nv, Hoten, luong)
        self.doanhSo = doanhSo
        self.Hoahong = Hoahong

    def get_ThuNhap(self):
        return self.luong + self.doanhSo * self.Hoahong

class TruongPhong(NhanVien):
    def __init__(self, Ma_nv, Hoten, luong, trachNhiem):
        super().__init__(Ma_nv, Hoten, luong)
        self.trachNhiem = trachNhiem

    def get_ThuNhap(self):
        return self.luong + self.trachNhiem
