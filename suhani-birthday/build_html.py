import json
import os

with open("content.json", "r") as f:
    content = json.load(f)

with open("photos/map.json", "r") as f:
    photos = json.load(f)

html_top = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Suhani's 20th Birthday Book</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""

html_bottom = """
</body>
</html>
"""

pages = []

# Page 1: Cover
cover_photo = "cover.jpeg"
pages.append(f"""
  <section class="page page-cover">
    
    <div class="torn-paper">
      <h3>SUHANI<br>TURNS 20</h3>
      <p>Jaipur, September 23</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae eleifend magna. Curabitur sed nunc nec nisi ultricies commodo. Duis sit amet ipsum eu turpis ullamcorper sollicitudin. Proin facilisis, urna vel fringilla cursus.</p>
      <p>Aliquam erat volutpat. Phasellus ut condimentum diam, sed pulvinar purus. Sed ullamcorper dui nec tortor tristique sagittis. Sed vel nisl non dolor pretium condimentum. Vivamus egestas, dolor at congue tincidunt.</p>
      <p>Pellentesque id nunc metus. Aenean dignissim mi rhoncus libero cursus pulvinar. Etiam fringilla sit amet massa efficitur gravida. Ut id leo lacus. Aenean nec eros vitae urna vehicula tincidunt sit amet finibus nunc.</p>
    </div>

    <div class="scrapbook-photo-container">
      <div class="photo-wrapper">
        <img class="scrapbook-photo" src="photos/originals/{cover_photo}" alt="Suhani">
      </div>
    </div>

    <div class="main-title">Suhani</div>
    <div class="sub-title">Happy 20th Birthday</div>
    <div class="love-text">A little book of love, just for you</div>

    <div class="stamp-20">20</div>
    <div class="bubble-20">20</div>

    <!-- Stickers -->
    <div class="sticker sticker-sun">☀️</div>
    <div class="sticker sticker-balloons">🎈</div>
    <div class="sticker sticker-sunflower">🌻</div>
    <div class="sticker sticker-cat">🐱</div>

  </section>
""")

# Page 2: Endpaper with Photo Collage
pages.append(f"""
  <section class="page page-endpaper" style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; padding: 20px;">
    <div class="photo-stamp" style="transform: rotate(5deg); width: 200px; height: 250px; margin: 10px;"><img src="photos/originals/1.jpeg" alt=""></div>
    <div class="photo-stamp" style="transform: rotate(-4deg); width: 220px; height: 270px; margin: 10px;"><img src="photos/originals/2.jpeg" alt=""></div>
    <div class="photo-stamp" style="transform: rotate(7deg); width: 180px; height: 220px; margin: 10px;"><img src="photos/originals/3.jpeg" alt=""></div>
    <div class="photo-stamp" style="transform: rotate(-6deg); width: 210px; height: 260px; margin: 10px;"><img src="photos/originals/4.jpeg" alt=""></div>
  </section>
""")

# Page 3: Dedication
pages.append(f"""
  <section class="page page-dedication">
    <div class="journal-card">
      <div class="tape" style="top: -15px; transform: translateX(-50%) rotate(3deg); background: rgba(255,182,193,0.5);"></div>
      <h2>For Kiddo,</h2>
      <p class="handwriting" style="font-size: 2rem; line-height: 1.5; color: var(--plum);">
        A collection of 20 years of memories, love, fights, <br>
        annoying moments, and the people who make it all worthwhile.<br><br>
        Happy 20th Birthday. ❤️<br>
        — From {content['from']}
      </p>
    </div>
  </section>
""")

# Build the rest of the HTML

# Page 4: Quotes
quotes_html = "".join([f'<div class="sticky-note" style="transform: rotate({i*5-10}deg);">{q}</div>' for i, q in enumerate(content['quotes'])])
photo_quotes = photos.get("photo2", {}).get("file", "photo_002.jpeg")
pages.append(f"""
  <section class="page" style="background-color: var(--pink);">
    <h2 class="section-title">Things Kiddo Actually Says</h2>
    <div class="photo-stamp" style="align-self: center; transform: rotate(-5deg); width: 250px; height: 300px;"><img src="photos/originals/{photo_quotes}" alt=""></div>
    <div class="grid-container">
      {quotes_html}
    </div>
  </section>
""")

