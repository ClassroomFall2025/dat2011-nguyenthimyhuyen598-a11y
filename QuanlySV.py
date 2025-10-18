import SinhvienPoly as svpl
class quanlisinhvien:
    #khởi tạo ds sv rỗng
    def __init__(self):
        self.dssv = []
    #phương thưc nhập dssv
    def nhap_danh_sach_sinh_vien(self):
        while True:
            hoten_sv = input("Nhập họ tên sinh viên: ")
            nganh = input("Nhập ngành học: ")
            if nganh.lower() == 'it':
                diem_java = float(input("Nhập điểm Java: "))
                diem_html = float(input("Nhập điểm HTML: "))
                diem_css = float(input("Nhập điểm CSS: "))
                sv = svpl.SinhVienIT(hoten_sv, nganh, diem_java, diem_html, diem_css)
                self.dssv.append(sv)
            elif nganh.lower() == 'biz':
                diem_marketing = float(input("Nhập điểm Marketing: "))
                diem_sales = float(input("Nhập điểm Sales: "))
                sv = svpl.SinhVienBiz(hoten_sv, nganh, diem_marketing, diem_sales)
                self.dssv.append(sv)
            elif nganh.lower() == 'exit':
                print("kết thúc nhập thông tin sinh viên")
                break
            else:
                print("Nhâp chưa đúng yêu cầu")
        return self.dssv
    
    def xuat_danh_sach_sinh_vien(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng.")
        else:
            print("Tên sinh vien, Ngành học, Điểm, Học lực")
            for sv in self.dssv:
                sv.xuat()
    
    def xuat_danh_sach_sinh_vien_gioi(self):
        ds_gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
        if not ds_gioi:
            print("Không có sinh viên giỏi.")
        else:
            print("Danh sách sinh viên giỏi:")
            for sv in ds_gioi:
                sv.xuat()

    def sap_xep_dssv(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng, không thể sắp xếp.")
        else:
            self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
            print("Đã sắp xếp danh sách sinh viên theo điểm giảm dần.")