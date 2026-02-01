import streamlit as st

# --- PHẦN 1: LOGIC XỬ LÝ (BACKEND) ---
def xac_dinh_cung(ngay, thang):
    # Mốc ngày chuyển cung của 12 tháng
    ngay_cat = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]

    # Danh sách tên cung
    ds_cung = ['Ma Kết', 'Bảo Bình', 'Song Ngư', 'Bạch Dương', 'Kim Ngưu', 'Song Tử',
               'Cự Giải', 'Sư Tử', 'Xử Nữ', 'Thiên Bình', 'Bọ Cạp', 'Nhân Mã', 'Ma Kết']

    if ngay < ngay_cat[thang - 1]:
        return ds_cung[thang - 1]
    else:
        return ds_cung[thang]

# --- PHẦN 2: GIAO DIỆN NGƯỜI DÙNG (FRONTEND) ---
def main():
    # Tiêu đề ứng dụng
    st.title("🔮 Ứng dụng Tra cứu Cung Hoàng Đạo")
    st.subheader("Nhập ngày sinh của bạn để khám phá!")

    # Tạo 2 cột để giao diện gọn gàng hơn
    col1, col2 = st.columns(2)

    with col1:
        ngay = st.number_input("Chọn Ngày sinh:", min_value=1, max_value=31, value=15)
    
    with col2:
        thang = st.number_input("Chọn Tháng sinh:", min_value=1, max_value=12, value=6)

    # Nút bấm tra cứu
    if st.button("Xem kết quả"):
        ket_qua = xac_dinh_cung(ngay, thang)
        
        # Hiển thị kết quả nổi bật
        st.success(f"Cung hoàng đạo của bạn là: **{ket_qua}**")
        ds_anh = {
            'Ma Kết': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Capricorn.svg/1200px-Capricorn.svg.png',
            'Bảo Bình': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Aquarius.svg/1200px-Aquarius.svg.png',
            'Song Ngư': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Pisces.svg/1200px-Pisces.svg.png',
            'Bạch Dương': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Aries.svg/1200px-Aries.svg.png',
            'Kim Ngưu': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Taurus.svg/1200px-Taurus.svg.png',
            'Song Tử': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Gemini.svg/1200px-Gemini.svg.png',
            'Cự Giải': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Cancer.svg/1200px-Cancer.svg.png',
            'Sư Tử': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Leo.svg/1200px-Leo.svg.png',
            'Xử Nữ': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Virgo.svg/1200px-Virgo.svg.png',
            'Thiên Bình': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Libra.svg/1200px-Libra.svg.png',
            'Bọ Cạp': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Scorpio.svg/1200px-Scorpio.svg.png',
            'Nhân Mã': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Sagittarius.svg/1200px-Sagittarius.svg.png'
        }
        if ket_qua in ds_anh:
            st.image(ds_anh[ket_qua], width=300, caption=f"Biểu tượng của {ket_qua}")
        st.balloons() # Hiệu ứng chúc mừng cho vui vẻ!

if __name__ == "__main__":
    main()