import json
import os
import asyncio
from playwright.async_api import async_playwright

async def render_pdf():
    html_file = f"file://{os.path.abspath('index.html')}"
    pdf_path = "build/suhani-birthday-book.pdf"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(html_file, wait_until="networkidle")
        
        # Take a screenshot of the first page to show the user
        await page.screenshot(path="build/cover-preview.png", full_page=False)
        
        await page.pdf(
            path=pdf_path,
            width="8in",
            height="8in",
            print_background=True,
            display_header_footer=False
        )
        await browser.close()
    print(f"Generated {pdf_path}")

if __name__ == "__main__":
    asyncio.run(render_pdf())
