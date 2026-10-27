from pathlib import Path
import json,re
SRC=Path('/mnt/data/mopd-course-research-edition-v4-learning-studio.html')
OUT=Path('/mnt/data/mopd-course-research-edition-v5-learning-science.html')
s=SRC.read_text(encoding='utf-8')

sources=[
 ('Dunlosky et al. (2013) — Improving Students’ Learning with Effective Learning Techniques','https://www.psychologicalscience.org/journals/pspi/1529100612453266/','Review: practice testing, distributed practice có bằng chứng mạnh; self-explanation/interleaving có điều kiện.'),
 ('Roediger & Karpicke (2006) — Test-Enhanced Learning','https://doi.org/10.1111/j.1467-9280.2006.01693.x','Retrieval sau khi học hỗ trợ lưu giữ lâu dài; không chỉ đo mức học.'),
 ('Cepeda et al. (2006) — Distributed Practice: Quantitative Synthesis','https://pubmed.ncbi.nlm.nih.gov/16719566/','Spacing effect; khoảng giãn phù hợp phụ thuộc mốc cần nhớ.'),
 ('Rohrer & Taylor (2007) — Shuffling Mathematics Problems Boosts Learning','https://digitalcommons.usf.edu/psy_facpub/1767/','Interleaving giúp phân biệt problem types trong thiết lập đã thử.'),
 ('Renkl & Atkinson (2003) — Transition from Worked Examples to Problem Solving','https://doi.org/10.1207/S15326985EP3801_3','Example fading: giảm guidance khi expertise tăng.'),
 ('Kirschner, Sweller & Clark (2006) — Why Minimal Guidance Does Not Work','https://doi.org/10.1207/s15326985ep4102_1','Cognitive load; novice nên được hướng dẫn có cấu trúc.'),
 ('Chi & Wylie (2014) — ICAP Framework','https://doi.org/10.1080/00461520.2014.965823','Phân biệt passive, active, constructive, interactive engagement.'),
 ('Butler (2010) — Repeated Testing Produces Superior Transfer','https://pubmed.ncbi.nlm.nih.gov/20804289/','Retrieval có thể hỗ trợ transfer sang câu hỏi suy luận mới trong thiết lập nghiên cứu.'),
 ('Kapur (2016) — Examining Productive Failure','https://doi.org/10.1080/00461520.2016.1155457','Productive failure cần giai đoạn consolidation và thiết kế thích hợp.'),
 ('Kornell, Hays & Bjork (2009) — Unsuccessful Retrieval Attempts Enhance Subsequent Learning','https://pubmed.ncbi.nlm.nih.gov/19586265/','Thử nhớ sai có thể hữu ích nếu sau đó được cung cấp feedback chính xác.'),
 ('Hattie & Timperley (2007) — The Power of Feedback','https://doi.org/10.3102/003465430298487','Feedback: mục tiêu, tiến độ và bước tiếp theo; chú trọng task/process/self-regulation.'),
 ('National Research Council (2000) — How People Learn: Learning and Transfer','https://www.nationalacademies.org/read/9853/chapter/6','Transfer cần nắm sâu khái niệm và khả năng nhận diện ứng dụng mới.')
]

