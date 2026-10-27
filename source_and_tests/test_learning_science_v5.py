from playwright.sync_api import sync_playwright
from pathlib import Path
P='/mnt/data/mopd-course-research-edition-v5-learning-science.html'
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 ctx=b.new_context(viewport={'width':1366,'height':900},accept_downloads=True)
 page=ctx.new_page()
 errors=[]
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.set_content(Path(P).read_text(),wait_until='domcontentloaded',timeout=25000)
 page.wait_for_timeout(450)
 print('title',page.title())
 print('lesson count',page.locator('.nav-item').count(),'hublocation',page.locator('#sc-hub').count())
 print('current h2',page.locator('h2.lesson-title').first.text_content() if page.locator('h2.lesson-title').count() else 'hero')
 for lesson_id in ['learning-science-lab','grpo','kl','mopd','rlcr','mr14','g1-prob']:
  sel=f'.nav-item[data-id="{lesson_id}"]'
  if page.locator(sel).count()==0: print('missing',lesson_id);continue
  page.locator(sel).click(timeout=3500)
  print(lesson_id,'pre',page.locator('.sc-preflight').count(),'pause',page.locator('.sc-pause').count(),'review',page.locator('.sc-review').count(),'studio',page.locator('.learning-studio').count())
  if lesson_id=='grpo':
   page.locator('.sc-preflight > summary').click()
   page.locator('.sc-pre-input').fill('Điểm baseline nhóm tương đối, kỳ vọng gradient giảm phương sai. '+ 'hello'*10)
   page.locator('.sc-conf').fill('70')
   page.locator('.sc-pre-save').click()
   page.locator('.sc-review > summary').click()
   page.locator('.sc-review-input').fill('GRPO dùng group relative advantages với rollout group để chuẩn hoá. Khi phần thưởng như nhau, signal khó học. '+ 'more'*10)
   page.locator('.sc-review-submit').click()
   print('review status',page.locator('.sc-review-status').inner_text(),'hub count',page.locator('#sc-hub-count').inner_text())
  if lesson_id=='learning-science-lab':
   page.screenshot(path='/mnt/data/mopd_v5_learning_science_chapter.png',full_page=False)
 print('errors',errors[:12])
 ctx.close()
 mobile=b.new_context(viewport={'width':390,'height':844},is_mobile=True,device_scale_factor=1)
 pg=mobile.new_page()
 pg.on('pageerror',lambda e: errors.append(str(e)))
 pg.set_content(Path(P).read_text(),wait_until='domcontentloaded',timeout=25000)
 pg.locator('.hamb').click()
 pg.locator('.nav-item[data-id="grpo"]').click()
 print('mobile overflow',pg.evaluate('document.documentElement.scrollWidth > innerWidth'), 'main width',pg.evaluate('document.documentElement.scrollWidth'))
 pg.locator('.sc-preflight > summary').click()
 pg.screenshot(path='/mnt/data/mopd_v5_mobile_preflight.png',full_page=False)
 print('all errors',errors[:12])
 b.close()
