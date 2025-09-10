import requests
import os

API_KEY = 'HOTtbQ96mgumakMCNOzUCGNslDyArO7joPvwzVyNHWBxv2aERnbO4Qzh'
headers = {'Authorization': API_KEY}
query = 'Lake'
per_page = 2000  # Max per request
page = 1

save_dir = 'pexels_videos'
os.makedirs(save_dir, exist_ok=True)

response = requests.get(
    f'https://api.pexels.com/videos/search?query={query}&per_page={per_page}&page={page}',
    headers=headers
)

data = response.json()
videos = data.get('videos', [])

downloaded = 0
for video in videos:
    width = video.get('width')
    height = video.get('height')

    # ✅ Filter: Only download horizontal videos
    if width and height and width > height:
        video_url = video['video_files'][0]['link']
        video_id = video['id']
        r = requests.get(video_url)
        with open(os.path.join(save_dir, f'video_{video_id}.mp4'), 'wb') as f:
            f.write(r.content)
        downloaded += 1

print(f"Download complete! {downloaded} horizontal videos saved.")