science_chapter={
 'id':'learning-science-lab','group':'Học cách học · Research Skills','num':'LS','short':'Learning Science · Evidence & Design',
 'title':'Learning Science for AI Researchers — Từ đọc hiểu đến năng lực truy hồi, chuyển giao và phản chứng',
 'lede':'Học để đọc được paper hôm nay; truy hồi được một tuần sau; tự suy luận khi gặp thuật toán chưa từng thấy.',
 'blocks':[
 {'t':'meaning','why':'Bài nền tảng của bản Research Edition v5: giải thích bằng chứng về spaced retrieval, cognitive load, worked examples, feedback, interleaving, transfer và metacognitive calibration. Phần giao diện biến những nguyên lý đó thành hành động trong các bài AI/RL. Đây là thiết kế dựa trên nghiên cứu, chưa phải hiệu quả giáo dục đã được thử nghiệm trên chính website.',
  'learn':['Phân biệt việc đọc thấy quen với retrieval không xem nguồn, và hiểu vì sao đo ngay sau khi đọc dễ lạc quan.','Chọn phương pháp hướng dẫn phù hợp giữa novice/expert, tránh quá tải cognitive load.','Thiết kế một bài interleaving có feedback và một delayed transfer test để đánh giá học sâu.','Tự tổ chức một thử nghiệm A/B đánh giá lợi ích của Learning Studio bằng đo lường có kiểm soát.'],
  'pre':'HS: Feynman / First Principles / Synthetic Mastery; nếu chưa có nền tảng RL hãy thử ví dụ từ F1 trước.','next':'Áp dụng Preflight → Pauses → Learning Studio → Delayed Review ở F1, GRPO, KL, MOPD và MR15.'},
 {'t':'h3','idx':'LS.1','x':'Đọc trôi chảy không phải là nhớ được hay áp dụng được'},
 {'t':'p','x':'Ba kết quả cần tách: (1) <b>performance trong khi đang đọc</b>, (2) <b>retention</b> sau một khoảng thời gian không nhìn nguồn, và (3) <b>transfer</b> sang tình huống/giả định mới. Việc thấy một công thức dễ hiểu ngay sau khi đọc không bảo đảm hai kết quả còn lại. Website vì vậy không gán nhãn mastery chỉ vì bạn tick checklist, viết dài hoặc hoàn thành một quiz ngay lập tức.'},
 {'t':'cards2','cards':[{'c':'var(--halo)','h':'Immediate performance','p':'Giải được khi đáp án hoặc công thức vẫn ở gần. Thích hợp chẩn đoán bước học, không đủ để khẳng định nhớ lâu.'},{'c':'var(--glm)','h':'Delayed retention','p':'Không nhìn nguồn, cố nhớ khái niệm, estimator, assumptions sau nhiều ngày; nhận phản hồi khi sai.'},{'c':'var(--mimo)','h':'Novel transfer','p':'Đổi domain, thay giả định, so sánh method gần nhau, dự đoán failure mode rồi kiểm chứng.'}]},
 {'t':'h3','idx':'LS.2','x':'Retrieval practice: Nhớ trước khi nhìn lại'},
 {'t':'p','x':'Dunlosky et al. đánh giá <b>practice testing</b> và <b>distributed practice</b> ở mức độ hữu dụng cao trên nhiều điều kiện học. Roediger & Karpicke cho thấy retrieval có thể cải thiện long-term retention so với chỉ học lại. Trong website: trước bài có Preflight chưa lộ đáp án; cuối bài có câu hỏi truy hồi; vòng sau bắt đầu từ blank page trước khi xem checklist. Nếu không nhớ được, mở feedback rồi thử lại, thay vì để bài mãi không hoàn thành.'},
 {'t':'note','title':'Không biến retrieval thành kiểm tra áp lực','x':'Nếu mới bắt đầu và không có chút kiến thức nền, một ví dụ có hướng dẫn là phù hợp hơn việc buộc tự suy luận trong vô vọng. Pretesting có thể hữu ích, nhưng khi câu trả lời sai phải có phần đối chiếu chính xác.'},
 {'t':'h3','idx':'LS.3','x':'Spacing: Đặt lịch ôn có cơ sở, không giả vờ tính độ nhớ chính xác'},
 {'t':'p','x':'Cepeda et al. tổng hợp 317 thí nghiệm về distributed practice: hiệu quả phụ thuộc cả khoảng giãn giữa các phiên và thời điểm kiểm tra cuối. Website dùng lịch <b>heuristic</b> 1–3–7–14–30 ngày để nhắc thực hành, tự điều chỉnh theo đánh giá sau retrieval. Các khoảng này <b>không phải</b> lịch tối ưu cho mọi kỹ năng, không phải thuật toán suy luận xác suất người học đã thành thạo.'},
 {'t':'h3','idx':'LS.4','x':'Cognitive load: Guided → Partially faded → Independent'},
 {'t':'p','x':'Renkl & Atkinson mô tả worked-example fading: ở giai đoạn đầu, lời giải từng bước giảm gánh nặng tìm kiếm; khi nền tảng tăng, chuyển dần sang tự giải. Kirschner–Sweller–Clark phản biện sự hướng dẫn tối thiểu với novice. Vì vậy mỗi bài có lựa chọn <b>Mới bắt đầu / Đã có nền tảng / Tự nghiên cứu</b>. Tùy chọn này điều khiển mức gợi ý, <i>không</i> tự khẳng định trình độ người học.'},
 {'t':'code','title':'Worked example → faded step → independent check','lang':'Python / NumPy',
  'prompt':'<p><b>Worked:</b> Với teacher [0.7,0.3] và student [0.5,0.5], tính full-vocab reverse KL bằng <code>sum(s * (log(s)-log(t)))</code>. <b>Faded:</b> sửa cách tính để giữ ổn định log(0). <b>Independent:</b> thay student bằng [0.9,0.1], dự đoán KL tăng hay giảm, chạy kiểm tra.</p>',
  'solution':"import numpy as np\nt=np.array([.7,.3])\ndef rkl(student,teacher):\n    s=np.asarray(student,dtype=float);t=np.asarray(teacher,dtype=float)\n    assert np.all(s>0) and np.all(t>0)\n    return float(np.sum(s*(np.log(s)-np.log(t))))\nfor s in [[.5,.5],[.9,.1]]: print(s,round(rkl(s,t),6))\n# Câu trả lời: kết quả không thể suy ra chính xác chỉ từ độ 'sắc nét' riêng lẻ.",
  'explain':'So sánh các giá trị số và phân tích độ lệch với teacher trước khi kết luận. Với các zero probabilities cần xác định support và dùng cách xử lý log-domain hợp lệ; epsilon tùy tiện làm thay đổi phân phối mục tiêu.'},
 {'t':'h3','idx':'LS.5','x':'Interleaving: Học phân biệt trước khi học giải nhanh'},
 {'t':'p','x':'Interleaving không phải xáo ngẫu nhiên mọi môn. Nó hữu ích nhất khi learner phải học cách <b>nhận diện đúng loại bài toán/thuật toán</b> trong số những phương pháp dễ nhầm: reverse KL vs forward KL, GRPO vs OPD vs RLCR, sampled-token vs full-vocab estimators, routing vs optimizer conflict. Bài luyện hỗn hợp nên theo sau một mức kiến thức cơ bản ở từng mục, và đi kèm phản hồi vì sao lựa chọn khác sai.'},
 {'t':'h3','idx':'LS.6','x':'ICAP và self-explanation: hoạt động phải tạo kiến thức mới'},
 {'t':'p','x':'ICAP (Chi & Wylie) phân biệt Passive, Active, Constructive và Interactive dựa trên hoạt động nhận thức quan sát được. Một textarea dài không tự động là “constructive”: người học có thể chép lại nguyên văn. Với AI research, sản phẩm constructive là một derivation, counterexample, một dự đoán có thể bác bỏ hoặc một thí nghiệm có kiểm soát.'},
 {'t':'h3','idx':'LS.7','x':'Productive failure: cố thử có kiểm soát, rồi học từ phản hồi'},
 {'t':'p','x':'Kapur phân biệt productive failure với thất bại vô ích. Website ưu tiên chu kỳ <b>prediction → attempt → worked answer/criteria → revision</b> thay vì bắt người mới lao vào bài toán không biết giải. Kornell et al. cũng cho thấy thử truy hồi thất bại có thể hỗ trợ học sau đó khi được cho đáp án. Với bài cao cấp, yêu cầu dự đoán dấu của gradient / tác động clipping trước khi chạy code; rồi giải thích chênh lệch giữa prediction và observation.'},
 {'t':'h3','idx':'LS.8','x':'Feedback phải chỉ ra sai ở đâu và bước nào tiếp theo'},
 {'t':'p','x':'Theo Hattie & Timperley, feedback hữu ích nên làm rõ mục tiêu, tiến độ và bước tiếp theo, ở mức task/process/self-regulation. Vì vậy các Preflight và Checkpoint có tiêu chí cần đối chiếu với nguồn, và review có rubric ngắn. Tự đánh giá <b>không phải chấm đúng-sai tự động</b>; mã nguồn không có mô hình AI đánh giá câu trả lời tự do.'},
 {'t':'h3','idx':'LS.9','x':'Metacognitive calibration và delayed assessment'},
 {'t':'p','x':'Tự tin 90% không đồng nghĩa hiểu đúng 90%. Trước bài, ghi mức tự tin và thử giải; sau bài, tự chấm mức nhớ. Khi ôn, ghi kết quả retrieval trước khi mở checklist để so sánh niềm tin và kết quả thực tế. Dữ liệu tự báo cáo có thể bị lệch, nên không suy ra kiến thức thật từ một slider tự tin.'},
 {'t':'h3','idx':'LS.10','x':'Blueprint: cùng một chủ đề, ba mức năng lực'},
 {'t':'cards2','cards':[{'c':'var(--moon)','h':'Novice · hiểu và sửa','p':'Xem worked example, phân tích bước sai, sau đó giải tương tự với 1 bước để trống.'},{'c':'var(--halo)','h':'Intermediate · phân biệt','p':'Dự đoán trước, tự dựng công thức, luyện một bài interleaved trong nhóm phương pháp gần nhau.'},{'c':'var(--glm)','h':'Researcher · transfer','p':'Đổi một giả định, tự thiết kế ablation, so sánh compute/failure modes và trả lời không xem nguồn.'}]},
 {'t':'h3','idx':'LS.11','x':'Không hứa hẹn hiệu quả chưa được kiểm chứng trên website'},
 {'t':'warn','title':'Giới hạn bằng chứng','x':'Các kết quả trên đến từ thí nghiệm học tập với tài liệu, học sinh/sinh viên và nhiều bối cảnh; không có thử nghiệm ngẫu nhiên chứng minh chính bản MOPD website này giúp researcher học sâu hơn. Thứ tự 1–3–7–14–30, mức hướng dẫn, lựa chọn câu hỏi và dashboard là <b>giả thuyết thiết kế sản phẩm</b>, không phải “công thức của não bộ”. Feynman Technique và Synthetic Mastery là nhãn thực hành, không được coi là phương pháp chuẩn hóa có RCT riêng.'},
 {'t':'h3','idx':'LS.12','x':'Cách đánh giá xem nâng cấp này có thực sự tốt hơn v4'},
 {'t':'ol','items':['Chọn 8–12 cặp chủ đề gần nhau (GRPO/OPD; forward/reverse KL; MOPD/RLCR) và xây delayed transfer test không xuất hiện nguyên văn trong bài.','Randomize learner hoặc block theo prior knowledge vào v4-control và v5-intervention; giữ thời gian học và quiz exposure tương tự.','Pre-register chỉ số chính: điểm delayed transfer sau 7–14 ngày, kèm retention, tỷ lệ bỏ cuộc và thời gian làm bài.','Chấm blind bởi rubric chuyên gia; đánh giá độ nhất trí giữa người chấm, không lấy số chữ hay self-check làm kết quả học tập.','Báo cáo khoảng tin cậy, missing data, subgroup novice/expert và adverse effects như quá tải hoặc tăng thời gian.']},
 {'t':'summary','items':['Practice testing + distributed practice có cơ sở thực nghiệm mạnh; scheduling chính xác của ứng dụng chỉ là heuristic.','Novice cần worked examples và guidance; expert có thể cần bài independent transfer khó hơn, không bắt tất cả học cùng cách.','Feedback và retrieval sau khoảng giãn quan trọng hơn số chữ người học viết hoặc tốc độ hoàn thành quiz.','Interleaving hữu ích cho phân biệt phương pháp gần nhau; không nên trộn các khái niệm không có liên hệ.','Muốn nói sản phẩm cải thiện học tập phải có thử nghiệm delayed retention/transfer với đối chứng.']},
 {'t':'reflist','title':'Nghiên cứu gốc và literature review — kèm phạm vi áp dụng','items':[{'t':a,'u':b,'d':c} for a,b,c in sources]},
 {'t':'quiz','qs':[
 {'q':'Bạn vừa đọc xong một bài KL và trả lời quiz chính xác. Điều gì là bằng chứng tốt hơn cho khả năng lưu giữ?','opts':['Đã cuộn hết bài','Không xem nguồn và giải lại sau một tuần','Viết lại công thức 20 lần trong cùng buổi','Chỉ đánh dấu tự tin 100%'],'a':1,'exp':'Đánh giá trì hoãn khi không nhìn nguồn ít bị ảnh hưởng bởi familiarity ngay sau khi đọc.'},
 {'q':'Vì sao novice không nên bắt đầu mọi bài với productive failure rất khó?','opts':['Vì bài khó luôn vô ích','Vì guidance/working memory giới hạn; cần kết hợp với consolidation và worked example','Vì chỉ quiz mới có giá trị','Vì người mới không thể học RL'],'a':1,'exp':'Kết quả về worked-example fading và guided instruction phụ thuộc vào prior knowledge.'},
 {'q':'Cặp nào phù hợp cho interleaving trong khóa?','opts':['MOPD và kiểu font chữ','Reverse KL và forward KL','Neural nets và menu điện thoại','Các màu chủ đề giao diện'],'a':1,'exp':'Interleaving phù hợp khi cần học cách phân biệt các problem types dễ nhầm.'},
 {'q':'Lịch 1–3–7–14–30 ngày có phải lịch tối ưu đã được chứng minh cho mọi sinh viên và mọi kỹ năng?','opts':['Có, là lịch tối ưu phổ quát','Không: đây là lịch gợi ý; độ giãn tối ưu phụ thuộc bối cảnh và thời điểm kiểm tra','Có, nhưng chỉ với GRPO','Không cần ôn tập cách quãng'],'a':1,'exp':'Spacing effect có bằng chứng mạnh; lịch tối ưu cụ thể không phổ quát.'},
 {'q':'Cách nào đo được Synthetic Mastery đáng tin nhất?','opts':['Độ dài bài viết','Số lần mở website','Delayed transfer trên bài mới có rubric và chấm độc lập','Số lần bấm nút hoàn thành'],'a':2,'exp':'Một bài mới và chấm độc lập tránh nhầm hành vi trên UI với năng lực thực sự.'},
 ]}
 ]
}
chapter_js='\n/* Learning Science v5 — evidence-based design module */\nconst LEARNING_SCIENCE_V5 = '+json.dumps(science_chapter,ensure_ascii=False)+';\nLESSONS.splice(LESSONS.findIndex(l=>l.id===\'learning-science\')+1,0,LEARNING_SCIENCE_V5);\n'
needle='/* ===== Learning Studio: exercise scaffolds grounded in current lesson ===== */'
assert s.count(needle)==1
s=s.replace(needle,chapter_js+'\n'+needle)

