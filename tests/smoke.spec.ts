import { test, expect, type Page } from '@playwright/test';

// Datos 100 % ficticios: email @example.com y tarjetas de prueba que publica la propia tienda.
const CLIENTE = {
  nombre: 'Lucía Prueba',
  direccion: 'Dirección de prueba 123',
  email: 'lucia.qa@example.com',
};
const TARJETA_APROBADA = '4111111111111111';
const TARJETA_RECHAZADA = '4000000000000002';

async function completarCheckout(page: Page, tarjeta: string) {
  await page.getByTestId('input-nombre').fill(CLIENTE.nombre);
  await page.getByTestId('input-direccion').fill(CLIENTE.direccion);
  await page.getByTestId('input-email').fill(CLIENTE.email);
  await page.getByTestId('input-tarjeta').fill(tarjeta);
  await page.getByTestId('input-vencimiento').fill('12/30');
  await page.getByTestId('input-cvv').fill('123');
  await page.getByTestId('submit-checkout').click();
}

async function agregarRemeraDinoEIrAlCheckout(page: Page) {
  await page.goto('/tienda');
  await page.getByTestId('add-to-cart-4').click(); // Remera Dino Aventurero · Niño (3-8) · $ 9.800
  await page.getByTestId('checkout-btn').click();
  await expect(page).toHaveURL(/\/checkout/);
}

test.describe('Smoke · flujos críticos de MiniModa', () => {
  test('CP-002 · filtrar por "Niño (3-8)" muestra solo productos de esa edad', async ({ page }) => {
    await page.goto('/tienda');
    await page.getByTestId('filter-edad').selectOption('Niño (3-8)');

    const tarjetas = page.getByTestId('product-card');
    await expect(tarjetas).toHaveCount(3);
    for (const tarjeta of await tarjetas.all()) {
      await expect(tarjeta).toContainText('Niño (3-8)');
    }
    await expect(page.getByTestId('product-1')).toBeHidden(); // Bebé (0-2)
  });

  test('CP-008 · agregar un producto actualiza el contador y el total del carrito', async ({ page }) => {
    await page.goto('/tienda');
    await page.getByTestId('add-to-cart-4').click();

    await expect(page.getByTestId('cart-count')).toHaveText('1');
    await expect(page.getByTestId('cart-qty-4')).toHaveText('1');
    await expect(page.getByTestId('cart-total')).toHaveText(/\$\s9\.800/);
  });

  test('CP-012 · compra con tarjeta de prueba aprobada confirma la orden', async ({ page }) => {
    await agregarRemeraDinoEIrAlCheckout(page);
    await completarCheckout(page, TARJETA_APROBADA);

    await expect(page.getByTestId('checkout-success')).toContainText('Compra confirmada');
    await expect(page.getByTestId('order-id')).toHaveText(/^MM-\d+$/);
  });

  test('CP-013 · tarjeta de prueba rechazada muestra el error y no genera orden', async ({ page }) => {
    await agregarRemeraDinoEIrAlCheckout(page);
    await completarCheckout(page, TARJETA_RECHAZADA);

    await expect(page.getByTestId('error-tarjeta')).toHaveText('Tarjeta rechazada');
    await expect(page.getByTestId('checkout-success')).toHaveCount(0);
  });
});
