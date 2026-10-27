# Đài Quan Sát MOPD · Research Edition v4 — Learning Studio

## Tổng quan

- File gốc: `mopd-course-research-edition-v3-rlcr.html` (được giữ nguyên).
- File kết quả: `mopd-course-research-edition-v4-learning-studio.html`.
- **116 mục điều hướng** (115 mục gốc + 1 chương mới “HS — Học cách học”).
- **114 trang có nội dung bài học**, không kể trang chào mừng và glossary, đều có khối Learning Studio với đủ 3 tầng.
- 30 bài được biên soạn 3 lời dẫn theo chủ đề cụ thể (GRPO, OPD, KL, MOPD, RLCR, MR1–MR15, v.v.); 84 bài khác có câu hỏi dựa trên chính mục tiêu học tập, tiêu đề bài, chủ đề công thức và cầu nối chương.
- 4 câu quiz ở chương HS, 10 nguồn learning science từ các bài review/meta-analysis và tài liệu chính thống.
- CSV liệt kê cả 114 × 3 câu hỏi để kiểm toán chất lượng.

## Khung phương pháp — phân biệt bằng chứng

1. **Feynman Technique**: protocol học thực hành (giải thích → tìm lỗ hổng → xem lại → giảng lại), được hỗ trợ gián tiếp bởi nghiên cứu self-explanation, learning by teaching, retrieval practice; đừng hiểu như một phương pháp được chứng minh trực tiếp bởi một thử nghiệm duy nhất.
2. **First-principles reasoning**: lập luận từ định nghĩa, giả định và các ràng buộc; là heuristic nghiên cứu/phương pháp luận, KHÔNG mặc nhiên chứng minh thuật toán đúng ngoài thực tế.
3. **Synthetic Mastery**: thuật ngữ do website định nghĩa cho **lắp ráp kiến thức + transfer sang vấn đề mới + falsification/verification**. Đây KHÔNG phải tên một construct độc lập đã có xác nhận thực nghiệm riêng; nền tảng gồm generative learning, transfer, retrieval, self-explanation.

## Cách sử dụng

1. Mở file HTML qua trình duyệt, chọn mục **HS — Feynman → First Principles → Synthesis** dưới lộ trình để đọc hướng dẫn và research references.
2. Mở bất kỳ bài học (ví dụ `GRPO`, `RLCR`, `MR5`), cuộn tới **Learning Studio** ngay trước quiz và mở phần đó.
3. Không xem lại nội dung khi viết lần đầu. Trả lời ba câu, bổ sung ví dụ và chứng minh/đối chứng sau khi kiểm tra nguồn.
4. Sử dụng “Mở checklist để tự đối chiếu” và “Tự xác nhận sau khi kiểm” để ghi lại tiến độ **tự đánh giá**. Việc này không tự động thay đổi điểm quiz.
5. Bấm “Xuất ghi chú JSON” để sao lưu. Bấm “Ôn lại sau ≥48 giờ” để lưu vòng cũ và làm lại từ trống (vòng cũ có thể xem lại ở mục history).

## Lưu trữ và quyền riêng tư

- Ghi chú được lưu *riêng trên trình duyệt này* bằng `localStorage`, khoá `mopd_learning_studio_notes_v4`.
- Ghi chú KHÔNG gửi đến backend và KHÔNG đồng bộ với tài khoản; chức năng login và đồng bộ quiz cũ giữ nguyên.
- Ở một số chế độ chạy HTML cục bộ, trình duyệt có thể chặn localStorage. Nên xuất JSON trước khi đóng tab hoặc chuyển thiết bị.
- Không có AI grading hoặc thang điểm đo độ thông thạo thật sự. Checkbox chỉ phản ánh tự xác nhận, không phải kết quả đánh giá khoa học.

## Nguồn learning science (kiểm tra 27/10/2026)

- University of York — Feynman Technique: https://subjectguides.york.ac.uk/study-revision/feynman-technique
- Bisra et al. (2018) — Inducing Self-Explanation: https://doi.org/10.1007/s10648-018-9434-x
- Kobayashi (2019) — Learning by Preparing-to-Teach and Teaching: https://doi.org/10.1111/jpr.12221
- Fiorella & Mayer (2016) — Eight Ways to Promote Generative Learning: https://eric.ed.gov/?id=EJ1120458
- Fiorella (2023) — Making Sense of Generative Learning: https://link.springer.com/article/10.1007/s10648-023-09769-7
- Dunlosky et al. (2013) — Effective Learning Techniques: https://doi.org/10.1177/1529100612453266
- Roediger & Karpicke (2006) — Test-Enhanced Learning: https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Karpicke & Blunt (2011) — Retrieval Practice: https://pubmed.ncbi.nlm.nih.gov/21252317/
- National Research Council (2000) — Learning and Transfer: https://www.nationalacademies.org/read/9853/chapter/6
- Chi & Wylie (2014) — ICAP Framework: https://doi.org/10.1080/00461520.2014.965823

## Kiểm thử kỹ thuật

- Trích xuất JavaScript và `node --check`: PASS.
- Tạo lời dẫn và cấu trúc Learning Studio cho 114/114 bài: PASS, mỗi bài 3 câu và 3 textareas.
- Chromium headless qua `page.set_content`: 116 mục menu, có đủ Guide HS: PASS.
- Chuyển giữa các bài `MOPD ↔ RLCR`, thử ghi chú và checkbox trong cùng phiên: PASS.
- Chromium mobile viewport 390px, đo scrollWidth=clientWidth=390px, ảnh minh họa: PASS.
- Không kiểm thử backend thực tế hoặc quá trình đồng bộ tài khoản. Do chính sách môi trường chạy test, không kiểm tra được localStorage *xuyên các phiên trình duyệt* bằng HTTP/file origin; code có lưu cục bộ bằng API localStorage chuẩn và bắt lỗi quyền truy cập.

## Phiên bản

v4 xây trên v3 và giữ nguyên 15 bài MOPD Research Track, bài RLCR, quiz, visualizations và các GPU Labs. Không thay thế nội dung các bài bằng tóm tắt hay sửa các kết luận nghiên cứu mà không kiểm chứng.
