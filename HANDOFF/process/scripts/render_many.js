// Usage: node render_many.js <list.json>   where list.json = [{"html": "/abs/in.html", "pdf": "/abs/out.pdf"}, ...]
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const list = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch();
  for (const item of list) {
    const pg = await b.newPage({ viewport: { width: 816, height: 1056 } });
    await pg.goto('file://' + item.html);
    await pg.waitForTimeout(300);
    await pg.pdf({ path: item.pdf, format: 'Letter', printBackground: true, preferCSSPageSize: true });
    await pg.close();
  }
  await b.close();
})();
