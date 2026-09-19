import os
import asyncio
from playwright.async_api import async_playwright

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Suhani's Surprise Plan</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&family=Nunito:wght@400;700&display=swap');
    body { font-family: 'Nunito', sans-serif; padding: 40px; color: #4A192C; background: #FAF6F0; }
    @page { size: A4; margin: 0; }
    h1 { font-family: 'Fredoka', sans-serif; color: #D21F3C; font-size: 3rem; text-align: center; }
    .card { background: white; padding: 15px; border-radius: 8px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); margin-bottom: 10px; border-left: 5px solid #FFB6C1; }
    h2 { font-family: 'Fredoka', sans-serif; margin-bottom: 5px; color: #D21F3C; }
    .rules { background: #FFFDD0; padding: 20px; border-radius: 8px; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>The Kiddo Surprise Protocol 🎂</h1>
  <div style="display: flex; gap: 20px;">
    <div style="flex: 1;">
      <h2>Timeline</h2>
      <ul style="line-height: 1.8;">
        <li><strong>T-45 mins:</strong> Setup & Decor</li>
        <li><strong>T-10 mins:</strong> Final Positions</li>
        <li><strong>T-0:</strong> Suhani Arrives</li>
        <li><strong>T+5 mins:</strong> Play Birthday Film</li>
        <li><strong>T+8 mins:</strong> Cake & Song</li>
        <li><strong>T+15 mins:</strong> Book Presentation</li>
      </ul>
      
      <h2>Roles (Template)</h2>
      <div class="card"><strong>Ansh:</strong> Distract Suhani, bring her in.</div>
      <div class="card"><strong>Pau:</strong> Cake & gift coordination.</div>
      <div class="card"><strong>Lavi:</strong> Lights & Poppers.</div>
      <div class="card"><strong>Kashish/Khushi:</strong> Camera & Video.</div>
    </div>
    
    <div style="flex: 1;" class="rules">
      <h2>Strict Rules 🛑</h2>
      <ul style="line-height: 1.8;">
        <li>Nobody mentions the book.</li>
        <li>Nobody reveals the surprise.</li>
        <li>Nobody posts before the surprise.</li>
        <li>No phone screens during the film.</li>
        <li>Start the film from the beginning.</li>
        <li>Keep the book hidden until the correct moment.</li>
      </ul>
    </div>
  </div>
</body>
</html>
"""

async def build_surprise():
    with open("suhani-birthday/surprise/plan.html", "w") as f:
        f.write(html)
        
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file://{os.path.abspath('suhani-birthday/surprise/plan.html')}")
        await page.pdf(path="suhani-birthday/build/suhani-surprise-plan.pdf", format="A4")
        await browser.close()
    print("Generated suhani-surprise-plan.pdf")

if __name__ == "__main__":
    os.makedirs("suhani-birthday/surprise", exist_ok=True)
    asyncio.run(build_surprise())
