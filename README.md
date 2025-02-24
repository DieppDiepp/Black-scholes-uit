# 📘 Giải Thích Cơ Sở Toán Học Của Mô Hình Black-Scholes Trong Định Giá Quyền Chọn Tài Chính  

## 📌 Giới thiệu  

Kể từ khi sàn giao dịch chứng khoán đầu tiên trên thế giới Amsterdam được thành lập cho tới một một thị trường hiện đại, năng động như ngày nay, các chủ thể tham gia thị trường luôn mong muốn tìm kiếm cho mình lợi nhuận thông qua việc mua bán cổ phiếu, nhưng có lẽ bởi những rủi ro từ hình thức truyền thống này vẫn khiến một số nhà đầu tư phân vân. Và với động lực đó rất nhiều các sản phẩm tài chính kiểu mới ra đời như các hợp đồng quyền chọn, phái sinh, hoán đổi nợ - cổ phiếu... Mặc dù bản chất của chúng vẫn dựa trên cơ chế giao dịch mua bán nhưng những hình thức này mang tới một sự đảm bảo cho các chủ thể sở hữu chúng, do đó chúng nhanh chóng được ưa chuộng bởi bộ phận nhà đầu tư an toàn. Và trong bài báo cáo này, chúng tôi xin được trình bày mô hình định giá quyền chọn nổi tiếng Black-Scholes, cũng như là các lý thuyết toán học đứng đằng sau giải thích và biện luận cho mô hình như chuyển động Brownian, quá trình winner, bổ đề Ito, phương trình vi phân ngẫu nhiên, ...

Báo cáo này được thực hiện bởi nhóm sinh viên từ **Trường Đại học Công nghệ Thông tin, Đại học Quốc gia TP. Hồ Chí Minh**, gồm:  
- **Ung Hoàng Long**  
- **Lương Đắc Nguyên**  
- **Bùi Trương Thái Sơn**  
- **Nguyễn Hoàng Long**  

Mục tiêu của báo cáo là giúp mọi người hiểu rõ hơn về **mô hình Black-Scholes**, một công cụ toán học quan trọng trong tài chính giúp định giá quyền chọn. Nhóm đi sâu vào các nền tảng toán học của mô hình như **Chuyển động Brownian, Bổ đề Ito, Phương trình vi phân ngẫu nhiên (SDE)** để giúp người đọc có cái nhìn tổng quan và logic hơn về công thức Black-Scholes. Dưới đây chỉ là tóm tắt, để làm rõ cơ sở toán học, tham khảo bản PDF báo cáo của chúng tôi.

---

## 📖 Nội dung chính  

### 1️⃣ **Chuyển động Brownian - Sự ngẫu nhiên trong thị trường tài chính**  
- Chuyển động Brownian là một mô hình mô phỏng sự biến động ngẫu nhiên của giá cổ phiếu. Về mặt toán học, nó tuân theo các điều kiện:  
  1. B(0) = 0
  2. B(t) - B(s) $\sim \mathcal{N}(0, t-s)$ (Phân phối chuẩn với giá trị kỳ vọng 0, phương sai $t-s$)  
  3. Gia số độc lập: $B(t_i) - B(t_{i-1})$ độc lập với nhau  

Công thức này giúp mô tả sự biến động không dự đoán được của cổ phiếu theo thời gian.  

---

### 2️⃣ **Phương trình vi phân ngẫu nhiên (SDE) - Cách mô tả sự thay đổi của giá cổ phiếu**  

Một mô hình tài chính cần tính đến sự biến động ngẫu nhiên. Do đó, người ta dùng phương trình vi phân ngẫu nhiên (SDE):  

$$
dX_t = a(X_t, t) dt + b(X_t, t) dB_t
$$  

Với:  
- $a(X_t, t)dt$ là **thành phần trôi dạt (drift)**, xác định xu hướng chính của giá cổ phiếu.  
- $b(X_t, t)dB_t$ là **thành phần khuếch tán (diffusion)**, thể hiện sự biến động ngẫu nhiên.  
- $dB_t$ là chuyển động Brownian tiêu chuẩn.  

