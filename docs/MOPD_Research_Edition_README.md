# Đài Quan Sát MOPD — Research Edition (24/10/2026)

## Các thay đổi chính

- Giữ lại toàn bộ nội dung và thiết kế từ HTML gốc, bổ sung **11 bài Research Track MR1–MR11** (lịch sử KD, on-policy states và KL, tối ưu ngân sách token, teacher reliability, gradient/update conflict, delta distillation, cross-tokenizer, continual learning, evaluation khoa học, capstone, black-box/API-only).
- Thêm phụ lục chuyên sâu và cảnh báo phạm vi kết luận cho Chương **4 (KL)**, **6 (MOPD)**, **C1 (giới hạn RLVR)** và lộ trình học.
- Thêm sách và danh mục papers có link, làm rõ preprint/giới hạn thực nghiệm.
- Thêm **hai visualization tương tác**: token-share imbalance và teacher routing.
- Thêm **một GPU Lab** end-to-end toy MOPD PyTorch để so sánh global-token và equal-domain loss; file `toy_mopd_budget.py` có thể chạy riêng.
- Bổ sung các thuật ngữ trong glossary và điều chỉnh diễn giải cực đoan về reverse KL/forward KL, pass@k và RLVR.
- Bổ sung cơ chế `localStorage` cho tiến độ khách học ngoại tuyến, giữ API tài khoản đồng bộ vốn có.

## Cách sử dụng

1. Mở `mopd-course-research-edition.html` bằng trình duyệt hiện đại (hoặc phục vụ bằng web server tĩnh). Các nguồn KaTeX/font sử dụng CDN nên cần kết nối mạng để hiển thị tối ưu.
2. Vào sidebar **MOPD Research Track · 2026** để xem MR1–MR11. MR3 và MR4 có visualization tương tác.
3. Sao chép GPU Lab MR3 hoặc chạy `python toy_mopd_budget.py` (cần PyTorch). Đây là thí nghiệm toy, không phải bản tái lập các benchmark quy mô LLM trong paper.
4. Nếu muốn sử dụng tài khoản và đồng bộ tiến độ, bạn vẫn cần API server `/api/me`, `/api/login`, `/api/progress` và các endpoint cũ của website. Backend không nằm trong file HTML được cung cấp, nên chưa được kiểm tra.

## Các bước xác minh đã làm

- Kiểm tra cú pháp JavaScript bằng Node.js (`node --check`).
- Chạy thử trên Chromium headless bằng Playwright, duyệt các chương được cập nhật và toàn bộ MR1–MR11, kiểm tra quiz và visualization; không ghi nhận lỗi JavaScript tại những trang thử.
- Chạy thử tất cả code-exercise mới bằng Python, gồm cả GPU Lab CPU; thành công trong môi trường kiểm tra.
- Kiểm tra responsive mobile và trạng thái mở/đóng sidebar.

## Điều chưa khẳng định

Chưa tái lập độc lập tất cả kết quả nghiên cứu trong các papers gốc; các kết quả đưa vào bài được dẫn là những kết quả *tác giả các công trình báo cáo* ở điều kiện của họ. Chưa kiểm tra backend thật và các dịch vụ ngoài trang. Các bài/chương cũ ngoài vùng chỉnh sửa không được kiểm chứng từng công thức bằng paper gốc trong lần này.
