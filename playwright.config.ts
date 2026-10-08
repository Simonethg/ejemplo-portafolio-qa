import { defineConfig, devices } from '@playwright/test';

/**
 * Smoke de MiniModa: corre contra la URL pública, sin usuarios, claves ni variables de entorno.
 * Un solo navegador (Chromium) para que el CI sea rápido y gaste pocos minutos.
 */
export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  expect: { timeout: 7_000 },
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: 'https://minimoda-navy.vercel.app',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
