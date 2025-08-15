from random import choice, shuffle

#create a list of rock bands
rock_bands = [['Led Zeppelin', 'rock', 'classic rock'],
              ['Pink Floyd', 'rock', 'progressive rock'],
              ['The Beatles', 'rock', 'Psychedelic rock'],
              ['Nirvana', 'rock', 'grunge'],
              ['slayer', 'rock', 'thrash metal'],
              ['Motorhead', 'rock', 'heavy metal'],
              ['Soundgarden', 'rock', 'grunge'],
              ['Radiohead', 'rock', 'alternative rock'],
              ['The Cranberries', 'rock', 'alternative rock'],
              ['Ramones', 'rock', 'punk rock'],
              ['Foo Fighters', 'rock', 'alternative rock'],
              ['Queen', 'rock', 'classic rock'],
              ['Jeff Beck', 'rock', 'blues rock'],
              ['The Who', 'rock', 'classic rock'],
              ['Dead Kennedys', 'rock', 'punk rock'],
              ['Deep Purple', 'rock', 'Classic rock'],
              ['sex pistols', 'rock', 'punk rock'],
              ['The Clash', 'rock', 'punk rock'],
              ['Van Halen', 'rock', 'Classic rock'],
              ['The Doors', 'rock', 'psychedelic rock'],
              ['AC/DC', 'rock', 'hard rock'],
              ['Guns N\' Roses', 'rock', 'hard rock'],
              ['Alice in Chains', 'rock', 'grunge'],
              ['Pearl Jam', 'rock', 'grunge'],
              ['Black Sabbath', 'rock', 'heavy metal'],
              ['Jimi Hendrix Experience', 'rock', 'psychedelic rock'],
              ['The Smiths', 'rock', 'alternative rock'],
              ['The Misfits', 'rock', 'horror punk'],
              ['The Stooges', 'rock', 'proto-punk'],
              ['The Velvet Underground', 'rock', 'art rock'],
              ['Joy Division', 'rock', 'post-punk'],
              ['The Cure', 'rock', 'gothic rock'],
              ['R.E.M.', 'rock', 'alternative rock'],
              ['The White Stripes', 'rock', 'garage rock'],
              ['Arctic Monkeys', 'rock', 'indie rock'],
              ['Paramore', 'rock', 'pop punk'],
              ['Linkin Park', 'rock', 'nu metal'],
              ['System of a Down', 'rock', 'alternative metal'],
              ['Metallica', 'rock', 'thrash metal'],
              ['Anthrax', 'rock', 'thrash metal'],
              ['Megadeth', 'rock', 'thrash metal'],
              ['Slipknot', 'rock', 'nu metal'],
              ['Limp Bizkit', 'rock', 'nu metal'],
              ['Morbid Angel', 'rock', 'death metal'],
              ['Death', 'rock', 'death metal'],
              ['Cannibal Corpse', 'rock', 'death metal'],
              ['Korn', 'rock', 'nu metal'],
              ['Dying Fetus', 'rock', 'death metal'],
              ['Suffocation', 'rock', 'death metal'],
              ['Opeth', 'rock', 'progressive metal'],
              ['Tool', 'rock', 'progressive metal'],
              ['Sepultura', 'rock', 'groove metal'],
              ['Pantera', 'rock', 'groove metal'],
              ['Carcass', 'rock', 'Melodic death metal'],
              ['At The Gates', 'rock', 'Melodic death metal'],
              ['In Flames', 'rock', 'Melodic death metal'],
              ['Kiss', 'rock', 'classic rock', 'glam rock'],
              ['Aerosmith', 'rock', 'classic rock'],
              ['Def Leppard', 'rock', 'classic rock'],
              ['Bon Jovi', 'rock', 'classic rock'],
              ['Scorpions', 'rock', 'hard rock'],
              ['Journey', 'rock', 'classic rock'],
              ['Boston', 'rock', 'classic rock'],
              ['Styx', 'rock', 'classic rock'],
              ['Foreigner', 'rock', 'classic rock'],
              ['Cheap Trick', 'rock', 'power pop'],
              ['Heart', 'rock', 'classic rock'],
              ['Fleetwood Mac', 'rock', 'soft rock'],
              ['Eagles', 'rock', 'soft rock'],
              ['Lynyrd Skynyrd', 'rock', 'southern rock'],
              ['The Allman Brothers Band', 'rock', 'southern rock'],
              ['Bob Seger', 'rock', 'classic rock'],
              ['Ozzy Osbourne', 'rock', 'heavy metal'],
              ['My Chemical Romance', 'rock', 'emo'],
              ['Blink-182', 'rock', 'pop punk'],
              ['Green Day', 'rock', 'punk rock'],
              ['Nine Inch Nails', 'rock', 'industrial rock'],
              ['Rage Against the Machine', 'rock', 'nu metal'],
              ['Motley Crue', 'rock', 'glam metal'],
              ['Rammstein', 'rock', 'industrial metal'],
              ['Type O Negative', 'rock', 'gothic metal'],
              ['Napalm Death', 'rock', 'grindcore'],
              ['S.O.D.', 'rock', 'grindcore'],
              ['Brutal Truth', 'rock', 'grindcore'],
              ['Repulsion', 'rock', 'grindcore'],
              ['Fall Out Boy', 'rock', 'pop punk'],
              ['Taking Back Sunday', 'rock', 'emo'],
              ['Between the Buried and Me', 'rock', 'progressive metal', 'mathcore'],
              ['The Dillinger Escape Plan', 'rock', 'mathcore'],
              ['Norma Jean', 'rock', 'metalcore'],
              ['Coal Chamber', 'rock', 'nu metal'],
              ['Coalesce', 'rock', 'mathcore'],
              ['The Number Twelve Looks Like You', 'rock', 'mathcore'],
              ['Heavy Heavy Low Low', 'rock', 'mathcore'],
              ['Car Bomb', 'rock', 'mathcore'],
              ['Converge', 'rock', 'metalcore'],
              ['motionless in White', 'rock', 'metalcore'],
              ['Killswitch Engage', 'rock', 'metalcore'],
              ['Rotten Sound', 'rock', 'grindcore'],
              ['Pig Destroyer', 'rock', 'grindcore'],
              ['Agoraphobic Nosebleed', 'rock', 'grindcore'],
              ['Cattle Decapitation', 'rock', 'deathgrind'],
              ['Misery Index', 'rock', 'deathgrind'],
              ['Aborted', 'rock', 'deathgrind'],
              ['Black Flag', 'rock', 'hardcore punk'],
              ['Minor Threat', 'rock', 'hardcore punk'],
              ['Bad Brains', 'rock', 'hardcore punk'],
              ['Living Colour', 'rock', 'hardcore punk'],
              ['Refused', 'rock', 'hardcore punk'],
              ['Tera Melos', 'rock', 'math rock'],
              ['The Mars Volta', 'rock', 'progressive rock'],
              ['Deftones', 'rock', 'alternative metal'],
              ['Faith No More', 'rock', 'alternative metal'],
              ['Helmet', 'rock', 'alternative metal'],
              ['Jane\'s Addiction', 'rock', 'alternative rock'],
              ['Soundwave', 'rock', 'post-hardcore'],
              ['Thursday', 'rock', 'post-hardcore'],
              ['Glassjaw', 'rock', 'post-hardcore'],
              ['Brand New', 'rock', 'emo'],
              ['Taking Back Sunday', 'rock', 'emo'],
              ['Dashboard Confessional', 'rock', 'emo']]

