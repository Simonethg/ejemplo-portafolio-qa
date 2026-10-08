import { test, expect } from '@playwright/test';

/**
 * Bugs conocidos que siguen abiertos.
 *
 * Cada test describe el comportamiento CORRECTO y está marcado con test.fail():
 * - Mientras el bug exista, el test falla "como se espera" y el CI queda en verde.
 * - Cuando lo corrijan, el test pasa, Playwright lo marca como "unexpected pass" y el CI se pone en rojo:
 *   ese es el aviso para volver a probar a mano, cerrar el bug y sacar el test.fail().
 */
test.describe('Bugs conocidos (abiertos)', () => {
  test('BUG-001 · el checkout no debería confirmar una compra con el carrito vacío', async ({ page }) => {
    test.fail(true, 'BUG-001 abierto: ver bug-reports/BUG-001-checkout-carrito-vacio.md');

    // Contexto nuevo = carrito vacío. Se entra directo a /checkout sin agregar productos.
    await page.goto('/checkout');
    await page.getByTestId('input-nombre').fill('Lucía Prueba');
    await page.getByTestId('input-direccion').fill('Dirección de prueba 123');
    await page.getByTestId('input-email').fill('lucia.qa@example.com');
    await page.getByTestId('input-tarjeta').fill('4111111111111111');
    await page.getByTestId('input-vencimiento').fill('12/30');
    await page.getByTestId('input-cvv').fill('123');
    await page.getByTestId('submit-checkout').click();

    // Se espera a que la tienda responda (mensaje de éxito o algún error) antes de verificar.
    const exito = page.getByTestId('checkout-success');
    await expect(exito.or(page.locator('[data-testid^="error-"]')).first()).toBeVisible();

    // Esperado: la compra se bloquea. Hoy aparece "Compra confirmada" con número de orden.
    expect(await exito.count(), 'No debería haber confirmación de compra sin productos').toBe(0);
  });
});
