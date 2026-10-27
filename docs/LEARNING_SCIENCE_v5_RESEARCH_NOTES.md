# Đài Quan Sát MOPD — Learning Science Research Notes (v5)

**Ngày rà soát: 27/10/2026.** Đây là ghi chú thiết kế khóa học dựa trên các công trình learning sciences và cognitive psychology. Đừng diễn giải nó như một thử nghiệm chứng minh rằng website v5 tốt hơn v4: chưa có RCT hay kết quả học tập của học viên trên chính sản phẩm.

## Luận điểm thiết kế

Website AI Research nên dạy ba kết quả *khác nhau*:

1. **Acquisition:** người học hiểu bài ngay sau khi được hướng dẫn (ví dụ suy ra KL, nêu điểm khác GRPO/OPD).
2. **Retention:** không xem lời giải vẫn có thể tái dựng công thức hoặc giải thích sau một khoảng giãn.
3. **Transfer:** nhận ra cùng cơ chế khi mô hình, dữ liệu, giả định và objective thay đổi; tự chọn phương pháp, kiểm định bằng ví dụ phản chứng hoặc ablation.

Một người đọc paper rất trôi chảy không mặc nhiên có retention/transfer. Thời gian học, số chữ viết, số lần tick hay self-confidence cũng không đủ để chứng nhận mastery.

## Bản đồ từ bằng chứng đến thiết kế

| Research | Điều bằng chứng hỗ trợ | Design áp dụng | Giới hạn / rủi ro |
|---|---|---|---|
| Dunlosky et al. 2013 | Practice testing & distributed practice có utility cao hơn chỉ đọc lại/highlight trong nhiều điều kiện | Preflight, delayed retrieval | Không có guarantee cho tất cả kỹ năng hoặc mọi learner |
| Roediger & Karpicke 2006 | Retrieval có thể nâng delayed retention | Trả lời trước khi xem nội dung và sau khi ôn | Không coi quiz ngay sau bài là retention thật |
| Cepeda et al. 2006 | Spacing cải thiện recall; optimal lag thay đổi theo test delay | Bảng Ôn tập và lịch nhắc học | 1–3–7–14–30 là lịch gợi ý sản phẩm, không phải interval thần kinh tối ưu |
| Rohrer & Taylor 2007 | Mixed problems giúp phân biệt dạng bài trong thiết lập toán học đã thử | Interleaved comparison theo nhóm gần nhau | Không trộn mọi thứ một cách ngẫu nhiên; novice cần học nền trước |
| Renkl & Atkinson 2003 | Worked examples hiệu quả lúc đầu, fading phù hợp khi kỹ năng phát triển | Chế độ guided/mixed/independent | Hỗ trợ từ nguồn bài học, không tự nhận biết trình độ |
| Kirschner et al. 2006 | Minimal guidance rủi ro cho novice do giới hạn working memory | Tùy chọn novice scaffold trong từng bài | Vẫn cần bài độc lập để kiểm tra transfer |
| Chi & Wylie 2014 | ICAP phân loại hoạt động từ passive đến constructive/interactive | Prediction, derivation, teach-back, testable synthesis | Viết dài có thể chỉ là chép lại; engagement không tự chứng minh outcome |
| Kapur 2016 | Productive failure đòi hỏi thiết kế và consolidation phù hợp | Predict → attempt → feedback → revise | Không biến failure thành bài khó vô hướng |
| Kornell et al. 2009 | Unsuccessful retrieval có thể hữu ích khi sau đó nhận đáp án | Cho phép trả lời 'không biết', rồi xem rubric | Không khen sai vô điều kiện; cần feedback đúng |
| Butler 2010 | Repeated testing hỗ trợ transfer ở các loại suy luận nhất định | Novel transfer prompt sau giãn cách | Không suy rộng rằng mọi transfer đều tăng |
| Hattie & Timperley 2007 | Feedback về goal, current status, next steps | Criteria lấy từ learning objectives và summary của bài | Rubric không chấm đúng/sai tự động |
| NRC 2000 | Deep structured understanding cần cho transfer | Liên hệ cross-topic, đổi assumptions, thử code | Transfer phải đo bằng bài mới, không nhắc lại nguyên văn |

## Chu kỳ triển khai ở **mỗi bài** (115 bài có nội dung)

**Trước khi đọc (Preflight):**
- Viết những gì đã biết trước khi đọc; có thể ghi “chưa biết”.
- Chọn confidence 0–100% để về sau đối chiếu metacognitive calibration.
- Dùng `pre` / `learn` / `summary` từ bài gốc làm câu hỏi và checklist, tránh suy diễn đáp án ngoài nguồn.

**Trong bài (Pause & Predict):**
- Ở khoảng 42% thân bài (trước quiz), dừng và dự đoán giả định hoặc trường hợp failure.
- Chỉ mở tiêu chí/gợi ý sau khi đã dự đoán.
- Đây là prompt tự giải thích; không tự tạo ra đáp án đúng nếu paper chưa nói.

**Scaffolding theo mức nền:**
- **Guided:** trích đoạn giải thích / code explanation / tổng kết từ chính bài gốc, yêu cầu một bước thay đổi giả định.
- **Mixed:** đưa một cue ngắn, để learner cố giải rồi mới mở nội dung worked.
- **Independent:** giữ gợi ý ẩn để người học tự tạo phản ví dụ và kiểm chứng.
- Hệ thống không suy đoán trình độ cá nhân và không “nâng hạng” người dùng tự động.

**Cuối bài (Learning Studio v4 giữ nguyên):**
- Feynman = explain + compare source.
- First principles = assumptions + derivation.
- Synthetic Mastery = connect ideas + independent test.
- Các checkbox là tự đánh giá; chỉ test khác biệt được xem là bằng chứng mạnh hơn.

