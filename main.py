import genius_scrape
import lyrics_generator

artist_name_next_bool = True
artist_list=[]
artist_name=input("What artist's style do you want to generate?")
artist_list.append(artist_name)
while artist_name_next_bool == True:
    add_artist = input("Would you like to add another artist's style? Y/n")
    if add_artist.lower() == "y" or add_artist.lower() == "yes":
        artist_name_next = input("Which artist?")
        artist_list.append(artist_name_next)
    elif add_artist.lower() == "n" or add_artist.lower() == "no":
        artist_name_next_bool = False
    else:
        print("Invalid input")
file_list = genius_scrape.scrape_lyric(artist_list)
model = lyrics_generator.lyric_model()
model.run_generator(file_list)
print("You can now generate lyrics")
while True:
    num_lines = input("How many lines do you want?")
    model.generate(int(num_lines))
    more_lines = input("Would you like to generate more lines? Y/N")
    if more_lines.lower() == "n" or more_lines.lower() == "no":
        break
