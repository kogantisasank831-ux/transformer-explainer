import assert from 'node:assert/strict';
import { createServer } from 'vite';
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';

const server=await createServer({configFile:fileURLToPath(new URL('../vite.config.js',import.meta.url)),server:{host:'127.0.0.1',port:1450,strictPort:true}});
await server.listen();
const browser=await chromium.launch({headless:true,executablePath:process.env.ORBIT_BROWSER||undefined,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
try {
  const page=await browser.newPage({viewport:{width:1120,height:850},colorScheme:'light'});
  const errors=[];page.on('pageerror',error=>errors.push(error.message));
  await page.goto('http://127.0.0.1:1450/?demo=1');
  await page.getByRole('button',{name:'XLSX Tables',exact:true}).click();
  assert.equal(await page.locator('.output-title').innerText(),'Convert to XLSX');
  assert.equal(await page.locator('#convert').isDisabled(),true);
  await page.getByRole('button',{name:'DOCX Select',exact:true}).click();
  await page.locator('#docx-mode').selectOption('page_images');
  assert.match(await page.locator('.note').first().innerText(),/not editable/);
  await page.getByRole('button',{name:'Excel',exact:true}).click();
  assert.equal(await page.locator('.output-title').innerText(),'Convert to PDF');
  await page.locator('#single-page').check();
  await page.getByRole('button',{name:'Settings',exact:true}).click();
  assert.equal(await page.locator('#settings-dialog').isVisible(),true);
  await page.getByRole('button',{name:'Close',exact:true}).click();
  for (const width of [1120,760,390,320]) {
    await page.setViewportSize({width,height:850});
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`overflow at ${width}px`);
  }
  if(process.env.ORBIT_SCREENSHOT) {
    await page.setViewportSize({width:1120,height:850});
    await page.getByRole('button',{name:'PDF',exact:true}).click();
    await page.screenshot({path:process.env.ORBIT_SCREENSHOT,fullPage:true,animations:'disabled'});
  }
  assert.deepEqual(errors,[]);
  console.log('PASS wheel selection, PDF Word modes, Excel PDF controls, settings and responsive layouts (320–1120 px).');
} finally { await browser.close();await server.close(); }
