def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = (10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2])
    else:
        tien_nuoc = (10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] +
                     (so_nuoc - 30) * gia_ban_nuoc[3])
    return tien_nuoc

# print("Nhập số nước sử dụng (m3): ", end="")
# so_nuoc = float(input())
# print(so_nuoc, "m3")
# print("Số tiền nước phải trả: ", tinh_tien_nuoc(so_nuoc), "VND")


# Tinh nguyen lieu lam banh
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"đường": 0.04, "đậu": 0.07}
    banh_thap_cam = {"đường": 0.06, "đậu": 0}
    banh_deo = {"đường": 0.05, "đậu": 0.02}
    nguyen_lieu = {}

    dau_hop_banh = sl_bdx * banh_dau_xanh["đậu"] + sl_btc * banh_thap_cam["đậu"] + sl_bd * banh_deo["đậu"]
    duong_hop_banh = sl_bdx * banh_dau_xanh["đường"] + sl_btc * banh_thap_cam["đường"] + sl_bd * banh_deo["đường"]

    nguyen_lieu["đường"] = duong_hop_banh
    nguyen_lieu["đậu"] = dau_hop_banh
    return nguyen_lieu

# print("Nhập số lượng bánh đậu xanh:",  end="")
# sl_bdx = int(input())
# print("\n Nhập số lượng bánh thập cẩm: ", end="")
# sl_btc = int(input())
# print("\n Nhập số lượng bánh dẻo: ", end="")
# sl_bd = int(input())

# nguyen_lieu = tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd)
# print("\n Số lượng đường cần dùng: ", nguyen_lieu["đường"], "kg")
# print("Số lượng đậu cần dùng: ", nguyen_lieu["đậu"], "kg")