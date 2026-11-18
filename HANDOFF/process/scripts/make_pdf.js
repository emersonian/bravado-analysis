// Usage: node make_pdf.js <input.html> <output.pdf> [png-prefix]
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 816, height: 1056 } });
  const errs = [];
  pg.on('pageerror', function (e) { errs.push(e.message); });
  await pg.goto('file://' + process.argv[2]);
  await pg.waitForTimeout(600);
  await pg.pdf({ path: process.argv[3], format: 'Letter', printBackground: true, preferCSSPageSize: true });
  console.log('page errors:', JSON.stringify(errs));
  await b.close();
})();
