import Nhanvien as Nhanvien
class Quanlynhanvien:
    def __init__(self):
        self.ds_nv = []

    def Nhap_ds_nhan_vien(self):
        while True:
            Ma_nv = input("Nhập mã nhân viên: ")
            hoten = input("Nhập họ tên nhân viên: ")
            luong = float(input("Nhập lương nhân viên: "))
            loai_nv = input("Nhập loại nhân viên (TiepThi/TruongPhong): ")
            if loai_nv.lower() == 'tiepthi':
                doanhSo = float(input("Nhập doanh số: "))
                Hoahong = float(input("Nhập hoa hồng: "))
                nv = Nhanvien.TiepThi (Ma_nv, hoten, luong, doanhSo, Hoahong)
                self.ds_nv.append(nv)
            elif loai_nv.lower() == 'truongphong':
                trachNhiem = float(input("Nhập trách nhiệm: "))
                nv = Nhanvien.TruongPhong (Ma_nv, hoten, luong, trachNhiem)
                self.ds_nv.append(nv)
            elif loai_nv.lower() == 'exit':
                print("Kết thúc nhập thông tin nhân viên")
                break
            else:
                print("Nhập chưa đúng yêu cầu")
        return self.ds_nv
    
    def Xuat_ds_nhan_vien(self):
        if not self.ds_nv:
            print("Danh sách nhân viên rỗng.")
        else:
            print("Mã NV, Họ tên, Lương, Thu nhập, Thuế thu nhập")
            for nv in self.ds_nv:
                nv.xuat()

    def Tim_nv_theo_ma(self):
        ma = input("Nhập mã nhân viên cần tìm: ")
        for nv in self.ds_nv:
            if nv.Ma_nv == ma:
                print("Đã tìm thấy nhân viên:")
                nv.xuat()
                return
            print("Không tìm thấy nhân viên có mã:", ma)

    def Xoa_nv_theo_ma(self):
        ma = input("Nhập mã nhân viên cần xóa: ")
        for nv in self.ds_nv:
            if nv.Ma_nv == ma:
                self.ds_nv.remove(nv)
                print("Đã xóa nhân viên có mã:", ma)
                nv.xuat()
                return
        print("Không tìm thấy nhân viên có mã:", ma)

    def Cap_nhat_thong_tin_nv(self):
        ma = input("Nhập mã nhân viên cần cập nhật: ")
        for nv in self.ds_nv:
            if nv.Ma_nv == ma:
                nv.Hoten = input("Nhập họ tên mới: ")
                nv.luong = float(input("Nhập lương mới: "))
                print("Đã cập nhật thông tin nhân viên.")
                return
        print("Không tìm thấy nhân viên có mã:", ma)

    def Tim_nv_theo_luong(self):
        min_luong = float(input("Nhập lương tối thiểu: "))
        max_luong = float(input("Nhập lương tối đa: "))
        ds = [nv for nv in self.ds_nv if min_luong <= nv.get_ThuNhap() <= max_luong]
        if ds:
            print("Danh sách nhân viên có lương trong khoảng:")
            for nv in ds:
                nv.xuat()
        else:
            print("Không có nhân viên trong khoảng lương này.")

    def Sap_xep_nv_theo_hoten(self):
        if not self.ds_nv:
            print("Danh sách nhân viên rỗng, không thể sắp xếp.")
        else:
            self.ds_nv.sort(key=lambda nv: nv.Hoten, reverse=False)
            print("Đã sắp xếp danh sách nhân viên theo họ tên.")
            for nv in self.ds_nv:
                nv.xuat()

    def Sap_xep_nv_theo_thu_nhap(self):
        if not self.ds_nv:
            print("Danh sách nhân viên rỗng, không thể sắp xếp.")
        else:
            self.ds_nv.sort(key=lambda nv: nv.get_ThuNhap)
            print("Đã sắp xếp danh sách nhân viên theo thu nhập.")
            for nv in self.ds_nv:
                nv.xuat()

    def Xuat_5_nv_thu_nhap_cao_nhat(self):
        if not self.ds_nv:
            print("Danh sách nhân viên rỗng.")
        else:
            # Dùng lại hàm sắp xếp có sẵn
            self.Sap_xep_nv_theo_thu_nhap()
            print("Tên NV | Lương | Thưởng | Thu nhập")
            for nv in self.ds_nv[:5]:
                nv.xuat()


