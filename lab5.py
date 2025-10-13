class Sanpham:
    def __init__(self, tensp, giamgia, dongia):
        self.tensp = tensp
        self.dongia = dongia
        self.giamgia = giamgia

    def get_tensp(self):
        return self.tensp
    def set_tensp(self, tensp):
        self.tensp = tensp
    def get_dongia(self):
        return self.dongia
    def set_dongia(self, dongia):
        self.dongia = dongia
    def get_giamgia(self):
        return self.giamgia
    def set_giamgia(self, giamgia):
        self.giamgia = giamgia

    def thue_nhap_khau(self):
        return self.dongia * 0.1
    def nhap_sp(self):
        self.tensp = input("Nhập tên sản phẩm: ")
        self.dongia = float(input("Nhập đơn giá: "))
        self.giamgia = float(input("Nhập giảm giá: "))
        
    def xuat_tt_sp(self):
        print(f"Tên sản phẩm: {self.tensp}, Đơn giá: {self.dongia}, Giảm giá: {self.giamgia}, Thuế nhập khẩu: {self.thue_nhap_khau()}")

    def __str__(self):
        return f"Sanpham(tensp={self.tensp}, dongia={self.dongia}, giamgia={self.giamgia})"