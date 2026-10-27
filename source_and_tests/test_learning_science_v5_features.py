from playwright.sync_api import sync_playwright
from pathlib import Path
p=Path('/mnt/data/mopd-course-research-edition-v5-learning-science.html')
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu','--disable-dev-shm-usage'])
 for dims in [(1340,900),(390,844)]:
  page=browser.new_page(viewport={'width':dims[0],'height':dims[1]})
  errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
  page.set_content(p.read_text(),wait_until='domcontentloaded',timeout=30000)
  print('viewport',dims,'nav',page.locator('.nav-item').count(),flush=True)
  info=page.evaluate('''() => {
  const l=LESSONS.filter(l=>!l.hero&&!l.glossary);
  const ids=l.map(l=>l.id);
  let tested=0;for(const item of l){if(scPreflightHTML(item).includes('data-sc-preflight')&&scPauseHTML(item).includes('data-sc-pause')&&scReviewHTML(item).includes('data-sc-review')&&scScaffoldHTML(item).includes('sc-scaffold'))tested++}
  return {n:l.length,unique:new Set(ids).size,tested,rlcr:LESSONS.filter(l=>/Collective Rewards|Avalon-M1/.test(l.title)).map(x=>x.id)};
 }''')
  print('coverage',info,flush=True)
  page.evaluate('''() =>{goTo(LESSONS.findIndex(x=>x.id==='grpo'));window.__memory={};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem(k){return window.__memory[k]||null},setItem(k,v){window.__memory[k]=v},removeItem(k){delete window.__memory[k]}}});}''')
  page.evaluate('''() =>{const a=document.querySelector('.sc-preflight');a.open=true;a.querySelector('textarea').value='GRPO được xây từ các rollouts và group advantage; tôi chưa chắc clip hoạt động thế nào.';a.querySelector('.sc-conf').value=70;a.querySelector('.sc-pre-save').click();const mode=document.querySelector('#sc-mode-select');mode.value='independent';mode.dispatchEvent(new Event('change'));const r=document.querySelector('.sc-review');r.open=true;r.querySelector('textarea').value='Group relative advantages dùng tín hiệu tương đối trong nhóm; nếu cả nhóm giống nhau thì variance rất thấp. Nhờ chuẩn hóa được tín hiệu huấn luyện.';r.querySelector('.sc-review-submit').click();}''')
  result=page.evaluate('''() => ({record:SC_STATE.grpo?.reps, due:SC_STATE.grpo?.due>Date.now(),counts:document.querySelector('#sc-hub-count').textContent,mode:document.querySelector('.sc-scaffold-independent').hidden,modeOther:document.querySelector('.sc-scaffold-guided').hidden,persist:!!window.__memory.mopd_learning_science_v5,overflow:document.documentElement.scrollWidth>window.innerWidth,error:document.querySelector('.sc-review-status').textContent})''')
  print('interaction',result,'errors',errs,flush=True)
  if dims[0]==390:
   page.screenshot(path='/mnt/data/mopd_v5_learning_science_mobile.png',full_page=False)
  page.close()
 browser.close()