css='''
/* ===== Research Edition v5 · Evidence-based Learning Science ===== */
.sc-preflight,.sc-review,.sc-pause{margin:20px 0;border:1px solid var(--line);border-radius:14px;background:var(--surface);overflow:hidden}
.sc-preflight>summary,.sc-review>summary,.sc-pause>summary{padding:13px 16px;display:flex;justify-content:space-between;gap:10px;align-items:center;cursor:pointer;font-family:var(--f-display);font-weight:600;font-size:14px}
.sc-preflight>summary{background:rgba(132,166,230,.07)}
.sc-pause>summary{background:rgba(79,208,170,.055)}
.sc-review>summary{background:rgba(242,233,206,.065)}
.sc-inner{padding:15px 18px 18px;border-top:1px solid var(--line-soft)}
.sc-eyebrow{font:600 10px var(--f-mono);letter-spacing:.12em;color:var(--halo);text-transform:uppercase}
.sc-desc,.sc-small{color:var(--text-dim);font-size:12.5px;line-height:1.65;margin:9px 0}
.sc-q{font-size:14.5px;line-height:1.6;margin:12px 0;color:var(--text)}
.sc-input{display:block;width:100%;min-height:76px;resize:vertical;border:1px solid var(--line);border-radius:9px;padding:12px 13px;background:var(--sky-deep);color:var(--text);font:13.5px/1.65 var(--f-body)}
.sc-input:focus{outline:1px solid var(--halo)}
.sc-buttons{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:10px 0}
.sc-btn{border:1px solid var(--line);border-radius:9px;padding:8px 11px;background:var(--surface-2);color:var(--text);font:600 12px var(--f-body);cursor:pointer}
.sc-btn:hover{border-color:var(--halo)}
.sc-btn:disabled{opacity:.5;cursor:default}
.sc-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.sc-rubric{margin:8px 0;padding:12px 14px;background:var(--surface-2);border-left:3px solid var(--halo);border-radius:8px}
.sc-rubric>summary{font-weight:600;font-size:12.5px;cursor:pointer;color:var(--halo)}
.sc-rubric ul{padding-left:18px;font-size:13px;color:var(--text-dim);margin:9px 0}
.sc-metabox{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:10px 0;font-size:12.5px}
.sc-metabox select,.sc-metabox input[type=range]{accent-color:var(--halo)}
.sc-metabox select{color:var(--text);background:var(--surface-2);border:1px solid var(--line);border-radius:8px;padding:7px 9px}
.sc-due{color:var(--moon);font:500 11px var(--f-mono)}
.sc-dash{margin:16px 12px;padding:13px;background:var(--surface);border:1px solid var(--line-soft);border-radius:10px}
.sc-dash h3{font-size:13px;font-family:var(--f-display);margin-bottom:6px}
.sc-dash p{font-size:11px;color:var(--text-dim);margin:5px 0 8px}
.sc-dashboard-list{list-style:none;margin:8px 0;padding:0;max-height:160px;overflow-y:auto}
.sc-dashboard-list li{padding:6px 0;border-bottom:1px solid var(--line-soft)}
.sc-dashboard-list button{border:0;background:transparent;color:var(--halo);font-size:12px;text-align:left;cursor:pointer}
.sc-footnote{font-size:11px;color:var(--text-faint);line-height:1.6}
@media(max-width:640px){.sc-grid{grid-template-columns:1fr}.sc-preflight>summary,.sc-review>summary,.sc-pause>summary{align-items:flex-start}}
'''
assert s.count('</style>')==1
s=s.replace('</style>',css+'\n</style>')

