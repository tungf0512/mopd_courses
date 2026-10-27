from playwright.sync_api import sync_playwright
from pathlib import Path
p='/mnt/data/mopd-course-research-edition-v5-learning-science.html'
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 page=b.new_page(viewport={'width':1320,'height':820})
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 print('setting content',flush=True)
 page.set_content(Path(p).read_text(),wait_until='domcontentloaded',timeout=40000)
 print('nav',page.locator('.nav-item').count(),'title',page.title(),flush=True)
 for lid in ['learning-science-lab','grpo','mopd','rlcr','mr14']:
  result=page.evaluate('''id=>{ const i=LESSONS.findIndex(l=>l.id===id);if(i<0)return {id,exists:false};goTo(i);return {id,exists:true,title:document.querySelector('h2.lesson-title')?.textContent,pre:document.querySelectorAll('.sc-preflight').length,pause:document.querySelectorAll('.sc-pause').length,review:document.querySelectorAll('.sc-review').length,scaffold:document.querySelectorAll('.sc-scaffold').length,studio:document.querySelectorAll('.learning-studio').length};}''',lid)
  print(result,flush=True)
 print('page errors',errors[:5],flush=True)
 b.close()
