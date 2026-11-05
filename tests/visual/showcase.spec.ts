import { expect, test } from '@playwright/test';

test('showcase', async ({ page }) => {
  await page.addInitScript(() => localStorage.setItem('dau.cookie-notice', 'dismissed'));
  await page.goto('/');
  await expect(page).toHaveScreenshot('showcase.png', { fullPage: true });
});