# Page 5: Habits
habits_html = "".join([f'<div class="sticky-note" style="background: var(--cream); transform: rotate({i%2 == 0 and 3 or -3}deg); width: 100%; margin-bottom: 15px;">{h}</div>' for i, h in enumerate(content['habits'])])
photo_habits = photos.get("photo3", {}).get("file", "photo_003.jpeg")
pages.append(f"""
  <section class="page" style="background-image: radial-gradient(rgba(0,0,0,0.1) 1px, transparent 1px); background-size: 15px 15px;">
    <h2 class="section-title">Things You Do</h2>
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        {habits_html}
      </div>
      <div style="flex: 1; display: flex; flex-direction: column; align-items: center;">
        <div class="photo-stamp" style="width: 250px; height: 300px;"><img src="photos/originals/{photo_habits}" alt=""></div>
        <div class="handwriting" style="margin-top: 10px;">(And I love you for it)</div>
      </div>
    </div>
  </section>
""")

# Page 6: Favorites
fav_html = ""
for category, items in content['favorites'].items():
    fav_html += f"<h3>{category.title()}</h3><p>{', '.join(items)}</p>"
pages.append(f"""
  <section class="page" style="background-color: var(--lilac);">
    <h2 class="section-title">Things That Make You, You</h2>
    <div class="journal-card" style="margin: 0 auto;">
      {fav_html}
    </div>
  </section>
""")

# Page 6.5: Newspaper Slide
pages.append(f"""
  <section class="page page-newspaper">
    <div class="newspaper-extra-sticker">EXTRA!</div>
    
    <div class="newspaper-header">
      <h1 class="newspaper-title">THE SUHANI TIMES</h1>
    </div>
    <div class="newspaper-meta">
      Wednesday, 23 September 2026 &bull; Jaipur &bull; Vol. 20, No. 1 &bull; Price: one smile
    </div>

    <h2 class="newspaper-headline">SUHANI TURNS 20</h2>
    <div class="newspaper-subtitle">City celebrates. Cat unavailable for comment.</div>

    <div class="newspaper-grid">
      
      <!-- Column 1 -->
      <div class="newspaper-col-1">
        <img class="newspaper-photo" src="photos/originals/3.jpeg" alt="Suhani">
        <div class="newspaper-caption">
          Ms Suhani, 20, seen smiling. Sources say this is how she actually looks.
        </div>
      </div>

      <!-- Column 2 -->
      <div class="newspaper-col-2">
        <div class="newspaper-article">
          <strong>TEENAGE YEARS OFFICIALLY EXPIRE.</strong> Suhani has officially left the chat of her teen years. Sources close to her report she still feels 16, but her ID card now demands she act like an adult. We wish her luck.
        </div>
        <div class="newspaper-article">
          <strong>CAFFEINE DEPENDENCY AT ALL-TIME HIGH.</strong> Local cafes report a sudden surge in cold coffee orders. "We can barely keep up with her iced latte demands," said one barista.
        </div>
        <div class="newspaper-article">
          <strong>WARDROBE CRISIS CONTINUES.</strong> Despite owning a closet full of clothes, Suhani was reportedly heard saying, "I have absolutely nothing to wear." The mystery remains unsolved.
        </div>
        <div class="newspaper-article">
          <strong>WANTED.</strong> A remote control that pauses time so she can sleep an extra 10 minutes every morning. Reward: Endless gratitude.
        </div>
        <div class="newspaper-article">
          <strong>WEATHER UPDATE.</strong> 100% chance of her looking stunning today, with scattered moments of random giggles.
        </div>
      </div>

      <!-- Column 3 -->
      <div class="newspaper-col-3">
        <div class="newspaper-article">
          <strong>ALSO IN 2006.</strong> You were born! But also, Pluto was downgraded from a planet to a "dwarf planet." Coincidence? We think not. You took its place as the star.
        </div>
        <div class="newspaper-article">
          <strong>YOUNGER THAN YOU.</strong> The original iPhone (2007), WhatsApp (2009), Instagram (2010), and TikTok (2016). You are officially vintage.
        </div>
        <div class="newspaper-article">
          <strong>HOROSCOPE (Virgo).</strong> You will overthink a tiny detail today, but you will also accomplish everything on your to-do list while looking effortlessly cute.
        </div>
        <div class="newspaper-article">
          <strong>LATE NIGHT SNACKING.</strong> Fridge door reportedly opened 14 times between 1 AM and 3 AM. Suspect remains at large.
        </div>
        <div class="newspaper-article">
          <strong>QUOTE OF THE DAY.</strong> "I'll be ready in 5 minutes." (Narrator: She was not ready in 5 minutes).
        </div>
      </div>

    </div>
  </section>
""")

