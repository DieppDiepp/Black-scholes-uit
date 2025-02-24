# Giải Thích Cơ Sở Toán Học Của Mô Hình Black-Scholes Trong Định Giá Quyền Chọn Tài Chính  

## 📌 Giới thiệu  

Kể từ khi sàn giao dịch chứng khoán đầu tiên trên thế giới Amsterdam được thành lập cho tới một một thị trường hiện đại, năng động như ngày nay, các chủ thể tham gia thị trường luôn mong muốn tìm kiếm cho mình lợi nhuận thông qua việc mua bán cổ phiếu, nhưng có lẽ bởi những rủi ro từ hình thức truyền thống này vẫn khiến một số nhà đầu tư phân vân. Và với động lực đó rất nhiều các sản phẩm tài chính kiểu mới ra đời như các hợp đồng quyền chọn, phái sinh, hoán đổi nợ - cổ phiếu... Mặc dù bản chất của chúng vẫn dựa trên cơ chế giao dịch mua bán nhưng những hình thức này mang tới một sự đảm bảo cho các chủ thể sở hữu chúng, do đó chúng nhanh chóng được ưa chuộng bởi bộ phận nhà đầu tư an toàn. Và trong bài báo cáo này, chúng tôi xin được trình bày mô hình định giá quyền chọn nổi tiếng Black-Scholes, cũng như là các lý thuyết toán học đứng đằng sau giải thích và biện luận cho mô hình như chuyển động Brownian, quá trình winner, bổ đề Ito, phương trình vi phân ngẫu nhiên, ...

Báo cáo này được thực hiện bởi nhóm sinh viên từ **Trường Đại học Công nghệ Thông tin, Đại học Quốc gia TP. Hồ Chí Minh**, gồm:  
- **Ung Hoàng Long**  
- **Lương Đắc Nguyên**  
- **Bùi Trương Thái Sơn**  
- **Nguyễn Hoàng Long**  

Báo cáo này nhằm giải thích một cách dễ hiểu về mô hình Black-Scholes - một công cụ cực kỳ quan trọng giúp định giá quyền chọn tài chính. Bên cạnh việc trình bày công thức Black-Scholes, nhóm còn đi sâu vào nền tảng toán học đứng sau mô hình, gồm **chuyển động Brownian, bổ đề Ito và phương trình vi phân ngẫu nhiên**.  

## 📖 Nội dung chính  

### 1️⃣ **Chuyển động Brownian - Sự ngẫu nhiên trong thị trường tài chính**  
Chuyển động Brownian là mô hình toán học mô phỏng sự biến động ngẫu nhiên của giá cổ phiếu. Nó được phát hiện bởi nhà khoa học Robert Brown khi quan sát các hạt phấn hoa chuyển động trong nước. Về sau, nhà toán học Norbert Wiener phát triển mô hình thành một quá trình ngẫu nhiên tiên tiến hơn được ứng dụng trong tài chính.  

Đặc điểm quan trọng của chuyển động Brownian:  
- **Ngẫu nhiên tuyệt đối**: Mô hình này không thể dự đoán một cách chính xác, chỉ có thể ước lượng xu hướng.  
- **Không khả vi**: Mọi thay đổi đều không trơn tru, giống như sự biến động thất thường của giá chứng khoán.  

### 2️⃣ **Phương trình vi phân ngẫu nhiên (SDE) - Cách mô tả sự thay đổi của giá cổ phiếu**  
Trong thế giới thực, giá cổ phiếu không chỉ bị ảnh hưởng bởi xu hướng tăng trưởng mà còn bởi các yếu tố ngẫu nhiên. Vì vậy, chúng ta dùng **phương trình vi phân ngẫu nhiên (SDE)** thay vì phương trình vi phân thông thường.  

**Công thức tổng quát của SDE:**  
\[
dX_t = a(X_t, t) dt + b(X_t, t) dB_t
\]  
Trong đó:  
- \( a(X_t, t)dt \) là **thành phần trôi dạt (drift)** - thể hiện xu hướng chính của giá cổ phiếu.  
- \( b(X_t, t)dB_t \) là **thành phần khuếch tán (diffusion)** - thể hiện mức độ biến động ngẫu nhiên.  
- \( dB_t \) là chuyển động Brownian.  

Mô hình nổi bật sử dụng SDE là **chuyển động Brownian hình học (GBM)** - nền tảng của mô hình Black-Scholes.  

### 3️⃣ **Bổ đề Ito - Công cụ toán học để xử lý quá trình ngẫu nhiên**  
Bổ đề Ito giúp chúng ta tính đạo hàm của một hàm số khi hàm đó bị ảnh hưởng bởi một quá trình ngẫu nhiên như chuyển động Brownian. Đây là nền tảng then chốt giúp xây dựng mô hình Black-Scholes.  

**Cách hiểu đơn giản:**  
- Nếu chúng ta biết **giá cổ phiếu biến động ngẫu nhiên** theo thời gian, làm thế nào để tính được **sự thay đổi của một hàm giá quyền chọn phụ thuộc vào cổ phiếu đó**?  
- Câu trả lời là sử dụng **bổ đề Ito** để tìm phương trình vi phân cho giá quyền chọn.  

### 4️⃣ **Phương trình vi phân Black-Scholes - Công thức đột phá trong tài chính**  
Từ chuyển động Brownian, SDE và bổ đề Ito, nhóm đã dẫn đến phương trình **Black-Scholes**, giúp định giá quyền chọn mua và bán.  

**Phương trình Black-Scholes:**  
\[
\frac{\partial C}{\partial t} + rS \frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} = rC
\]  
Trong đó:  
- \( C \) là giá của quyền chọn.  
- \( S \) là giá cổ phiếu hiện tại.  
- \( r \) là lãi suất phi rủi ro.  
- \( \sigma \) là độ biến động giá.  

### 5️⃣ **Công thức Black-Scholes - Cách tính giá quyền chọn**  
Dưới đây là hai công thức then chốt để định giá **quyền chọn mua (Call Option) và quyền chọn bán (Put Option)**:  

\[
C = S(0) N(d_1) - K e^{-rT} N(d_2)
\]
\[
P = K e^{-rT} N(-d_2) - S(0) N(-d_1)
\]

Với  
\[
d_1 = \frac{\ln (\frac{S(0)}{K}) + (r + \frac{\sigma^2}{2}) T}{\sigma \sqrt{T}}
\]
\[
d_2 = d_1 - \sigma \sqrt{T}
\]  

📌 **Ý nghĩa dễ hiểu của công thức này:**  
- Nếu cổ phiếu có giá cao hơn giá thực hiện \( K \) tại thời điểm đáo hạn, người mua quyền chọn có lợi.  
- Công thức cho chúng ta một cách tính toán chính xác giá trị của quyền chọn dựa trên giá cổ phiếu hiện tại, mức biến động và lãi suất.  

## 📝 Kết luận  
**Mô hình Black-Scholes là một trong những phát minh quan trọng trong tài chính hiện đại.** Nó giúp các nhà đầu tư và nhà giao dịch định giá quyền chọn và hiểu rõ sự biến động của thị trường. Báo cáo này trình bày nền tảng toán học của mô hình một cách chi tiết, dễ hiểu để bạn đọc có thể nắm được cách thức hoạt động của công thức Black-Scholes.  

## 📚 Tài liệu tham khảo  
Bài báo sử dụng nhiều tài liệu nghiên cứu về toán học tài chính, bao gồm sách, bài báo khoa học và các tài liệu trực tuyến.  
