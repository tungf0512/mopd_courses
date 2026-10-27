# Đài Quan Sát MOPD — Research Edition v2 (24/10/2026)

## Nội dung thay đổi trong lần này

**Giữ nguyên nội dung và tính năng của Research Edition trước đó.** Bổ sung vào nhóm nền tảng và mở rộng researcher:

- **MR1 (nâng cấp):** Hinton temperature KD và hệ số T², so sánh DAgger / Sequence KD / MiniLLM / GKD; bài tập tính entropy và nguồn GKD riêng. Lưu ý MiniLLM và GKD: bản đầu arXiv 2023, đăng ICLR 2024.
- **MR12 — One Student, Many Teachers / PromptSD (Ma et al., arXiv:2607.18293):** đào tạo teacher bằng soft prompts trên frozen backbone; công thức hai giai đoạn; teacher families; giới hạn khả năng tổng quát hóa; toy routing audit; bài tập ablation; references và quiz.
- **MR13 — When Top-K Misses the Decision (Shen et al., arXiv:2607.07050v6):** retained teacher probability mass ≠ đủ thông tin gradient cho tool call; teacher-vs-student support union; trade-off over-calling/required-call recall; visualization top-K tương tác, numerical audit và quiz. Công thức gradient cross-entropy được đánh dấu là ví dụ, KHÔNG phải restricted JSD loss của paper.
- **MR14 — Distillation of Large Language Models via Concrete Score Matching (Kim et al., ICLR 2026):** Concrete Score Distillation/CSD, logit-shift invariance, khác biệt so với direct logit MSE và probability KL; ví dụ gradient-size và chi phí; visualization logit shift, mã toy unit tests, bài tập và quiz.
- **Liên kết ngược:** lộ trình, glossary, Chương 4, Chương 6, MR10 đã có ghi chú và references dẫn tới MR12–MR14.

### Sources chính xác

- DAgger: https://proceedings.mlr.press/v15/ross11a.html
- Hinton KD: https://arxiv.org/abs/1503.02531
- Sequence KD: https://aclanthology.org/D16-1139/
- MiniLLM: https://arxiv.org/abs/2306.08543
- GKD / On-Policy Distillation: https://arxiv.org/abs/2306.13649
- PromptSD: https://arxiv.org/abs/2607.18293
- Top-K decision-critical support: https://arxiv.org/abs/2607.07050
- Concrete Score Distillation (ICLR 2026): https://proceedings.iclr.cc/paper_files/paper/2026/hash/1bfc9f74afa91b9b8add5a97a97001a1-Abstract-Conference.html

## Khởi chạy

Mở `mopd-course-research-edition-v2.html` bằng trình duyệt desktop/mobile hiện đại. Có thể serve file bằng `python -m http.server 8000`. Để lấy math/fonts chất lượng tối ưu cần CDN (KaTeX + Google Fonts). Trong sidebar tìm “MOPD Research Track · 2026”, MR12–MR14.

Các file `examples/mr1_temperature.py`, `mr12.py`, `mr13.py`, `mr14.py` chạy với `numpy` (`pip install numpy`). Toy GPU lab cũ `toy_mopd_budget.py` yêu cầu `torch`.

## Những kiểm thử đã chạy

- `node --check` kiểm tra JavaScript chính của HTML.
- Chromium + Playwright: desktop kiểm thử mở MR1/MR2/MR11/MR12/MR13/MR14, thử quiz và hai viz; mobile kiểm thử MR14, sidebar, overflow và lỗi JS.
- Chạy tất cả bốn ví dụ Python mới trong thư mục examples.
- Bảo toàn file Research Edition gốc; đây là file độc lập phiên bản v2.

## Giới hạn được công bố

- Các code toy **không** tái hiện nguyên văn training quy mô LLM của các papers; thông tin được phân biệt rõ trong nội dung mỗi bài.
- Chưa thử backend tài khoản và đồng bộ API thực tế; cấu trúc backend cũ vẫn được giữ nguyên.
- Chưa tái lập độc lập accuracy/benchmark được paper báo cáo.
- Các bài khác của website ngoài vùng nâng cấp này không được audit lại toàn bộ về mặt nội dung.
