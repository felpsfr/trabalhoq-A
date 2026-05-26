"""Inspeciona o formulário de login e tenta autenticação com placeholders sugeridos."""
from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://local-eats-unisenac.vercel.app/", wait_until="networkidle")
        page.wait_for_timeout(1500)

        # capturar HTML reduzido
        print("=== HTML do main / form ===")
        try:
            print(page.locator("form").first.inner_html()[:2000])
        except Exception as e:
            print(f"(sem form) {e}")
        print()

        # tentar login com credenciais inválidas e capturar mensagem
        print("=== Tentativa: credenciais inválidas ===")
        page.locator("input[type='email']").first.fill("naoexiste@x.com")
        page.locator("input[type='password']").first.fill("senhaerrada")
        page.get_by_role("button", name="Entrar", exact=True).first.click()
        page.wait_for_timeout(2500)
        print(f"URL após click: {page.url}")
        print(f"Title: {page.title()}")
        body_text = page.locator("body").text_content() or ""
        # imprime trechos que pareçam mensagem de erro
        for linha in body_text.split("\n"):
            l = linha.strip()
            if l and any(kw in l.lower() for kw in ["inv", "erro", "incorret", "senha", "credenc", "falha"]):
                print(f"   -> {l!r}")
        print()

        # listar localStorage/sessionStorage para entender persistência
        print("=== localStorage keys ===")
        keys = page.evaluate("() => Object.keys(localStorage)")
        print(keys)

        browser.close()


if __name__ == "__main__":
    main()
