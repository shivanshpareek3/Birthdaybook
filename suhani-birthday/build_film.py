import json
import os
import random

def generate_film():
    with open('content.json', 'r') as f:
        content = json.load(f)

    # Prepare exactly 35 beautiful, romantic, and sweet lines for the film
    raw_texts = [
        "To the girl who makes my world brighter...",
        "Happy 20th Birthday, my beautiful Suhani. ❤️",
        "It feels like just yesterday we met, yet I can't imagine life without you.",
        "Your smile is my favorite thing in the whole world.",
        "Even when you're angry, you look incredibly cute.",
        "I love how we can talk about everything and nothing all at once.",
        "You are the peace in my chaotic days.",
        "Every time you laugh, my heart skips a beat.",
        "I cherish every silly argument and every sweet makeup.",
        "You're not just my girl, you're my best friend.",
        "I love the way your eyes light up when you see food.",
        "Your nakhre are tough to handle, but I wouldn't have it any other way.",
        "You make the ordinary moments feel extraordinary.",
        "I promise to always listen to your endless stories.",
        "Even your 'bhaad mae jao' sounds sweet to me now.",
        "You are the most beautiful part of my life.",
        "I love the way you say my name.",
        "You are my safe space, my home.",
        "I'll always be here to hold your hand.",
        "Your happiness means everything to me.",
        "I love you more than words could ever explain.",
        "You are the dream I never want to wake up from.",
        "I promise to always try my best for you.",
        "Even when you take 45 minutes to get ready...",
        "...it's always worth the wait, because you look stunning.",
        "I want to travel the world with you.",
        "I want to create a million more memories with you.",
        "You are my favorite notification.",
        "Thank you for being exactly who you are.",
        "Thank you for letting me be me.",
        "I love your kindness, your attitude, and your heart.",
        "Welcome to your 20s, my love.",
        "May this year bring you everything you desire.",
        "I will always be your biggest cheerleader.",
        "Here's to a lifetime of us. I love you, Kiddo. ❤️"
    ]
                
    # We want exactly 35 chunks for 2.5 minutes (35 * 4.3s = 150s)
    text_chunks = raw_texts[:35]
    if len(text_chunks) < 35:
        # pad with remaining quotes or habits
        for h in content.get('habits', []):
            text_chunks.append(h)
        for q in content.get('quotes', []):
            text_chunks.append(f'"{q}"')
    
    text_chunks = text_chunks[:35]

    # Get images
    photos_dir = 'photos/originals'
    all_photos = [f for f in os.listdir(photos_dir) if f.endswith('.jpeg')]
    random.seed(42) # fixed seed for consistency
    random.shuffle(all_photos)
    
    # Make sure we have 35 photos
    while len(all_photos) < 35:
        all_photos.extend(all_photos)
    selected_photos = all_photos[:35]

    # Build HTML
    html_scenes = []
    for i in range(35):
        img_src = f"../photos/originals/{selected_photos[i]}"
        text = text_chunks[i]
        
        scene_html = f"""
        <div class="scene" id="scene{i}">
          <img src="{img_src}" class="ken-burns" alt="Memory">
          <div class="text-overlay">
            <p>{text}</p>
          </div>
        </div>
        """
        html_scenes.append(scene_html)
        
    scenes_html_str = "\n".join(html_scenes)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Suhani's 20th Birthday Film</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Fredoka:wght@600&family=Nunito:wght@400;700&display=swap');
    
    body, html {{ 
      margin: 0; padding: 0; background: #0a0a0a; overflow: hidden; 
      display: flex; justify-content: center; align-items: center; 
      height: 100vh; width: 100vw;
      font-family: 'Nunito', sans-serif;
    }}
    
    /* Responsive Player Container */
    #player {{ 
      width: 100%; height: 100%; 
      position: relative; overflow: hidden; 
      background: black;
    }}
    
    .scene {{ 
      position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
      opacity: 0; transition: opacity 1.5s ease-in-out; 
      display: flex; flex-direction: column; justify-content: center; align-items: center; 
    }}
    .scene.active {{ opacity: 1; z-index: 10; }}
    
    .ken-burns {{ 
      position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
      object-fit: contain; /* ensures full image is visible */
      z-index: 1; 
      animation: none; 
      opacity: 0.8;
      filter: drop-shadow(0 0 20px rgba(255,255,255,0.1));
    }}
    
    /* Apply animation only to active scene */
    .active .ken-burns {{ 
      animation: kenburns 6s ease-out forwards; 
    }}
    
    @keyframes kenburns {{ 
      0% {{ transform: scale(1.0); }} 
      100% {{ transform: scale(1.15); }} 
    }}
    
    .text-overlay {{
      position: absolute;
      bottom: 10%;
      left: 5%;
      right: 5%;
      text-align: center;
      z-index: 10;
      background: rgba(0,0,0,0.4);
      padding: 20px;
      border-radius: 10px;
      backdrop-filter: blur(5px);
    }}
    
    .text-overlay p {{ 
      font-family: 'Caveat', cursive; 
      font-size: clamp(2rem, 5vw, 4rem); 
      font-weight: bold; 
      color: #fff; 
      margin: 0;
      text-shadow: 2px 2px 5px rgba(0,0,0,0.8), -1px -1px 0 rgba(0,0,0,0.5); 
      line-height: 1.3;
    }}

    #start-btn {{
      position: absolute;
      z-index: 100;
      padding: 15px 30px;
      font-family: 'Fredoka', sans-serif;
      font-size: 1.5rem;
      background: #D21F3C;
      color: white;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 5px 15px rgba(0,0,0,0.3);
      transition: transform 0.2s;
    }}
    #start-btn:hover {{ transform: scale(1.05); }}
    
    .hidden {{ display: none !important; }}
    
  </style>
</head>
<body>

  <button id="start-btn">▶ Play Birthday Film</button>

  <div id="player">
    {scenes_html_str}
  </div>
  
  <!-- Hidden YouTube Player for Background Music -->
  <div id="yt-player" class="hidden"></div>
  
  <script>
    const scenes = document.querySelectorAll('.scene');
    const startBtn = document.getElementById('start-btn');
    let current = 0;
    const SCENE_DURATION = 4300; // 4.3 seconds per scene
    
    // YouTube Player API
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
    var player;
    function onYouTubeIframeAPIReady() {{
      player = new YT.Player('yt-player', {{
        height: '0',
        width: '0',
        videoId: '7maJOI3QMu0', // Yiruma - River Flows in You (Beautiful Romantic Piano)
        playerVars: {{
          'autoplay': 0,
          'controls': 0,
          'loop': 1,
          'playlist': '7maJOI3QMu0'
        }},
      }});
    }}
    
    function nextScene() {{
      if(current > 0) scenes[current-1].classList.remove('active');
      if(current < scenes.length) {{
        scenes[current].classList.add('active');
        current++;
        setTimeout(nextScene, SCENE_DURATION);
      }} else {{
        // End of film
        scenes[current-1].innerHTML = '<div class="text-overlay" style="bottom: 40%;"><p style="font-size: 5rem;">Happy 20th Birthday, Kiddo! ❤️</p></div>';
      }}
    }}
    
    startBtn.addEventListener('click', () => {{
      startBtn.classList.add('hidden');
      
      // Play YouTube audio
      if (player && typeof player.playVideo === 'function') {{
        player.playVideo();
      }}
      
      // Start the film
      nextScene();
    }});
  </script>
</body>
</html>
"""

    with open('film/index.html', 'w') as f:
        f.write(html_content)
        
    print("Generated film/index.html with 35 cinematic scenes!")

if __name__ == "__main__":
    generate_film()
