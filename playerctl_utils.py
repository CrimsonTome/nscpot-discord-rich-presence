import subprocess

def get_artists():
    result = subprocess.run(["playerctl", "--player=ncspot", "metadata"], stdout=subprocess.PIPE, text=True)
    # Find all lines containing "artist" and extract the artist names and join them
    artists = []
    for line in result.stdout.splitlines():
        if "artist" in line:
            artist = line.split("artist")[-1].strip()
            artists.append(artist)
    return ", ".join(artists)

def get_track_name():
    result = subprocess.run(["playerctl", "--player=ncspot", "metadata"], stdout=subprocess.PIPE, text=True)
    # Find the line containing "title" and extract the track name
    track_line = next((line for line in result.stdout.splitlines() if "title" in line), None)
    return track_line.split("title")[-1].strip() if track_line else None

def get_art_url():
    result = subprocess.run(["playerctl", "--player=ncspot", "metadata"], stdout=subprocess.PIPE, text=True)
    # Find the line containing "artUrl" and extract the URL
    art_line = next((line for line in result.stdout.splitlines() if "artUrl" in line), None)
    return art_line.split("artUrl")[-1].strip() if art_line else None
