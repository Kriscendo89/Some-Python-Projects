from random import choice, shuffle

#create a list of rock bands
rock_bands = [['Led Zeppelin', 'rock', 'classic rock', 'happy'],
              ['Pink Floyd', 'rock', 'progressive rock', 'emotional', 'sad'],
              ['The Beatles', 'rock', 'Psychedelic rock', 'happy'],
              ['Nirvana', 'rock', 'grunge', 'sad', 'angry'],
              ['slayer', 'rock', 'thrash metal', 'angry', 'energetic'],
              ['Motorhead', 'rock', 'heavy metal', 'energetic', 'happy'],
              ['Soundgarden', 'rock', 'grunge', 'sad', 'emotional'],
              ['Radiohead', 'rock', 'alternative rock', 'sad', 'emotional'],
              ['The Cranberries', 'rock', 'alternative rock', 'sad', 'emotional'],
              ['Ramones', 'rock', 'punk rock', 'energetic', 'happy'],
              ['Foo Fighters', 'rock', 'alternative rock', 'energetic'],
              ['Frank Zappa and The Mothers of Invention', 'rock', 'experimental rock', 'happy'],
              ['Steely Dan', 'rock', 'jazz rock', 'relaxed'],
              ['Queen', 'rock', 'classic rock', 'happy'],
              ['Jeff Beck', 'rock', 'blues rock', 'relaxed', 'emotional'],
              ['The Who', 'rock', 'classic rock', 'energetic', 'happy'],
              ['Dead Kennedys', 'rock', 'punk rock', 'angry', 'energetic'],
              ['Deep Purple', 'rock', 'Classic rock', 'energetic'],
              ['sex pistols', 'rock', 'punk rock', 'angry'],
              ['The Clash', 'rock', 'punk rock', 'energetic'],
              ['Van Halen', 'rock', 'Classic rock', 'energetic', 'happy'],
              ['The Doors', 'rock', 'psychedelic rock', 'relaxed', 'emotional'],
              ['AC/DC', 'rock', 'hard rock', 'energetic'],
              ['Guns N\' Roses', 'rock', 'hard rock', 'energetic'],
              ['Alice in Chains', 'rock', 'grunge', 'sad', 'emotional'],
              ['Pearl Jam', 'rock', 'grunge', 'emotional'],
              ['Black Sabbath', 'rock', 'heavy metal', 'energetic', 'angry'],
              ['Jimi Hendrix Experience', 'rock', 'psychedelic rock', 'happy'],
              ['The Smiths', 'rock', 'alternative rock', 'sad', 'emotional'],
              ['The Misfits', 'rock', 'horror punk', 'angry', 'energetic'],
              ['The Stooges', 'rock', 'proto-punk', 'energetic'],
              ['The Velvet Underground', 'rock', 'art rock', 'emotional', 'relaxed'],
              ['Joy Division', 'rock', 'post-punk', 'sad', 'emotional'],
              ['The Cure', 'rock', 'gothic rock', 'sad', 'emotional'],
              ['R.E.M.', 'rock', 'alternative rock', 'happy', 'relaxed'],
              ['The White Stripes', 'rock', 'garage rock', 'energetic', 'happy'],
              ['Arctic Monkeys', 'rock', 'indie rock', 'energetic', 'happy'],
              ['Paramore', 'rock', 'pop punk', 'energetic', 'happy'],
              ['Linkin Park', 'rock', 'nu metal', 'energetic', 'angry', 'emotional'],
              ['System of a Down', 'rock', 'alternative metal', 'energetic', 'angry'],
              ['Metallica', 'rock', 'thrash metal', 'energetic', 'angry'],
              ['Anthrax', 'rock', 'thrash metal', 'energetic', 'angry'],
              ['Megadeth', 'rock', 'thrash metal', 'energetic', 'angry'],
              ['Slipknot', 'rock', 'nu metal', 'energetic', 'angry'],
              ['Limp Bizkit', 'rock', 'nu metal', 'energetic', 'angry'],
              ['Morbid Angel', 'rock', 'death metal', 'angry', 'energetic'],
              ['Death', 'rock', 'death metal', 'angry', 'energetic'],
              ['Cannibal Corpse', 'rock', 'death metal', 'angry', 'energetic'],
              ['Korn', 'rock', 'nu metal', 'energetic', 'angry'],
              ['Dying Fetus', 'rock', 'death metal', 'angry', 'energetic'],
              ['Suffocation', 'rock', 'death metal', 'angry', 'energetic'],
              ['Opeth', 'rock', 'progressive metal', 'energetic', 'emotional'],
              ['Tool', 'rock', 'progressive metal', 'energetic', 'emotional'],
              ['Sepultura', 'rock', 'groove metal', 'energetic', 'angry'],
              ['Pantera', 'rock', 'groove metal', 'energetic', 'angry'],
              ['Carcass', 'rock', 'Melodic death metal', 'energetic', 'angry'],
              ['At The Gates', 'rock', 'Melodic death metal', 'energetic', 'angry'],
              ['In Flames', 'rock', 'Melodic death metal', 'energetic', 'angry'],
              ['Kiss', 'rock', 'classic rock', 'glam rock', 'energetic', 'happy'],
              ['Aerosmith', 'rock', 'classic rock', 'energetic', 'happy'],
              ['Def Leppard', 'rock', 'classic rock', 'happy'],
              ['Bon Jovi', 'rock', 'classic rock', 'happy'],
              ['Scorpions', 'rock', 'hard rock', 'classic rock', 'energetic', 'happy'],
              ['Journey', 'rock', 'classic rock', 'happy'],
              ['Boston', 'rock', 'classic rock', 'happy'],
              ['Styx', 'rock', 'classic rock', 'happy'],
              ['Foreigner', 'rock', 'classic rock', 'happy'],
              ['Cheap Trick', 'rock', 'power pop', 'classic rock', 'happy'],
              ['Heart', 'rock', 'classic rock', 'happy'],
              ['Fleetwood Mac', 'rock', 'soft rock', 'happy'],
              ['Eagles', 'rock', 'soft rock', 'happy', 'relaxed'],
              ['Lynyrd Skynyrd', 'rock', 'southern rock', 'happy'],
              ['The Allman Brothers Band', 'rock', 'southern rock', 'happy'],
              ['Bob Seger', 'rock', 'classic rock', 'happy'],
              ['Creedence Clearwater Revival', 'rock', 'swamp rock', 'happy', 'relaxed'],
              ['Ozzy Osbourne', 'rock', 'heavy metal', 'energetic'],
              ['My Chemical Romance', 'rock', 'emo', 'sad', 'emotional', 'angry'],
              ['Blink-182', 'rock', 'pop punk', 'energetic', 'happy'],
              ['Green Day', 'rock', 'punk rock', 'energetic', 'happy'],
              ['Nine Inch Nails', 'rock', 'industrial rock', 'emotional', 'energetic'],
              ['Rage Against the Machine', 'rock', 'nu metal', 'energetic', 'angry'],
              ['Motley Crue', 'rock', 'glam metal', 'energetic', 'happy'],
              ['Rammstein', 'rock', 'industrial metal', 'energetic', 'angry'],
              ['Type O Negative', 'rock', 'gothic metal', 'sad', 'emotional'],
              ['Napalm Death', 'rock', 'grindcore', 'angry', 'energetic'],
              ['S.O.D.', 'rock', 'grindcore', 'angry', 'energetic'],
              ['Brutal Truth', 'rock', 'grindcore', 'angry', 'energetic'],
              ['Repulsion', 'rock', 'grindcore', 'angry', 'energetic'],
              ['Fall Out Boy', 'rock', 'pop punk', 'energetic', 'happy'],
              ['Taking Back Sunday', 'rock', 'emo', 'sad', 'emotional'],
              ['Between the Buried and Me', 'rock', 'progressive metal', 'mathcore', 'energetic'],
              ['The Dillinger Escape Plan', 'rock', 'mathcore', 'energetic', 'angry'],
              ['Norma Jean', 'rock', 'metalcore', 'emotional', 'angry'],
              ['Coal Chamber', 'rock', 'nu metal', 'energetic', 'angry'],
              ['Coalesce', 'rock', 'mathcore', 'energetic', 'angry'],
              ['The Number Twelve Looks Like You', 'rock', 'mathcore', 'energetic', 'happy', 'angry'],
              ['Heavy Heavy Low Low', 'rock', 'mathcore', 'energetic', 'angry', 'happy'],
              ['Car Bomb', 'rock', 'mathcore', 'energetic', 'angry'],
              ['Converge', 'rock', 'metalcore', 'energetic', 'angry'],
              ['motionless in White', 'rock', 'metalcore', 'emotional', 'angry'],
              ['Killswitch Engage', 'rock', 'metalcore', 'emotional', 'angry'],
              ['Rotten Sound', 'rock', 'grindcore', 'angry', 'energetic'],
              ['Pig Destroyer', 'rock', 'grindcore', 'angry', 'energetic'],
              ['Agoraphobic Nosebleed', 'rock', 'grindcore', 'angry', 'energetic'],
              ['Cattle Decapitation', 'rock', 'deathgrind', 'angry', 'energetic'],
              ['Misery Index', 'rock', 'deathgrind', 'angry', 'energetic'],
              ['Aborted', 'rock', 'deathgrind', 'angry', 'energetic'],
              ['Black Flag', 'rock', 'hardcore punk', 'energetic', 'angry'],
              ['Minor Threat', 'rock', 'hardcore punk', 'energetic', 'angry'],
              ['Bad Brains', 'rock', 'hardcore punk', 'energetic', 'angry'],
              ['Living Colour', 'rock', 'hardcore punk', 'energetic'],
              ['Refused', 'rock', 'hardcore punk', 'energetic', 'angry'],
              ['Tera Melos', 'rock', 'math rock', 'energetic', 'happy'],
              ['The Mars Volta', 'rock', 'progressive rock', 'energetic', 'emotional'],
              ['Deftones', 'rock', 'alternative metal', 'emotional', 'energetic'],
              ['Faith No More', 'rock', 'alternative metal', 'energetic', 'happy'],
              ['Helmet', 'rock', 'alternative metal', 'energetic', 'angry'],
              ['Jane\'s Addiction', 'rock', 'alternative rock', 'energetic', 'happy'],
              ['Thursday', 'rock', 'post-hardcore', 'emo', 'sad', 'emotional'],
              ['Glassjaw', 'rock', 'post-hardcore', 'emo', 'sad', 'emotional'],
              ['Brand New', 'rock', 'emo', 'sad', 'emotional'],
              ['Taking Back Sunday', 'rock', 'emo', 'sad', 'emotional'],
              ['Dashboard Confessional', 'rock', 'emo', 'sad', 'emotional'],
              ['The Used', 'rock', 'emo', 'sad', 'emotional'],
              ['Folk Implosion', 'rock', 'emo', 'emotional', 'energetic'],
              ['Talking Heads', 'rock', 'new wave', 'happy', 'energetic'],
              ['Sonic Youth', 'rock', 'alternative rock', 'emotional', 'energetic'],
              ['Smashing Pumpkins', 'rock', 'alternative rock', 'emotional', 'energetic'],]

shuffle(rock_bands)

moods = {'happy', 'sad', 'energetic', 'relaxed', 'depressed', 'angry'}

# Input mood
print(f"What is your current mood? (e.g. {', '.join(moods)})")
mood = input("Happy, Sad, Energetic, Relaxed, Depressed, Angry: ").strip().lower()

# Normalize mood input
mood = mood.replace(" ", "")

# Define a function to normalize the mood input
def normalize_mood(mood):
    return mood if mood in moods else None

def map_mood(mood):
    mood_mapping = {
        'happy': ['numetal', 'pop punk', 'soft rock', 'classic rock'],
        'sad': ['soft rock', 'emo', 'post-hardcore'],
        'energetic': ['punk rock', 'thrash metal', 'hard rock', 'grunge', 'alternative rock', 'metalcore', 'nu metal', 'mathcore'],
        'relaxed': ['soft rock', 'jazz rock', 'psychedelic rock'],
        'depressed': ['emo', 'post-hardcore', 'grunge'],
        'angry': ['thrash metal', 'death metal', 'grindcore', 'nu metal', 'hardcore punk', 'mathcore', 'metalcore'],
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