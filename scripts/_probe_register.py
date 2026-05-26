"""Tenta registrar um usuário novo, depois loga, e descreve o estado pós-login."""
import time

from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://local-eats-unisenac.vercel.app/", wait_until="networkidle")
        page.wait_for_timeout(1500)

        # tentar logar com placeholder credentials primeiro
        print("=== Login com placeholder credentials (teste@teste.com / 123) ===")
        page.locator("#loginEmail").fill("teste@teste.com")
        page.locator("#loginPassword").fill("123")
        page.locator("button.primary-btn", has_text="Entrar").click()
        page.wait_for_timeout(2500)
        print(f"URL: {page.url}  Title: {page.title()}")
        err = page.locator("#errorMsg")
        if err.is_visible():
            print(f"   Erro mostrado: {err.text_content()!r}")

        if "login" in page.url:
            # tentar registrar
            print()
            print("=== Registrando usuário novo ===")
            unique = f"qa{int(time.time())}@teste.com"
            page.get_by_role("button", name="Criar Conta").click()
            page.wait_for_timeout(500)
            # campos de registro
            page.locator("input[type='text']").fill("QA Tester")
            page.locator("input[type='email']").nth(1).fill(unique)
            page.locator("input[type='password']").nth(1).fill("senha123")
            print(f"Tentando registrar: {unique}")
            page.get_by_role("button", name="Registrar").click()
            page.wait_for_timeout(3000)
            print(f"URL pós-registro: {page.url}")
            print(f"Title: {page.title()}")

            # agora tentar logar
            if "login" in page.url:
                page.locator("#loginEmail").fill(unique)
                page.locator("#loginPassword").fill("senha123")
                page.locator("button.primary-btn", has_text="Entrar").click()
                page.wait_for_timeout(2500)

        print()
        print("=== Estado pós-login ===")
        print(f"URL: {page.url}")
        print(f"Title: {page.title()}")
        print()
        print("=== Headings na home ===")
        for h in page.locator("h1, h2, h3").all():
            try:
                print(f"  {h.evaluate('el => el.tagName')}: {h.text_content()!r}")
            except Exception:
                pass
        print()
        print("=== Possible cards ===")
        for sel in ["article", ".restaurant-card", "[data-testid='restaurant-card']", ".card", ".restaurante", "main .item"]:
            n = page.locator(sel).count()
            if n:
                print(f"  {sel}: {n}")
        print()
        print("=== Links de navegação ===")
        for a in page.locator("nav a, header a, a").all()[:15]:
            try:
                print(f"  href={a.get_attribute('href')} text={(a.text_content() or '').strip()!r}")
            except Exception:
                pass

        browser.close()


if __name__ == "__main__":
    main()
