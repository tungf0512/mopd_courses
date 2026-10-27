from pathlib import Path
p=Path('/mnt/data/mopd-course-research-edition-v5-learning-science.html')
s=p.read_text()
# create scaffold with actual content in the source lesson
needle='function scProfileHTML(){return `'
assert s.count(needle)==1
insert=r'''function scScaffoldHTML(l){
 const blocks=l.blocks||[],m=scMean(l),math=blocks.find(b=>b.t==='mathdeep'),code=blocks.find(b=>b.t==='code'),meaning=(m.learn||[]);
 const worked=lsClean(code?.explain||math?.whole||blocks.find(x=>x.t==='analogy')?.x||blocks.find(x=>x.t==='summary')?.items?.[0]||meaning[0]||l.title).slice(0,680);
 const target=lsClean(code?.prompt||math?.intuition||meaning[1]||l.title).slice(0,460);
 const independent=lsClean(meaning[2]||blocks.find(x=>x.t==='summary')?.items?.[1]||l.title).slice(0,360);
 return `<details class="sc-pause sc-scaffold"><summary><span>Scaffolding — Chọn mức hỗ trợ phù hợp</span><span class="sc-due">Worked → Faded → Independent</span></summary><div class="sc-inner"><div class="sc-scaffold-guided"><p class="sc-small"><b>Worked example có hướng dẫn (trích kiến thức từ bài):</b> ${scEscape(worked)}</p><p class="sc-q">Bước cần tự làm: ${scEscape(target)}. Thử biến đổi một giả định và giải thích ảnh hưởng.</p></div><div class="sc-scaffold-mixed" hidden><p class="sc-q">Gợi ý bước đầu: ${scEscape(target)}. Chỉ mở phần lời giải sau khi bạn đã thử nêu ít nhất một bước suy luận.</p><details class="sc-rubric"><summary>Mở một điểm đối chiếu</summary><p class="sc-small">${scEscape(worked)}</p></details></div><div class="sc-scaffold-independent" hidden><p class="sc-q">Không nhìn nguồn: tự tái dựng, kiểm tra một phản ví dụ và đo kết quả — ${scEscape(independent)}</p><details class="sc-rubric"><summary>Đối chiếu lại bằng chứng từ bài</summary><p class="sc-small">${scEscape(worked)}</p></details></div><p class="sc-footnote">Các đoạn gợi ý được trích/paraphrase từ chính bài học; không phải lời giải mới do một tutor trực tiếp chấm.</p></div></details>`;
}
'''
s=s.replace(needle,insert+needle)
assert s.count('  h+=scProfileHTML();')==1
s=s.replace('  h+=scProfileHTML();','  h+=scProfileHTML();\n  h+=scScaffoldHTML(l);')
# swap pause generic with one referencing actual source objective
s=s.replace("const s=lsClean(summary?.items?.[0]||m.learn?.[1]||l.title);\n const related=scFindRelated(l);", "const s=lsClean(summary?.items?.[0]||m.learn?.[1]||l.title);\n const focus=lsClean(m.learn?.[1]||m.learn?.[0]||l.title);\n const related=scFindRelated(l);")
s=s.replace('Nếu bạn thay đổi một giả định quan trọng trong <b>${scEscape(l.title)}</b>, điều gì sẽ không còn đúng?', 'Trước khi xem phần còn lại, hãy dự đoán điều kiện/giới hạn của mục tiêu <b>${scEscape(focus)}</b>. Nếu thay đổi một assumption, điều gì sẽ không còn đúng?')
# when mode updates, affect scaffold content
old="SC_MODE==='guided'?'Nên xem worked example trước khi giải bài tương tự.':SC_MODE==='mixed'?'Hãy thử trước, mở hint khi bị kẹt.':'Hãy thử độc lập và tự phản chứng trước khi mở rubric.';};"
new="SC_MODE==='guided'?'Nên xem worked example trước khi giải bài tương tự.':SC_MODE==='mixed'?'Hãy thử trước, mở hint khi bị kẹt.':'Hãy thử độc lập và tự phản chứng trước khi mở rubric.'; c.querySelectorAll('.sc-scaffold-guided').forEach(x=>x.hidden=SC_MODE!=='guided');c.querySelectorAll('.sc-scaffold-mixed').forEach(x=>x.hidden=SC_MODE!=='mixed');c.querySelectorAll('.sc-scaffold-independent').forEach(x=>x.hidden=SC_MODE!=='independent');};"
assert s.count(old)==1
s=s.replace(old,new)
s=s.replace('  const related=scFindRelated(l);\n return `<details class="sc-review"','  const related=scFindRelated(l);\n return `<details class="sc-review"')
# improve exit question tie back to source lesson rather than only title
s=s.replace('hãy nhắc lại <b>${scEscape(lsPrompt(l).core)}</b>, rồi chỉ ra điều kiện mà kết luận đó không còn áp dụng.', 'hãy giải thích <b>${scEscape(lsPrompt(l).core)}</b>, rồi chỉ ra một điều kiện khiến cách giải thích đó không còn áp dụng.')
# add global CSS hidden fix (display none when attribute hidden; div default native should)
p.write_text(s)
print('patched bytes',p.stat().st_size)
