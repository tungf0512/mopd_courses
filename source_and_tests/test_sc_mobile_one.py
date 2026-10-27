from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu'])
 page=b.new_page(viewport={'width':390,'height':844},is_mobile=True)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(Path('/mnt/data/mopd-course-research-edition-v5-learning-science.html').read_text(),wait_until='domcontentloaded',timeout=30000)
 x=page.evaluate("()=>{goTo(LESSONS.findIndex(l=>l.id==='mr15'));return {width:innerWidth, doc:document.documentElement.scrollWidth,summary:document.querySelector('.sc-preflight > summary')?.textContent,study:document.querySelector('.learning-studio')!==null}}")
 print(x,'js errors',errors,flush=True)
 page.screenshot(path='/mnt/data/mopd_v5_mobile.png',full_page=False,timeout=10000)
 b.close()
