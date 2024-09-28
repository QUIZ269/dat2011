def xacNhanHanhDong(action_desc):
    """Xác nhận hành động từ người dùng."""
    while True:
        xacNhan = input(f"Bạn có chắc chắn muốn {action_desc}? (Y/N): ").strip().upper()
        if xacNhan == 'Y':
            return True
        elif xacNhan == 'N':
            print("Hành động đã bị hủy.")
            return False
        else:
            print("Vui lòng nhập 'Y' hoặc 'N'.")

def hienThi():
    print("Đã chọn chương trình: Hiển thị danh sách")
def timKiem():
    print("Đã chọn chương trình: Tìm kiếm ")
def themMoi():
    print("Đã chọn chương trình: Thêm mới")
    if xacNhanHanhDong("thêm dữ liệu mới"):
        
        print("Dữ liệu đã được thêm.")
    else:
        print("Không có thay đổi nào được thực hiện.")
def capNhat():
    print("Đã chọn chương trình: Cập nhật")
    if xacNhanHanhDong("cập nhật dữ liệu"):
        
        print("Dữ liệu đã được cập nhật.")
    else:
        print("Không có thay đổi nào được thực hiện.")
def xoa():
    print("Đã chọn chương trình: Xóa")
    if xacNhanHanhDong("xóa dữ liệu"):

        print("Dữ liệu đã được xóa.")
    else:
        print("Không có thay đổi nào được thực hiện.")
def thayTheDuLieu():
    print("Đã chọn chương trình: Thay thế dữ liệu")
    if xacNhanHanhDong("Thay thế dữ liệu"):
    
        print("Dữ liệu đã được thay thế.")
    else:
        print("Không có thay đổi nào được thực hiện.")
def phanTrang():
    print("Đã chọn chương trình: Phân trang")
def xemChiTiet():
    print("Đã chọn chương trình: Xem chi tiết")
def xuatDuLieu():
    print("Đã chọn chương trình: Xuất dữ liệu")
def phucHoiDuLieu():
    print("Đã chọn chương trình: Phục hồi dữ liệu")
def thoat():
    if xacNhanHanhDong("thoát chương trình"):
        print("Thoát chương trình.")
        exit(0)
    else:
        print("Không thoát chương trình, tiếp tục làm việc.")

def show_menu():
    while True:
        print("\n --------- QUẢN LÝ MÔN HỌC ----------")
        print("1. Hiển thị danh sách")
        print("2. Tìm kiếm hoặc lọc")
        print("3. Thêm mới ")
        print("4. Cập nhật")
        print("5. Xóa")
        print("6. Thay đổi dữ liệu")
        print("7. Phân trang")
        print("8. Xem chi tiết")
        print("9. Xuất dữ liệu")
        print("10. Phục hồi dữ liệu")
        print("0. Thoát")

        try:
            chon = int(input("Mời nhập chương trình: "))
            
            if chon == 1:
                hienThi()
                
            elif chon == 2:
                timKiem()
                
            elif chon == 3:
                themMoi()

            elif chon == 4:
                capNhat()

            elif chon == 5:
                 xoa()

            elif chon == 6:
                thayTheDuLieu()   

            elif chon == 7:
                 phanTrang()

            elif chon ==8:
                 xemChiTiet()

            elif chon == 9:
                 xuatDuLieu()

            elif chon == 10:
                 phucHoiDuLieu()
           
            elif chon == 0:
                thoat()
               
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")
                
        except ValueError:
            print("Lựa chọn không hợp lệ,không được nhập ký tự, vui lòng thử lại đúng yêu cầu(1-10)")


show_menu()