# Page 7: Letters Opener
pages.append(f"""
  <section class="page" style="background-color: var(--pink); justify-content: center; align-items: center;">
    <h2 class="section-title" style="font-size: 4rem; color: white;">Letters for You</h2>
    <div class="photo-stamp" style="width: 300px; height: 350px; transform: rotate(4deg);"><img src="photos/originals/{photos.get('photo4', dict()).get('file', 'photo_004.jpeg')}" alt=""></div>
  </section>
""")

# Main Letter Pages
main_letter_text = content['main_letter']
paragraphs = [p for p in main_letter_text.split('\n') if p.strip()]
chunk_size = 6 if len(main_letter_text) > 1000 else len(paragraphs)
chunks = [paragraphs[i:i + chunk_size] for i in range(0, len(paragraphs), chunk_size)]

for i, chunk in enumerate(chunks):
    chunk_html = "".join([f"<p style='margin-bottom: 15px; font-size: 1rem;'>{p}</p>" for p in chunk])
    title = "A Letter For You"
    if i > 0:
        title += " (Continued)"
        
    pages.append(f"""
      <section class="page">
        <h2 class="section-title" style="font-size: 2rem; margin-bottom: 10px; text-align: left;">{title}</h2>
        <div class="journal-card" style="width: 100%; height: 85%; padding: 20px; box-sizing: border-box;">
          <div style="font-size: 1rem; line-height: 1.5; color: var(--plum);">
            {chunk_html}
          </div>
        </div>
      </section>
    """)

# Wishes Opener
pages.append(f"""
  <section class="page" style="background-color: var(--gold); justify-content: center; align-items: center;">
    <h2 class="section-title" style="font-size: 4rem; color: white;">Wishes For You</h2>
    <div class="photo-stamp" style="width: 300px; height: 350px; transform: rotate(-3deg);"><img src="photos/originals/s1.jpeg" alt=""></div>
  </section>
""")