**Sau một khoảng giãn (Delayed Review):**
- Truy hồi nội dung không xem nguồn, so sánh với một bài gần về mục tiêu/assumptions.
- Mở rubric để có corrective feedback.
- Learner tự đánh giá 0/1/2, ghi nhận và lập lịch lại.
- Heuristic spacing: 1, 3, 7, 14, 30 ngày; chọn khác nhau theo kết quả tự đánh giá; **không có khả năng đo true mastery**.

## Ví dụ học thuật nên thêm vào ngân hàng bài tập

- **Reverse KL/Forward KL:** đóng tài liệu, viết định nghĩa; sau đó so sánh sampling distribution với chiều divergence; chỉ ra trường hợp student-generated states + forward token-KL.
- **GRPO/OPD:** dự đoán khi reward của tất cả rollout đồng hạng; so sánh tín hiệu outcome sparse với teacher log-ratio dày; thay sampling policy và xét bias.
- **MOPD:** trước khi đọc kết quả, dự đoán domain dài có thể chi phối loss theo token; chạy toy lab, kiểm chứng với optimizer và budget.
- **RLCR:** phân biệt joint reward và individual credit assignment; so collective reward cùng total token budget với single agent để tránh kết luận sai về compute.
- **Cross-tokenizer:** tự chỉ ra tại sao 2 vocab khác nhau không có token-level KL trực tiếp; đề xuất cách alignment và counterexample.
- **Concrete Score Distillation:** dự đoán tác động của cộng cùng một hằng số lên logits, chạy invariant test thay vì học thuộc.

## Thử nghiệm thực tế để kiểm chứng website v5

**Research question:** Liệu Learning Science v5 có nâng delayed retention / transfer trên khóa MOPD so với v4 khi giữ instructional time tương đương?

**Thiết kế sơ bộ**:
1. Pre-register learner population, 8–12 cặp bài (cùng domain), và outcomes trước khi nhận dữ liệu.
2. Thu pretest, đo prior expertise, rồi randomize v4/v5; cân bằng thời lượng và teacher contact.
3. Sau 7–14 ngày, kiểm tra delayed retrieval và các câu **new transfer** chưa xuất hiện trong training.
4. Chấm bằng rubric blind ít nhất 2 independent raters; định lượng agreement, thời gian, dropout, subjective load.
5. Báo hiệu quả với bootstrap/CI, hiệu chỉnh multiple comparisons ở secondary outcomes và sensitivity to attrition.
6. Điều kiện phủ định: v5 cải thiện completion nhưng không cải thiện delayed transfer, hoặc gây quá tải ở novice.

**Không đủ bằng chứng:** tăng lượt truy cập, nhiều note hơn, 100% quiz, độ tự tin tăng hoặc việc app nhắc ôn thường xuyên.

## Tài liệu gốc / trang tóm tắt học thuật

1. Dunlosky et al. (2013) — Effective Learning Techniques: https://www.psychologicalscience.org/journals/pspi/1529100612453266/
2. Roediger & Karpicke (2006) — Test-Enhanced Learning: https://doi.org/10.1111/j.1467-9280.2006.01693.x
3. Cepeda et al. (2006) — Distributed Practice: https://pubmed.ncbi.nlm.nih.gov/16719566/
4. Rohrer & Taylor (2007) — Shuffling Mathematics Problems: https://digitalcommons.usf.edu/psy_facpub/1767/
5. Renkl & Atkinson (2003) — Worked Example Fading: https://doi.org/10.1207/S15326985EP3801_3
6. Kirschner, Sweller & Clark (2006) — Minimal Guidance: https://doi.org/10.1207/s15326985ep4102_1
7. Chi & Wylie (2014) — ICAP: https://doi.org/10.1080/00461520.2014.965823
8. Butler (2010) — Repeated Testing and Transfer: https://pubmed.ncbi.nlm.nih.gov/20804289/
9. Kapur (2016) — Productive Failure: https://doi.org/10.1080/00461520.2016.1155457
10. Kornell, Hays & Bjork (2009) — Unsuccessful Retrieval: https://pubmed.ncbi.nlm.nih.gov/19586265/
11. Hattie & Timperley (2007) — Feedback: https://doi.org/10.3102/003465430298487
12. National Research Council (2000) — Learning and Transfer: https://www.nationalacademies.org/read/9853/chapter/6
13. Bisra et al. (2018) — Self-Explanation Meta-Analysis: https://doi.org/10.1007/s10648-018-9434-x
14. Karpicke & Blunt (2011) — Retrieval Practice vs Concept Mapping: https://pubmed.ncbi.nlm.nih.gov/21252317/

## Khả năng / giới hạn của triển khai kỹ thuật

- Offline HTML + JavaScript, không phụ thuộc AI grading, không gửi phản hồi tự do tới dịch vụ chấm bài.
- V5 dùng localStorage riêng (`mopd_learning_science_v5`), v4 notes giữ khóa `mopd_learning_studio_notes_v4` để tránh ghi đè dữ liệu cũ.
- Bảng ôn trong sidebar hiện các lesson đã lập lịch; có xuất chung dữ liệu v4 + v5 ra JSON.
- Ngày học tính theo đồng hồ máy cá nhân, có thể bị lệch nếu thay đổi giờ hoặc đổi thiết bị.
- Ở file HTML cục bộ, trình duyệt có thể chặn storage; nên xuất JSON định kỳ. Chưa có đồng bộ v5 với tài khoản/backend.
- **Không** chấm độ đúng văn bản tự do, không tự phát hiện misconceptions, không chứng minh một learner đã đạt research mastery.