# Persistent hub, near nav bottom. No destructive changes to existing state.
hub_html='''<div class="sc-dash" id="sc-hub" aria-label="Ôn tập dựa trên khoa học học tập"><h3>◷ Learning Review</h3><p id="sc-hub-count">Bài cần ôn dựa trên lịch bạn tự thiết lập</p><ol class="sc-dashboard-list" id="sc-hub-list"></ol><button type="button" class="sc-btn" id="sc-hub-export">Xuất toàn bộ dữ liệu v5</button><p class="sc-footnote">Nhắc ôn là lịch thực hành, không phải chứng nhận mastery.</p></div>\n'''
assert s.count('<div class="side-foot">')==1
s=s.replace('<div class="side-foot">',hub_html+'<div class="side-foot">')

# v5 JS source
v5_js=r'''
/* ===============================================
   LEARNING SCIENCE ENGINE · v5
   Retrieval → corrective feedback → spacing → transfer
   No server AI grading or psychometric mastery inference.
   =============================================== */
const SC_KEY='mopd_learning_science_v5';
const SC_STATE=(()=>{try{const o=JSON.parse(localStorage.getItem(SC_KEY)||'{}');return o&&typeof o==='object'&&!Array.isArray(o)?o:{};}catch(e){return {};}})();
let SC_MODE='guided';
try{SC_MODE=localStorage.getItem('mopd_sc_mode_v5')||'guided';}catch(e){}
function scSave(){try{localStorage.setItem(SC_KEY,JSON.stringify(SC_STATE));}catch(e){}}
function scRecord(l){return SC_STATE[l.id]||(SC_STATE[l.id]={prior:'',confidence:40,checks:{},reviewText:'',reps:0,due:0,logs:[]});}
function scEscape(x){return lsEsc(String(x||''));}
function scMean(l){return (l.blocks||[]).find(x=>x.t==='meaning')||{};}
function scCriteria(l){
 const m=scMean(l), a=(m.learn||[]).slice(0,3).map(lsClean).filter(Boolean), sum=(l.blocks||[]).find(x=>x.t==='summary');
 const points=(sum?.items||[]).slice(0,2).map(lsClean).filter(Boolean);
 return [...a,...points].slice(0,5).length?[...a,...points].slice(0,5):['Định nghĩa đúng '+l.title,'Nêu một giả định/điều kiện','Đưa một ví dụ và trường hợp không áp dụng'];
}
function scFindRelated(l){
 const explicit={kl:'gkd',grpo:'opd',opd:'grpo',mopd:'rlcr','rlcr':'mopd','learning-science-lab':'learning-science','mr13':'kl','mr14':'kl','mr5':'mopd','mr4':'mopd'};
 let p=explicit[l.id]?LESSONS.find(x=>x.id===explicit[l.id]):null;
 if(!p) p=LESSONS.find(x=>x.id!==l.id && x.group===l.group && !x.hero&&!x.glossary && x.id!=='roadmap' && x.id!=='resources');
 if(!p)p=LESSONS.find(x=>x.id==='grpo');
 return p;
}
function scRubricHTML(l){return '<ul>'+scCriteria(l).map(x=>'<li>'+scEscape(x)+'</li>').join('')+'</ul>';}
function scPreflightHTML(l){
 const rec=scRecord(l), m=scMean(l), p=lsPrompt(l);
 const pre=lsClean(m.pre||'');
 return `<details class="sc-preflight" data-sc-preflight><summary><span>01 · Preflight — Tự nhớ trước khi đọc</span><span class="sc-due">Không chấm tự động</span></summary><div class="sc-inner"><div class="sc-eyebrow">Retrieval · Diagnostic · Calibration</div><p class="sc-desc">Đóng nguồn, thử trả lời trước. Nếu chưa biết, viết "chưa biết" và học có hướng dẫn. Đây không phải kiểm tra để loại người học.</p>${pre?`<p class="sc-small"><b>Kiến thức trước:</b> ${scEscape(pre)}</p>`:''}<p class="sc-q">Trước khi đọc, hãy giải thích từ trí nhớ: ${scEscape(p.core)}. Bạn dự đoán điểm nào của chủ đề này dễ gây nhầm lẫn?</p><textarea class="sc-input sc-pre-input" placeholder="Viết từ trí nhớ; bạn có thể ghi rõ điều mình chưa biết…">${scEscape(rec.prior||'')}</textarea><div class="sc-metabox"><label>Độ tự tin trước khi đọc: <b class="sc-conf-label">${rec.confidence??40}%</b></label><input class="sc-conf" aria-label="Độ tự tin ban đầu" type="range" min="0" max="100" step="10" value="${rec.confidence??40}"></div><div class="sc-buttons"><button class="sc-btn sc-pre-save" type="button">Lưu dự đoán ban đầu</button><span class="sc-small sc-pre-status" role="status"></span></div><details class="sc-rubric"><summary>Chỉ xem sau khi đã thử — Mục tiêu đối chiếu</summary>${scRubricHTML(l)}<p class="sc-small">Đây là tiêu chí từ bài gốc, không phải đáp án tự động cho đoạn viết.</p></details></div></details>`;
}
function scPauseHTML(l){
 const m=scMean(l), summary=(l.blocks||[]).find(b=>b.t==='summary');
 const s=lsClean(summary?.items?.[0]||m.learn?.[1]||l.title);
 const related=scFindRelated(l);
 return `<details class="sc-pause" data-sc-pause><summary><span>02 · Pause & Predict — Trước khi xem tiếp</span><span class="sc-due">Dừng 90 giây</span></summary><div class="sc-inner"><div class="sc-eyebrow">Prediction · Self-explanation · Corrective feedback</div><p class="sc-desc">Gợi ý hoạt động, không bắt buộc. Nên thử ít nhất một giả định/ ví dụ trước khi đọc phần giải thích còn lại.</p><p class="sc-q">Nếu bạn thay đổi một giả định quan trọng trong <b>${scEscape(l.title)}</b>, điều gì sẽ không còn đúng? Liên hệ một cách có thể kiểm tra với <b>${scEscape(related?.title||'phương pháp trước')}</b>.</p><textarea class="sc-input sc-pause-input" placeholder="Dự đoán trước. Kết luận sẽ được so sánh với nội dung phần sau…"></textarea><details class="sc-rubric"><summary>Xem gợi ý sau khi tự dự đoán</summary><p class="sc-small">Điểm cần kiểm tra từ bài: ${scEscape(s)}. Đối chiếu với công thức, assumptions và các ví dụ dưới đây. Ghi lại khi bạn thay đổi ý kiến.</p></details></div></details>`;
}
function scReviewHTML(l){
 const rec=scRecord(l), due=rec.due>0?new Date(rec.due).toLocaleDateString('vi-VN'):'Chưa lập lịch';
 const related=scFindRelated(l);
 return `<details class="sc-review" data-sc-review><summary><span>04 · Delayed Retrieval & Transfer</span><span class="sc-due sc-review-due">${scEscape(due)}</span></summary><div class="sc-inner"><div class="sc-eyebrow">Spaced practice · Interleaving · Feedback · Transfer</div><p class="sc-desc">Vòng ôn nên làm <b>vào ngày khác</b>, không nhìn nội dung bên trên. Lịch 1–3–7–14–30 ngày chỉ là heuristic; đánh giá của bạn không xác nhận năng lực khách quan.</p><p class="sc-q">Không xem bài: hãy nhắc lại <b>${scEscape(lsPrompt(l).core)}</b>, rồi chỉ ra điều kiện mà kết luận đó không còn áp dụng.</p><textarea class="sc-input sc-review-input" placeholder="Viết lại từ trí nhớ; lưu cục bộ…">${scEscape(rec.reviewText||'')}</textarea><p class="sc-q"><b>Interleaved comparison:</b> So sánh ${scEscape(l.short)} với ${scEscape(related?.short||'một chủ đề đã học')} về <i>mục tiêu, assumptions, supervision và failure mode</i>. Bạn chọn cách nào khi gặp một tình huống mới và tại sao?</p><div class="sc-metabox"><label for="sc-review-grade">Tự đánh giá trước khi đọc đáp án:</label><select id="sc-review-grade"><option value="0">Chưa nhớ / sai trọng tâm</option><option value="1">Nhớ một phần; cần đối chiếu</option><option value="2">Nhớ rõ; có ví dụ độc lập</option></select></div><details class="sc-rubric"><summary>Mở tiêu chí đối chiếu sau khi đã thử</summary>${scRubricHTML(l)}<p class="sc-small">Để kiểm chứng chuyển giao, bạn cần tạo ví dụ mới, unit test hoặc giải độc lập; không chỉ tự tick.</p></details><div class="sc-buttons"><button class="sc-btn sc-review-submit" type="button">Ghi nhận vòng ôn và đặt ngày mới</button><span class="sc-small sc-review-status" role="status"></span></div><p class="sc-small">Tổng phiên ôn đã ghi: <b class="sc-review-count">${(rec.logs||[]).length}</b>. Bạn có thể làm lại sau feedback; không có điểm mastery tự động.</p></div></details>`;
}
function scProfileHTML(){return `<div class="sc-metabox sc-mode"><label for="sc-mode-select">Mức hướng dẫn:</label><select id="sc-mode-select"><option value="guided" ${SC_MODE==='guided'?'selected':''}>Mới bắt đầu · worked example</option><option value="mixed" ${SC_MODE==='mixed'?'selected':''}>Có nền tảng · hints vừa phải</option><option value="independent" ${SC_MODE==='independent'?'selected':''}>Researcher · tự giải trước</option></select><span class="sc-small sc-mode-note"></span></div>`;}
function scBind(l){
 const c=document.getElementById('content');if(!c||l.hero||l.glossary)return;
 const pre=c.querySelector('.sc-preflight'), rec=scRecord(l);
 if(pre){const conf=pre.querySelector('.sc-conf');conf.addEventListener('input',()=>{pre.querySelector('.sc-conf-label').textContent=conf.value+'%';});pre.querySelector('.sc-pre-save').addEventListener('click',()=>{rec.prior=pre.querySelector('.sc-pre-input').value.slice(0,16000);rec.confidence=Number(conf.value);rec.preAt=Date.now();scSave();pre.querySelector('.sc-pre-status').textContent='Đã lưu baseline để đối chiếu về sau.';});}
 const profile=c.querySelector('#sc-mode-select');if(profile){const msg=c.querySelector('.sc-mode-note');const setMode=()=>{SC_MODE=profile.value;try{localStorage.setItem('mopd_sc_mode_v5',SC_MODE);}catch(e){}msg.textContent=SC_MODE==='guided'?'Nên xem worked example trước khi giải bài tương tự.':SC_MODE==='mixed'?'Hãy thử trước, mở hint khi bị kẹt.':'Hãy thử độc lập và tự phản chứng trước khi mở rubric.';};profile.addEventListener('change',setMode);setMode();}
 const pause=c.querySelector('.sc-pause');if(pause){let v=rec.pause||'';pause.querySelector('.sc-pause-input').value=v;pause.querySelector('.sc-pause-input').addEventListener('change',e=>{rec.pause=e.target.value.slice(0,16000);scSave();});}
 const box=c.querySelector('.sc-review');if(box){const input=box.querySelector('.sc-review-input');input.addEventListener('change',()=>{rec.reviewText=input.value.slice(0,16000);scSave();});box.querySelector('.sc-review-submit').addEventListener('click',()=>{
  const grade=Number(box.querySelector('#sc-review-grade').value), ans=input.value.trim();
  if(ans.length<30){box.querySelector('.sc-review-status').textContent='Hãy thử truy hồi bằng một đoạn ngắn trước khi lưu kết quả.';return;}
  const now=Date.now(), old=rec.reps||0;
  if(grade===0)rec.reps=0;else if(grade===1)rec.reps=Math.max(1,old);else rec.reps=Math.min(5,old+1);
  const schedule=[1,3,7,14,30];const gap=grade===0?1:schedule[Math.min(4,rec.reps-1)];
  rec.due=now+gap*86400000;rec.last=now;rec.reviewText=ans.slice(0,16000);rec.logs=Array.isArray(rec.logs)?rec.logs:[];
  rec.logs.push({at:now,grade,gap,preview:ans.slice(0,180)});rec.logs=rec.logs.slice(-40);
  scSave();box.querySelector('.sc-review-due').textContent=new Date(rec.due).toLocaleDateString('vi-VN');box.querySelector('.sc-review-count').textContent=rec.logs.length;box.querySelector('.sc-review-status').textContent='Đã ghi vòng ôn · đề nghị kiểm tra lại sau '+gap+' ngày.';scUpdateHub();
 });}
 scUpdateHub();
}
function scUpdateHub(){
 const hub=document.getElementById('sc-hub'), list=document.getElementById('sc-hub-list');if(!hub||!list)return;
 const arr=LESSONS.filter(l=>SC_STATE[l.id]?.due>0).map(l=>({l,due:SC_STATE[l.id].due})).sort((a,b)=>a.due-b.due);
 const now=Date.now(), due=arr.filter(x=>x.due<=now);
 hub.querySelector('#sc-hub-count').textContent=arr.length?`${due.length} bài đến hạn / ${arr.length} bài đã đặt lịch`:'Chưa có lịch — ghi một vòng ôn cuối bài để bắt đầu.';
 list.innerHTML=arr.slice(0,6).map(({l,due})=>`<li><button type="button" data-sc-go="${scEscape(l.id)}">${scEscape(l.short)}</button><span class="sc-footnote"> · ${new Date(due).toLocaleDateString('vi-VN')}</span></li>`).join('');
 list.querySelectorAll('button[data-sc-go]').forEach(b=>b.addEventListener('click',()=>{const idx=LESSONS.findIndex(l=>l.id===b.dataset.scGo);if(idx>=0)goTo(idx);}));
 const exp=hub.querySelector('#sc-hub-export');if(exp&&!exp.dataset.bound){exp.dataset.bound='1';exp.addEventListener('click',()=>{const o={created:new Date().toISOString(),learningScienceV5:SC_STATE,learningStudioV4:LS_NOTES,notice:'self-report, no automated evaluation'};const blob=new Blob([JSON.stringify(o,null,2)],{type:'application/json'});const a=document.createElement('a');const url=URL.createObjectURL(blob);a.href=url;a.download='mopd-learning-science-v5-backup.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1500);});}
}
'''
needle2='/* ============================================================\n   NAV BUILD'
assert s.count(needle2)==1
s=s.replace(needle2,v5_js+'\n'+needle2)