# Wishes Pages
for person, wish_text in content.get('wishes', {}).items():
    paragraphs = [p for p in wish_text.split('\n') if p.strip()]
    chunk_size = 6 if len(wish_text) > 1000 else len(paragraphs)
    chunks = [paragraphs[i:i + chunk_size] for i in range(0, len(paragraphs), chunk_size)]
    
    for i, chunk in enumerate(chunks):
        chunk_html = "".join([f"<p style='margin-bottom: 15px; font-size: 1rem;'>{p}</p>" for p in chunk])
        title = f"From {person.title().replace('_', ' ')}"
        if i > 0:
            title += " (Continued)"
            
        photo_insert = ""
        if person == 'sushmita' and i == 0:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(5deg);"><img src="photos/originals/sushmita.jpeg" alt="Sushmita"></div>'
        elif person == 'roshni' and i == 0:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(-4deg);"><img src="photos/originals/roshni.jpeg" alt="Roshni"></div>'
        elif person == 'lavi' and i == 0:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(3deg);"><img src="photos/originals/lavi.jpeg" alt="Lavi"></div>'
        elif person == 'khushi' and i == 0:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(-3deg);"><img src="photos/originals/khushi.jpeg" alt="Khushi"></div>'
        elif person == 'ansh' and i == 0:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(2deg);"><img src="photos/originals/a2.jpeg" alt="Ansh"></div>'
        elif person == 'ansh' and i == 1:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(-3deg);"><img src="photos/originals/a3.jpeg" alt="Ansh"></div>'
        elif person == 'ansh' and i == 2:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(4deg);"><img src="photos/originals/a5.jpeg" alt="Ansh"></div>'
        elif person == 'ansh' and i == 3:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(-5deg);"><img src="photos/originals/a4.jpeg" alt="Ansh"></div>'
        elif person == 'ansh' and i == 4:
            photo_insert = '<div class="photo-stamp" style="float: right; width: 220px; height: 260px; margin-left: 15px; margin-bottom: 10px; transform: rotate(3deg);"><img src="photos/originals/a6.jpeg" alt="Ansh"></div>'
        elif person == 'ansh' and i == 5:
            chunk_html += '<div style="text-align: center; margin-top: 30px;"><div class="photo-stamp" style="display: inline-block; width: 240px; height: 280px; transform: rotate(-2deg);"><img src="photos/originals/a1.jpeg" alt="Ansh"></div></div>'
        elif person == 'pau' and i == 0:
            chunk_html += '<div style="text-align: center; margin-top: 30px;"><div class="photo-stamp" style="display: inline-block; width: 220px; height: 260px; transform: rotate(3deg);"><img src="photos/originals/pau.jpeg" alt="Pau"></div></div>'
        elif person == 'kashish' and i == 0:
            photo_insert = '''
            <div style="float: right; width: 340px; display: flex; flex-wrap: wrap; justify-content: center; margin-left: 15px; margin-bottom: 10px;">
              <div class="photo-stamp" style="width: 140px; height: 160px; transform: rotate(-5deg); margin: 5px;"><img src="photos/originals/kashish.jpeg" alt="Kashish"></div>
              <div class="photo-stamp" style="width: 140px; height: 160px; transform: rotate(4deg); margin: 5px;"><img src="photos/originals/kashis1.jpeg" alt="Kashish"></div>
              <div class="photo-stamp" style="width: 200px; height: 230px; transform: rotate(-2deg); margin: 8px;"><img src="photos/originals/kashish2.jpeg" alt="Kashish"></div>
            </div>
            '''
            
        pages.append(f"""
          <section class="page">
            <h2 class="section-title" style="font-size: 2rem; margin-bottom: 10px; text-align: left;">{title}</h2>
            <div class="journal-card" style="width: 100%; height: 85%; padding: 20px; box-sizing: border-box;">
              <div style="font-size: 1rem; line-height: 1.5; color: var(--plum);">
                {photo_insert}
                {chunk_html}
              </div>
            </div>
          </section>
        """)

# Final Pages
pages.append(f"""
  <section class="page" style="background-color: var(--pink); justify-content: center; align-items: center; text-align: center; padding: 40px;">
    
    <div style="font-family: 'Fredoka', sans-serif; font-size: 2.5rem; color: white; margin-bottom: 30px; text-shadow: 2px 2px 0px rgba(0,0,0,0.1); line-height: 1.3;">
      "Some people make the world more beautiful just by being in it."
    </div>

    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin-bottom: 40px;">
      <div class="photo-stamp" style="width: 180px; height: 210px; transform: rotate(-6deg);"><img src="photos/originals/s2.jpeg" alt=""></div>
      <div class="photo-stamp" style="width: 200px; height: 240px; transform: rotate(4deg); margin-top: 20px;"><img src="photos/originals/s3.jpeg" alt=""></div>
      <div class="photo-stamp" style="width: 170px; height: 200px; transform: rotate(-3deg);"><img src="photos/originals/s4.jpeg" alt=""></div>
    </div>

    <div class="title-sticker" style="font-size: 3.5rem; transform: rotate(-2deg); margin-bottom: 20px; z-index: 10;">HAPPY 20TH, KIDDO</div>
    
    <div class="handwriting" style="font-size: 2.5rem; color: var(--plum); margin-top: 10px; z-index: 10;">
      Here's to a lifetime of us. ❤️
    </div>
  </section>
""")

full_html = html_top + "\n".join(pages) + html_bottom

with open("index.html", "w") as f:
    f.write(full_html)

print("Generated index.html")
