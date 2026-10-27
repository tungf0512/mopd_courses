# Đài Quan Sát MOPD — Research Edition v3 (RLCR)

Ngày cập nhật: 24/10/2026. Nguồn mã xuất phát từ `mopd-course-research-edition-v2.html` và giữ nguyên các bài cũ, interface, tài khoản/progress workflows. **Không ghi đè bản v2.**

## Nội dung mới: MR15 — Reinforcement Learning from Collective Rewards

- Bài học nghiên cứu 14 mục (`MR15.1`–`MR15.14`): hệ thống CEO/specialists shared-parameter; formalism joint REINFORCE; collective return vs advantage; CISPO với K=16/upper clip 5; GKPO và Kelly family; curricula (horizon, environment, task); policy action masking; benchmarking và matched-token/latency; hierarchy & causal confounders; COMA/MAPPO/QMIX/PARL; organisational-insularity safety; research questions, failure modes.
- 7 khối phân tích công thức (mathdeep), 3 bài code có thể sao chép, 2 visualization có sliders, 7 câu quiz với giải thích, 6 tài liệu tham khảo chuẩn.
- Điều hướng và tiến độ học tập tự động bao gồm MR15; bổ sung glossary, roadmap và crosslinks từ các bài liên quan.
- File `rlcr_toy_lab.py`: NumPy standalone chạy demo 2-agent role-conditioned shared policy, leave-one-out global advantage, finite difference gradient check. Chạy `python rlcr_toy_lab.py`; yêu cầu Python 3 + numpy.

## Nguồn khoa học

1. Zarov, Course, Hartshorn et al. (2026), *Avalon-M1: Reinforcement Learning from Collective Rewards*, primary technical report **under revision**, công bố 23/10/2026: https://www.gr.inc/avalonm1.pdf . Đã kiểm tra phần methodology (pp. 9–13), results, safety và Appendix H.
2. Trang công bố chính thức: https://www.gr.inc/releases/avalon-m1
3. Yu et al., *The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games* (NeurIPS 2022): https://proceedings.neurips.cc/paper_files/paper/2022/hash/9c1535a02f0ce079433344e14d910597-Abstract.html
4. Foerster et al., *Counterfactual Multi-Agent Policy Gradients* (AAAI 2018): https://ojs.aaai.org/index.php/AAAI/article/view/11794
5. Rashid et al., *QMIX* (ICML 2018): https://proceedings.mlr.press/v80/rashid18a.html
6. Kimi K2.5 / PARL: https://www.kimi.com/en/blog/kimi-k2-5

## Phạm vi và giới hạn

- Bài học phân biệt số liệu **self-reported** của nhóm Avalon với các suy luận lý thuyết và toy simulations.
- **RLCR không phải MOPD.** RLCR cập nhật nhiều instances của cùng một policy bằng shared collective advantage; MOPD học từ phân phối nhiều teacher.
- Paper không dùng on-policy distillation sau SFT; CISPO và GKPO là objectives dùng trong các môi trường khác nhau, không đồng nghĩa định nghĩa RLCR.
- Hai visualization chỉ mô phỏng ý tưởng, không trích xuất đường cong/định lượng từ paper.
- Model/harness/environments được tác giả thông báo sẽ phát hành sau; không khẳng định khả năng tái lập hiện tại. Mã NumPy chỉ là demo không tái lập thực nghiệm paper.
- Trang web tải Google Fonts & KaTeX từ CDN như bản v2; nếu mở offline hoàn toàn có thể không render công thức bằng KaTeX. Backend auth/progress chỉ có thể thử với server thực tế.

## Kiểm thử được thực hiện

- `node --check` đối với toàn bộ JavaScript inline: pass.
- Chromium headless (đã loại external CDN trong smoke test): bài MR15 render thành công, 14 heading, 7 mathdeep, 3 bài tập code, 2 interactive diagrams với sliders, 7 câu quiz. Quiz hiển thị lời giải; không có `pageerror` trong những thao tác được kiểm thử.
- Viewport 390px: không tràn ngang, width bằng 390px.
- `rlcr_toy_lab.py`: finite-difference gradient check pass; bài toy học phối hợp từ P≈0.25 lên P≈0.992 sau 700 iterations.

## Sử dụng

Tải HTML và mở bằng browser. Truy cập mục **MOPD Research Track · 2026 → MR15 — RLCR · Agent Organisations** trong sidebar. Để chạy lab: `python rlcr_toy_lab.py`.