# replace rendering start with preflight, two-stage content, studio etc
old='''  h+=`<div class="rule"></div>`;
  const qpos=l.blocks.findIndex(b=>b.t==='quiz');
  const splitAt=qpos<0?l.blocks.length:qpos;
  h+=l.blocks.slice(0,splitAt).map(blockHTML).join('');
  h+=learningStudioHTML(l);
  h+=l.blocks.slice(splitAt).map(blockHTML).join('');
'''
new='''  h+=`<div class="rule"></div>`;
  h+=scProfileHTML();
  h+=scPreflightHTML(l);
  const qpos=l.blocks.findIndex(b=>b.t==='quiz');
  const splitAt=qpos<0?l.blocks.length:qpos;
  const halfway=Math.max(1,Math.min(splitAt,Math.floor(splitAt*0.42)));
  h+=l.blocks.slice(0,halfway).map(blockHTML).join('');
  h+=scPauseHTML(l);
  h+=l.blocks.slice(halfway,splitAt).map(blockHTML).join('');
  h+=learningStudioHTML(l);
  h+=scReviewHTML(l);
  h+=l.blocks.slice(splitAt).map(blockHTML).join('');
'''
assert s.count(old)==1
s=s.replace(old,new)
# bind after bind pager
old='''  bindLearningStudio(l);
  bindPager();'''
new='''  bindLearningStudio(l);
  scBind(l);
  bindPager();'''
assert s.count(old)==1
s=s.replace(old,new)
# ensure UI not overpromise re quiz
s=s.replace("'Hoàn thành bài tập để đánh dấu chương'","'Quiz đã xem hết · Nên ôn lại để kiểm tra ghi nhớ'")
s=s.replace("'Trả lời hết các câu hỏi bên trên, chương sẽ tự được đánh dấu.'","'Trả lời quiz chỉ đánh dấu tiến độ đọc; không xác nhận mastery hoặc retention.'")
s=s.replace("'Đã hoàn thành chương này'","'Đã đánh dấu tiến độ chương này'")
# title and notes
s=s.replace('Learning Studio v4 — Feynman · First Principles · Synthetic Mastery','Learning Science v5 — Retrieval · Feedback · Spacing · Transfer')
s=s.replace('114 trang có Learning Studio','114 trang có Learning Studio')
OUT.write_text(s,encoding='utf-8')
print('saved',OUT,'size',OUT.stat().st_size,'old',SRC.stat().st_size)
