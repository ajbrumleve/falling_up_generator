import re

import lyricsgenius
import config
import os

def scrape_lyric(artist_list):
    file_list=[]
    genius = lyricsgenius.Genius(config.GENIUS_TOKEN,timeout=20,sleep_time=1,retries=5)

    for name in artist_list:
        if not os.path.exists('lyrics/{}.txt'.format(name).lower()):
            artist = genius.search_artist(name, sort="title")


            print(len(artist.songs))
            with open('lyrics/{}.txt'.format(artist.name).lower(), 'w', encoding='utf-8') as f:
                print("running")
                s = artist.songs[0].lyrics
                s = re.sub(r'^(.* ?)Lyrics', r'', s)
                s = re.sub(r'\[(.*?)\]', r'', s)
                s = re.sub(r'You might also like', r'', s)
                s = re.sub(r'[1-9].*Embed', r'', s)
                s = re.sub(r'Embed$', r'', s)
                print(s)
                f.write(s)
            for item in artist.songs[1:]:
                sl = item.lyrics
                sl = re.sub(r'^(.* ?)Lyrics', r'', sl)
                sl = re.sub(r'\[(.*?)\]', r'', sl)
                sl = re.sub(r'You might also like', r'', sl)
                sl = re.sub(r'[1-9].*Embed', r'', sl)
                sl = re.sub(r'.*?(Embed)$', r'', sl)
                print(sl)
                with open('lyrics/{}.txt'.format(artist.name).lower(), 'a', encoding='utf-8') as f:
                    f.write('\n')
                    f.write(sl)
            file_list.append('lyrics/{}.txt'.format(artist.name).lower())
        else:
            file_list.append('lyrics/{}.txt'.format(name).lower())
    return file_list
def lyrics_cleaning(text_file):
    with open(text_file,encoding='utf-8') as f:
        s = f.read()

    # Safely write the changed content, if found in the file
    with open(text_file, 'w',encoding='utf-8') as f:
        s = re.sub(r'^(.* ?)Lyrics', r'', s)
        s = re.sub(r'\[(.*?)\]', r'', s)
        s = re.sub(r'You might also like', r'', s)
        s = re.sub(r'[1-9].*Embed', r'', s)
        s = re.sub(r'embed$', r'', s)
        f.write(s)
    return