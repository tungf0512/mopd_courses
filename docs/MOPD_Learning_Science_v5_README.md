# MOPD Research Edition v5 — Learning Science

## Những gì đã đổi so với v4

- Giữ các bài học AI/RL, Learning Studio v4, quiz, visualizations và GPU Labs.
- Thêm chương **LS — Learning Science for AI Researchers**, gồm 12 phần lớn, case study phương pháp giảng dạy, 5 quiz và 12 nguồn trực tiếp trong website.
- Website hiện có **117 mục điều hướng**, gồm **115 trang nội dung** và hai mục chào mừng/glossary; 115/115 trang nội dung có Preflight, Scaffolding, Pause & Predict, Learning Studio v4 và Delayed Review.
- **Guided / Mixed / Independent:** mỗi mức làm hiện phần hướng dẫn phù hợp, trích từ learning objectives và đoạn giải thích của chính bài học.
- **Spaced Review Hub:** nhắc các bài đã được đặt lịch 1–3–7–14–30 ngày (heuristic), ghi lại các vòng thực hành và xuất JSON.
- **Metacognitive calibration:** lưu dự đoán ban đầu và độ tự tin tự báo cáo để so sánh về sau.
- **Interleaving:** câu hỏi so sánh bài hiện tại với một bài có liên hệ. Không xem một câu hỏi so sánh tự viết là kiểm định thành thạo.
- Bổ sung chú giải rằng tiến độ quiz không phải chứng nhận mastery.

## Bắt đầu

1. Mở `mopd-course-research-edition-v5-learning-science.html` bằng trình duyệt hiện đại. Các thư viện ngoài (fonts, KaTeX) cần mạng để tải lần đầu; text content hoạt động kể cả khi thiếu font.
2. Vào **HS → LS Learning Science** để đọc cơ sở phương pháp.
3. Mở một bài như **GRPO** hoặc **MR15 — RLCR**. Chọn Guided/Mixed/Independent tùy mức hiểu.
4. Mở **Preflight** và thử viết những gì đã biết, chọn confidence, lưu baseline.
5. Đọc bài; mở **Pause & Predict** trước phần tiếp theo. Dùng scaffolding khi thiếu kiến thức nền.
6. Cuối bài làm **Learning Studio** v4 và **Delayed Review**; thử tự nhắc trước khi mở rubric.
7. Lịch ôn xuất hiện trong sidebar **Ôn tập**. Từ Review Hub có thể xuất toàn bộ ghi chú v4 và lịch ôn v5.

## Kiểm tra đã thực hiện

- JavaScript toàn trang được biên dịch kiểm tra cú pháp qua Node `vm.Script`: PASS.
- Headless Chromium: 117 mục menu, kiểm tra 115/115 bài có thể tạo Preflight, Scaffolding, Pause và Review: PASS.
- Các trang đại diện LS, GRPO, MOPD, MR14 mở được, không có lỗi JavaScript: PASS.
- Desktop: lưu baseline, đổi mode Independent, tạo vòng ôn và kiểm tra Hub/schedule với localStorage giả lập: PASS.
- Mobile 390px: mở MR15 và xác nhận không tràn ngang, JS error=0: PASS.
- Hạn chế: do môi trường trình duyệt kiểm thử chặn `file://` và HTTP, chưa kiểm chứng lưu trữ xuyên các lần mở browser bằng origin thật; chưa thử các hoạt động của backend đăng nhập thực tế.

## Lưu ý khoa học

- Practice testing và spacing có evidence tổng quát mạnh hơn nhiều hoạt động ghi chép thụ động; hiệu quả của từng bài và lịch ôn trên site chưa được thử nghiệm thực địa.
- Lịch cách quãng, rubric, chế độ hướng dẫn là **implementation heuristics**, không phải thuật toán tự đo năng lực.
- Self-assessment không xác minh câu trả lời tự do; muốn kiểm định tác dụng giáo dục phải đo delayed retention và novel transfer so với nhóm đối chứng.

Đọc thêm `LEARNING_SCIENCE_v5_RESEARCH_NOTES.md` để xem bảng nguồn → quyết định thiết kế, giới hạn, gợi ý experiment design và danh mục 14 nguồn.
