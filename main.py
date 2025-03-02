from pypresence import Presence
from playerctl_utils import get_artists, get_track_name, get_art_url
import time

RPC = Presence("1345518060727177347")
last_track = None

def update_rpc():
    global last_track
    artists = get_artists()
    track = get_track_name()
    art_url = get_art_url()
    current_track = (track, artists, art_url)
    if current_track != last_track:
        last_track = current_track
        RPC.connect()
        RPC.update(
        state=f"{artists}",  # Display artist names
        details=f"{track}",  # Display the track name
        large_image=art_url,  # URL for album art
        large_text=f"{track}"  # Text shown when hovering over the image
        )
        print(f"Updated presence: {track} by {artists}")
    else:
        print("Same track, not updating presence")
if __name__ == "__main__":
    while True:
        update_rpc()
        time.sleep(5)