"""Script auxiliar (não é teste): inspeciona o DOM real do Local Eats para
ajustar seletores dos POMs. Executar com: python scripts/_probe_site.py
"""
from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://local-eats-unisenac.vercel.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        print("=== TITLE ===")
        print(page.title())
        print()
        print("=== HEADINGS ===")
        for h in page.locator("h1, h2, h3").all():
            try:
                print(f"- {h.evaluate('el => el.tagName')}: {h.text_content()!r}")
            except Exception:
                pass
        print()
        print("=== LINKS ===")
        for a in page.locator("a").all()[:25]:
            try:
                print(f"- href={a.get_attribute('href')!r} text={a.text_content()!r}")
            except Exception:
                pass
        print()
        print("=== BUTTONS ===")
        for b in page.locator("button").all()[:25]:
            try:
                print(f"- text={b.text_content()!r}")
            except Exception:
                pass
        print()
        print("=== INPUTS ===")
        for i in page.locator("input").all()[:10]:
            try:
                print(f"- type={i.get_attribute('type')!r} placeholder={i.get_attribute('placeholder')!r} name={i.get_attribute('name')!r}")
            except Exception:
                pass
        print()
        print("=== POSSIBLE CARDS ===")
        for sel in ["article", ".restaurant-card", "[data-testid='restaurant-card']", ".card", "main > div > div"]:
            count = page.locator(sel).count()
            if count:
                print(f"- {sel}: {count} elementos")

        browser.close()


if __name__ == "__main__":
    main()
