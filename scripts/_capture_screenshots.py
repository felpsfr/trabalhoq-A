"""Captura screenshots das telas principais do Local Eats como evidência dos PBLs 7/8."""
from pathlib import Path

from playwright.sync_api import sync_playwright

EVID = Path(__file__).resolve().parent.parent / "artefatos" / "evidencias"
EVID.mkdir(parents=True, exist_ok=True)


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800}, locale="pt-BR")

        page.goto("https://local-eats-unisenac.vercel.app/", wait_until="networkidle")
        page.screenshot(path=str(EVID / "01_login.png"), full_page=True)

        page.locator("#loginEmail").fill("teste@teste.com")
        page.locator("#loginPassword").fill("123")
        page.locator("button.primary-btn", has_text="Entrar").click()
        page.wait_for_url("**/static/index.html", timeout=10_000)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(EVID / "02_home_pos_login.png"), full_page=True)

        page.locator("a[href^='restaurant.html?id=']").first.click()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(EVID / "03_detalhe_restaurante.png"), full_page=True)

        page.goto("https://local-eats-unisenac.vercel.app/static/profile.html", wait_until="networkidle")
        page.screenshot(path=str(EVID / "04_favoritos.png"), full_page=True)

        page.goto("https://local-eats-unisenac.vercel.app/static/orders.html", wait_until="networkidle")
        page.screenshot(path=str(EVID / "05_pedidos.png"), full_page=True)

        # contexto novo (sessão limpa) para capturar erro de login
        ctx2 = browser.new_context(viewport={"width": 1280, "height": 800}, locale="pt-BR")
        page2 = ctx2.new_page()
        page2.goto("https://local-eats-unisenac.vercel.app/", wait_until="networkidle")
        page2.locator("#loginEmail").fill("invalido@x.com")
        page2.locator("#loginPassword").fill("errada")
        page2.locator("button.primary-btn", has_text="Entrar").click()
        page2.wait_for_timeout(2000)
        page2.screenshot(path=str(EVID / "06_login_erro.png"), full_page=True)
        ctx2.close()

        browser.close()
    print(f"Screenshots salvos em {EVID}")


if __name__ == "__main__":
    main()
