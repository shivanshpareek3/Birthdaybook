import os
import random
from PIL import Image
import numpy as np

# Use moviepy 2.x syntax
from moviepy import *

def create_reel(image_folder, output_file):
    # Get list of images
    # Only use Ansh's photos
    images = [os.path.join(image_folder, f"a{i}.jpeg") for i in range(1, 7) if os.path.exists(os.path.join(image_folder, f"a{i}.jpeg"))]
    
    # Shuffle or select a subset to make a ~30 second reel
    random.shuffle(images)
    selected_images = images # Use all Ansh photos
    
    # Reel dimensions
    W, H = 1080, 1920
    
    clips = []
    # 30 seconds total, 6 images = 5.0 seconds each
    duration_per_image = 30.0 / len(selected_images) if selected_images else 5.0
    
    for idx, img_path in enumerate(selected_images):
        try:
            # Resize image to fit inside 1080x1920, pad with black or crop
            # moviepy v2 handles resizing with ImageClip
            # Let's open with PIL to resize and crop to 9:16 to avoid stretching
            with Image.open(img_path) as pil_img:
                pil_img = pil_img.convert("RGB")
                img_w, img_h = pil_img.size
                
                # Calculate aspect ratios
                target_ratio = W / H
                img_ratio = img_w / img_h
                
                if img_ratio > target_ratio:
                    # Image is wider, crop width
                    new_w = int(img_h * target_ratio)
                    left = (img_w - new_w) // 2
                    pil_img = pil_img.crop((left, 0, left + new_w, img_h))
                else:
                    # Image is taller, crop height
                    new_h = int(img_w / target_ratio)
                    top = (img_h - new_h) // 2
                    pil_img = pil_img.crop((0, top, img_w, top + new_h))
                    
                pil_img = pil_img.resize((W, H), Image.Resampling.LANCZOS)
                
                # Convert back to numpy array for moviepy
                img_array = np.array(pil_img)
            
            # Create ImageClip
            clip = ImageClip(img_array).with_duration(duration_per_image)
            
            # Add simple animation based on index
            if idx % 2 == 0:
                # Zoom in effect
                clip = clip.resized(lambda t: 1 + 0.05*t)
            else:
                # Zoom out effect
                clip = clip.resized(lambda t: 1.1 - 0.05*t)
            
            # Fade transition
            clip = clip.with_effects([vfx.CrossFadeIn(0.5)]) if idx > 0 else clip
            
            # Only on the first image, overlay beautifully designed Happy Birthday at the top
            if idx == 0:
                # Create styled text clip, smaller font and positioned top
                txt = TextClip(text=" Happy Birthday! ", font_size=80, color="gold",
                               bg_color="rgba(0,0,0,150)", stroke_color="white", stroke_width=2, method="label")
                txt = txt.with_position(("center", 200)).with_duration(duration_per_image).with_effects([vfx.CrossFadeIn(0.5)])
                clip = CompositeVideoClip([clip, txt])
                
            clips.append(clip)
            
        except Exception as e:
            print(f"Error processing {img_path}: {e}")
            
    # Concatenate clips
    final_video = concatenate_videoclips(clips, method="compose")
    
    # Check if we have audio, else just write without audio
    if os.path.exists("punjabi_romantic_party.mp3"):
        audio = AudioFileClip("punjabi_romantic_party.mp3")
        # Loop the audio to match the video duration
        audio = audio.with_effects([afx.AudioLoop(duration=final_video.duration)])
        final_video = final_video.with_audio(audio)
    
    # Write result
    final_video.write_videofile(output_file, fps=30, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    image_dir = "/Users/apple/Desktop/Birthday book"
    out_file = "/Users/apple/Desktop/Birthday book/birthday_reel.mp4"
    create_reel(image_dir, out_file)
    print(f"Reel saved to {out_file}")
