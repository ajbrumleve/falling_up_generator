import lyricsgenius
import config

genius = lyricsgenius.Genius(config.GENIUS_TOKEN)

artist = genius.search_artist("falling_up", sort="title")

print(len(artist.songs))
with open('falling_up.txt', 'w', encoding='utf-8') as f:
    f.write(artist.songs[0].lyrics)
for item in artist.songs[1:]:
    with open('falling_up.txt', 'a',encoding='utf-8') as f:
        f.write('\n')
        f.write(item.lyrics)
