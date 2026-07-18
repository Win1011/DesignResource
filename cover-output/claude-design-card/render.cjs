const { chromium } = require('playwright-core');
const path = require('path');
const fs = require('fs');

(async () => {
  const dir = __dirname;
  const outPath = path.join(dir, 'cover-dark-magazine.png');
  const browser = await chromium.launch({
    executablePath: '/usr/local/bin/google-chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files'],
  });
  const page = await browser.newPage({
    viewport: { width: 1200, height: 1600 },
    deviceScaleFactor: 1,
  });
  await page.goto('file://' + path.join(dir, 'cover-dark-magazine.html'), {
    waitUntil: 'networkidle',
    timeout: 60000,
  });
  await page.waitForTimeout(1200);
  await page.evaluate(async () => {
    if (document.fonts?.ready) await document.fonts.ready;
    await Promise.all(
      Array.from(document.images).map((img) =>
        img.complete
          ? Promise.resolve()
          : new Promise((res) => {
              img.onload = img.onerror = res;
            })
      )
    );
  });
  const el = await page.$('#card');
  if (!el) throw new Error('#card not found');
  await el.screenshot({ path: outPath, type: 'png' });
  console.log('wrote', outPath);
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