shuffle(rock_bands)

moods = {'happy', 'sad', 'energetic', 'relaxed'}

# Input mood
print(f"What is your current mood? (e.g. {', '.join(moods)})")
mood = input("Happy, Sad, Energetic, Relaxed, Depressed, Angry: ").strip().lower()

# Normalize mood input
mood = mood.replace(" ", "")

# Define a function to normalize the mood input
def normalize_mood(mood):
    mood_mapping = {
        'happy': 'happy',
        'sad': 'sad',
        'energetic': 'energetic',
        'relaxed': 'relaxed',
        'depressed': 'depressed',
        'angry': 'angry'
    }
    return mood_mapping.get(mood, None)

def map_mood(mood):
    mood_mapping = {
        'happy': ['numetal', 'pop punk', 'soft rock', 'classic rock'],
        'sad': ['soft rock', 'emo', 'post-hardcore'],
        ...: ...
    }
    return mood_mapping.get(mood, [])

mood = normalize_mood(mood)

# Check if the mood is valid
if mood is None:
    print("Invalid mood input. Please enter one of the following: Happy, Sad, Energetic, Relaxed, Depressed, Angry.")
    exit() 

rock_types = map_mood(mood)

# Print the mood
print(f"You are feeling {mood}.")

# Based on the mood, suggest a rock band
print("Here are some rock bands you might enjoy based on your mood:")


# loop through and find a band that matches the mood
for item in rock_bands:
    broke = False
    for rock_type in rock_types:
        if rock_type in item[1:]:
            print(f"Based on your mood, you might enjoy listening to {item[0]}, which is known for {', '.join(item[1:])}.")
            broke = True
            break
    if broke: break
else:
    print("Sorry, I couldn't find a rock band that matches your mood.")  # only reached if for-loop isn't broken, which only happenss if no match is found.

    # Suggest a random rock band if no match found
    random_band = choice(rock_bands)
    print(f"How about trying {random_band[0]}? They are known for {', '.join(random_band[1:])}.")

    # End of the script
    print("Enjoy your music!")


# CONTRIBUTOR NOTES:
# * You had the same for-loop (finding rock band based on mood) twice with different implementations (one of them was better yet broken).
# * I fixed some more stuff and made it actually find a rock band based on mood.
# * You're gonna have to map some moods to some rock types yourself.