📌 Một trong những dạng đặc biệt của SDE là **chuyển động Brownian hình học (GBM)**, dùng để mô hình hóa giá cổ phiếu:  

$$
dS(t) = \mu S(t) dt + \sigma S(t) dB(t)
$$  

Với:  
- $\mu$ là tỷ lệ tăng trưởng trung bình  
- $\sigma$ là độ biến động  

---

### 3️⃣ **Bổ đề Ito - Công cụ toán học để xử lý quá trình ngẫu nhiên**  

#### Công thức Bổ đề Ito:  
Nếu $f(X, t)$ là một hàm số khả vi và $X(t)$ tuân theo phương trình vi phân ngẫu nhiên:  

$$
dX(t) = a(X, t) dt + b(X, t) dB(t)
$$  

Thì vi phân của $f(X, t)$ được tính như sau:  

$$
df = \left( \frac{\partial f}{\partial t} + a \frac{\partial f}{\partial X} + \frac{1}{2} b^2 \frac{\partial^2 f}{\partial X^2} \right) dt + b \frac{\partial f}{\partial X} dB(t)
$$  

Đây là công thức rất quan trọng giúp suy ra mô hình Black-Scholes.  

---

### 4️⃣ **Phương trình vi phân Black-Scholes - Định giá quyền chọn tài chính**  

Bằng cách áp dụng **Bổ đề Ito** vào một danh mục đầu tư gồm cổ phiếu và quyền chọn, ta thu được **phương trình Black-Scholes**:  

$$
\frac{\partial C}{\partial t} + rS \frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} = rC
$$  

Với:  
- $C$ là giá của quyền chọn.  
- $S$ là giá cổ phiếu hiện tại.  
- $r$ là lãi suất phi rủi ro.  
- $\sigma$ là độ biến động.  

👉 Phương trình này cho phép ta xác định giá trị của quyền chọn tài chính theo thời gian.  

---

### 5️⃣ **Công thức Black-Scholes để định giá quyền chọn**  

#### 🌟 **Công thức quyền chọn mua Châu Âu (Call Option):**  
$$
C = S(0) N(d_1) - K e^{-rT} N(d_2)
$$  

#### 🌟 **Công thức quyền chọn bán Châu Âu (Put Option):**  
$$
P = K e^{-rT} N(-d_2) - S(0) N(-d_1)
$$  

Với:  

$$
d_1 = \frac{\ln (\frac{S(0)}{K}) + (r + \frac{\sigma^2}{2}) T}{\sigma \sqrt{T}}
$$  

$$
d_2 = d_1 - \sigma \sqrt{T}
$$  

Trong đó:  
- $S(0)$: Giá cổ phiếu ban đầu  
- $K$: Giá thực hiện  
- $T$: Thời gian đáo hạn  
- $r$: Lãi suất phi rủi ro  
- $\sigma$: Độ biến động  

---

## 📝 Kết luận  
✔ **Mô hình Black-Scholes là nền tảng quan trọng trong tài chính hiện đại**, giúp xác định giá trị quyền chọn mà không cần ước lượng trực tiếp mức lợi nhuận kỳ vọng của nhà đầu tư.  

✔ Dựa trên nền tảng toán học chặt chẽ **(Chuyển động Brownian, Bổ đề Ito, và Phương trình Vi phân Ngẫu nhiên)**, nó tạo ra một phương pháp phổ quát để **định giá quyền chọn tài chính**.  

✔ Dù có một số giả định đơn giản hóa (không có phí giao dịch, không có chia cổ tức…), **mô hình này vẫn đóng vai trò rất lớn trong các chiến lược tài chính thực tế**.  

---

## 📚 Tài liệu tham khảo  
Báo cáo được xây dựng dựa trên các tài liệu toán học tài chính hàng đầu, bao gồm:  
1. **F. C. Klebaner**, *Introduction to Stochastic Calculus with Applications*  
2. **Y. Yoo**, *Stochastic Calculus and Black-Scholes Model*  
3. Wikipedia & các tài liệu học thuật khác.  
