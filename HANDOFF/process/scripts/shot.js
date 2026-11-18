const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const scheme of ['light', 'dark']) {
    const pg = await b.newPage({ viewport: { width: 920, height: 1200 }, colorScheme: scheme, deviceScaleFactor: 1 });
    const errs = [];
    pg.on('pageerror', function (e) { errs.push(e.message); });
    await pg.goto('file://' + process.argv[2]);
    await pg.waitForTimeout(1000);
    const figs = [['chMain', 'B'], ['chDoc', 'C'], ['chMonthly', 'D'], ['chHist', 'A']];
    for (const pair of figs) {
      const el = await pg.$('#' + pair[0]);
      await el.screenshot({ path: process.argv[3] + '/fig' + pair[1] + '-' + scheme + '.png' });
    }
    const tables = await pg.$$('table');
    await tables[0].screenshot({ path: process.argv[3] + '/figF-' + scheme + '.png' });
    console.log(scheme, 'page errors:', JSON.stringify(errs));
    await pg.close();
  }
  await b.close();
})();
