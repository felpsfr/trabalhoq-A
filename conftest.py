"""Conftest raiz — fixtures compartilhadas entre as suítes E2E e BDD.

Mantém um único `sync_playwright()` por sessão para evitar conflito de event loop
quando as duas suítes rodam no mesmo `pytest`.
"""
from __future__ import annotations

import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    b = playwright_instance.chromium.launch(headless=True)
    yield b
    b.close()


@pytest.fixture
def page(browser: Browser):
    context = browser.new_context(viewport={"width": 1280, "height": 800}, locale="pt-BR")
    p: Page = context.new_page()
    p.set_default_timeout(15_000)
    yield p
    context.close()
