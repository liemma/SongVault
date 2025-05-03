from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re

app = Flask(__name__)

# Name : Emma Li

current_id = 11
all_data = { "1": { 
            "id": "1",
            "title": "Fifteen", 
            "artist": "Taylor Swift", 
            "writers": ["Taylor Swift"], 
            "album": "Fearless", 
            "year": "2008", 
            "summary": "Inspired by Swift's high-school freshman year, the lyrics narrate how she and her friend Abigail Anderson, both at 15, experience teenage heartbreak and realize life aspirations.", 
            "genre": ["Country Pop", "Guitar Pop"],
            "duration": "4:55", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/8/8f/Taylor_Swift_-_Fifteen.png",
            "lyrics_link": "https://genius.com/Taylor-swift-fifteen-lyrics", 
            "music_video": "https://youtu.be/Pb-K2tXWK4w?si=7ByTSd0ASxRvVJnO",  
            "similar_song_ids": ["2", "4", "6", "7", "9"]
            },
        "2": { 
            "id": "2",
            "title": "Back to December", 
            "artist": "Taylor Swift", 
            "writers": ["Taylor Swift"], 
            "album": "Speak Now", 
            "year": "2010", 
            "summary": "Inspired by Swift's relationship with the actor Taylor Lautner, the lyrics are about a remorseful plea for forgiveness from a former lover.", 
            "genre": ["Country Pop"],
            "duration": "4:53", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/0/0f/Back_to_December.png",
            "lyrics_link": "https://genius.com/Taylor-swift-back-to-december-taylors-version-lyrics", 
            "music_video": "https://youtu.be/QUwxKWT6m7U?si=Y8lgdocceH1cZ3gb",  
            "similar_song_ids": ["1", "4", "6", "7", "9"]
            },
        "3": { 
            "id": "3",
            "title": "Hey Ya!", 
            "artist": "Outkast", 
            "writers": ["Andre Benjamin"], 
            "album": "Speakerboxxx/The Love Below", 
            "year": "2003", 
            "summary": "A song by American hip hop duo Outkast, performed by its member André 3000, who wrote and produced the song. Along with 'The Way You Move', recorded by Outkast's other member Big Boi, 'Hey Ya!' was released by Arista Records as the second single from the duo's fifth album, Speakerboxxx/The Love Below, on September 9, 2003.", 
            "genre": ["Pop", "Electro", "Funk", "Neo-Soul"],
            "duration": "4:53", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/d/d8/Hey_Ya_single_cover.png",
            "lyrics_link": "https://genius.com/Outkast-hey-ya-lyrics", 
            "music_video": "https://youtu.be/PWgvGjAhvIw?si=QAPYngEZzKi5DAi6",  
            "similar_song_ids": ["5", "8", "10"]
            },
        "4": { 
            "id": "4",
            "title": "Enchanted", 
            "artist": "Taylor Swift", 
            "writers": ["Taylor Swift"], 
            "album": "Speak Now", 
            "year": "2010", 
            "summary": "A song written and recorded by the American singer-songwriter Taylor Swift for her third studio album, Speak Now (2010). Produced by Swift and Nathan Chapman, the song is a power ballad combining pop, rock, and country. The production incorporates gentle acoustic guitars and crescendos after each refrain, leading to dynamic electric guitars, a steady drum beat, and a vocal harmony-layered coda. In the lyrics, a narrator is infatuated with someone after meeting them for the first time, and she worries about whether the initial feeling will be reciprocated.", 
            "genre": ["Country", "Pop", "Rock"],
            "duration": "5:52", 
            "song_cover": "https://img.buzzfeed.com/buzzfeed-static/static/2018-04/16/10/asset/buzzfeed-prod-web-04/sub-buzz-16652-1523887341-1.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
            "lyrics_link": "https://genius.com/Taylor-swift-enchanted-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=igIfiqqVHtA",  
            "similar_song_ids": ["1", "2", "6", "7", "9"]
            },
        "5": { 
            "id": "5",
            "title": "Fast Car", 
            "artist": "Tracy Chapman", 
            "writers": ["Tracy Chapman"], 
            "album": "Tracy Chapman", 
            "year": "1988", 
            "summary": "The debut single by American singer-songwriter Tracy Chapman, released on April 6, 1988, by Elektra Records, as the lead single from her 1988 self-titled debut studio album. Chapman's appearance at the Nelson Mandela 70th Birthday Tribute concert in June 1988 helped the song become a top-ten hit in the United States, reaching number six on the Billboard Hot 100, and led the album to top the Billboard 200. The single also reached number five on the UK Singles Chart.", 
            "genre": ["Folk rock", "Folk pop", "Soft rock"],
            "duration": "4:57", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/3/30/Fastcar_tchapman.jpg",
            "lyrics_link": "https://genius.com/Tracy-chapman-fast-car-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=AIOAlaACuv4",  
            "similar_song_ids": ["3"]
            },
        "6": { 
            "id": "6",
            "title": "Lover", 
            "artist": "Taylor Swift", 
            "writers": ["Taylor Swift"], 
            "album": "Lover", 
            "year": "2019", 
            "summary": "A timeless love song meant for a wedding reception: the lyrics are about an committed romantic relationship, and the bridge draws on the bridal rhyme 'Something old'. Produced by Swift and Jack Antonoff, 'Lover' is a country, indie folk, and rock ballad set to a waltz. Its reverbed production is driven by acoustic guitar and consists of snare drums, piano, and pizzicato strings.", 
            "genre": ["Country", "Indie folk", "Alternative country", "Rock"],
            "duration": "3:41", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/c/cd/Taylor_Swift_-_Lover.png",
            "lyrics_link": "https://genius.com/Taylor-swift-lover-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=-BjZmE2gtdo",  
            "similar_song_ids": ["1", "2", "4", "7", "9"]
            },
        "7": { 
            "id": "7",
            "title": "State of Grace", 
            "artist": "Taylor Swift", 
            "writers": ["Taylor Swift"], 
            "album": "Red", 
            "year": "2012", 
            "summary": "An opening track of 'Red', 'State of Grace' features arena rock production, incorporating chiming guitars and dynamic drums. Its lyrics use anthemic hooks and abstract metaphors to describe the ups and downs of a transformative romance.", 
            "genre": ["Arena rock", "Alternative rock"],
            "duration": "4:55", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/8/8a/Taylor_Swift_-_State_of_Grace.png",
            "lyrics_link": "https://genius.com/Taylor-swift-state-of-grace-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=QQsgJJ_CzBc",  
            "similar_song_ids": ["1", "2", "4", "6", "9"]
            },

        "8": { 
            "id": "8",
            "title": "Here Comes the Sun", 
            "artist": "The Beatles", 
            "writers": ["George Harrison"], 
            "album": "Abbey Road", 
            "year": "1969", 
            "summary": "One of The Beatles' most beloved songs, 'Here Comes the Sun' was written by George Harrison and expresses relief and optimism as winter turns to spring. The song features an uplifting melody with acoustic guitar, Moog synthesizer, and rich harmonies.", 
            "genre": ["Folk rock", "Pop rock"],
            "duration": "3:06", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/4/41/Thebeatles_here_comes_the_sun.jpg",
            "lyrics_link": "https://genius.com/The-beatles-here-comes-the-sun-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=KQetemT1sWc",  
            "similar_song_ids": ["3", "5"]
        },

        "9": { 
            "id": "9",
            "title": "Red", 
            "artist": "Taylor Swift", 
            "writers": ["Taylor Swift"], 
            "album": "Red", 
            "year": "2013", 
            "summary": "The title track from Taylor Swift's fourth studio album, 'Red' describes the intensity of a passionate but tumultuous relationship. The song blends country, pop, and rock elements, featuring driving instrumentation and emotionally charged lyrics.", 
            "genre": ["Country pop", "Rock"],
            "duration": "3:43", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/c/c0/Taylor_Swift_-_Red_%28Single%29.png",
            "lyrics_link": "https://genius.com/Taylor-swift-red-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=Zlot0i3Zykw",  
            "similar_song_ids": ["1", "2", "4", "6", "7"]
        },

        "10": { 
            "id": "10",
            "title": "Dreams", 
            "artist": "Fleetwood Mac", 
            "writers": ["Stevie Nicks"], 
            "album": "Rumours", 
            "year": "1977", 
            "summary": "'Dreams' is Fleetwood Mac's only number-one hit in the US. Written by Stevie Nicks, the song captures the emotional turmoil within the band during the recording of 'Rumours'. It features a soft rock sound with smooth harmonies and a hypnotic rhythm.", 
            "genre": ["Soft rock", "Pop rock"],
            "duration": "4:17", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/b/b9/Fleetwood_Mac_-_Dreams.png",
            "lyrics_link": "https://genius.com/Fleetwood-mac-dreams-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=mrZRURcb1cM",  
            "similar_song_ids": ["8", "5"]
        },
    
        "11": { 
            "id": "11",
            "title": "Happy", 
            "artist": "Pharrell Williams", 
            "writers": ["Pharrell Williams"], 
            "album": "G I R L", 
            "year": "2013", 
            "summary": "'Happy' is an upbeat, feel-good song that became a global hit. Originally written for the 'Despicable Me 2' soundtrack, the song features a soulful, upbeat melody with handclaps and a lively rhythm, embodying a joyful and positive message.", 
            "genre": ["Soul", "Funk", "Pop"],
            "duration": "3:53", 
            "song_cover": "https://upload.wikimedia.org/wikipedia/en/2/23/Pharrell_Williams_-_Happy.jpg",
            "lyrics_link": "https://genius.com/Pharrell-williams-happy-lyrics", 
            "music_video": "https://www.youtube.com/watch?v=y6Sxv-sUYtM",  
            "similar_song_ids": ["8", "10"]
        }


}


# ROUTES

@app.route('/')
def homepage():
   return render_template('homepage.html', data=all_data)   


@app.route('/view/<id>')
def view(id):
    song=all_data[id]
    return render_template('view.html', song=song, data=all_data)


@app.route('/search/<path:query>')
def search(query):
    query = query.strip().lower()  # Trim whitespace and convert to lowercase
    
    if not query:  # Ignore empty queries
        return render_template("search.html", results={}, query="", no_results=True)

    # Search in title, writers, and album (case-insensitive substring match)
    results = {
        id: song for id, song in all_data.items()
        if query in song['title'].lower() or
           any(query in writer.lower() for writer in song.get('writers', [])) or
           query in song.get('album', '').lower()
    }

    no_results = len(results) == 0  # Check if there are no matches

    result_count = len(results)
    return render_template("search.html", results=results, query=query, result_count=result_count, no_results=no_results)


@app.route('/add', methods=['GET'])
def add():
    return render_template("add.html", all_data=all_data)


@app.route('/edit/<id>')
def edit(id):
    song=all_data[id]   # specify the song to edit
    return render_template('edit.html', song=song, all_data=all_data)


# Custom filter to highlight entire words matching the search query
def bold_match(text, query):
    if not text or not query:
        return text  # Return original if empty

    # Use regex to match entire words that contain the query
    regex = re.compile(r'\b\w*' + re.escape(query) + r'\w*\b', re.IGNORECASE)  # \b ensures full word match

    return regex.sub(lambda match: f'<strong class="extra-bold">{match.group()}</strong>', text)  # Wrap full match in <strong>

# Register the Jinja filter
app.jinja_env.filters['bold_match'] = bold_match


# AJAX FUNCTIONS
@app.route('/add_song_ajax', methods=['POST'])
def add_song_ajax():
    global current_id

    if not request.is_json:
        return jsonify(success=False, errors={"general": "Invalid JSON data"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify(success=False, errors={"general": "No JSON data received"}), 400

    print("Received JSON Data:", data)  # Debugging output

    # Error handling
    errors = {}
    if not data.get("title", "").strip():
        errors["title"] = "Title is required."
    if not data.get("artist", "").strip():
        errors["artist"] = "Artist is required."
    if not data.get("writers", "").strip():
        errors["writers"] = "Writers field cannot be empty."
    if not data.get("album", "").strip():
        errors["album"] = "Album field cannot be empty."
    if not data.get("year", "").strip().isdigit():
        errors["year"] = "Year must be a number."
    
    # Ensure duration is in x:xx format
    duration = data.get("duration", "").strip()
    if not re.match(r'^\d+:[0-5][0-9]$', duration):
        errors["duration"] = "Duration must be in x:xx format."


    if not data.get("song_cover", "").strip().startswith("http"):
        errors["song_cover"] = "Song cover must be a valid URL."
    if not data.get("lyrics_link", "").strip().startswith("http"):
        errors["lyrics_link"] = "Lyrics link must be a valid URL."
    if not data.get("music_video", "").strip().startswith("http"):
        errors["music_video"] = "Music video link must be a valid URL."

    if errors:
        return jsonify(success=False, errors=errors)

    # Generate new song ID
    current_id += 1
    new_id = str(current_id)

    similar_songs = data.get("similar_song_ids", [])
    
    # Save new song to the database
    all_data[new_id] = {
        "id": new_id,
        "title": data["title"],
        "artist": data["artist"],
        "writers": data["writers"].split(", "),
        "album": data["album"],
        "year": data["year"],
        "summary": data["summary"],
        "genre": data["genre"].split(", "),
        "duration": data["duration"],
        "song_cover": data["song_cover"],
        "lyrics_link": data["lyrics_link"],
        "music_video": data["music_video"],
        "similar_song_ids": similar_songs
    }

    return jsonify(success=True, id=new_id, message="New item successfully created.")

@app.route('/edit_song_ajax', methods=['POST'])
def edit_song_ajax():
    global current_id
    
    if not request.is_json:
        return jsonify(success=False, errors={"general": "Invalid JSON data"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify(success=False, errors={"general": "No JSON data received"}), 400

    print("Received JSON Data:", data)  # Debugging output

    # Error handling
    errors = {}
    if not data.get("title", "").strip():
        errors["title"] = "Title is required."
    if not data.get("artist", "").strip():
        errors["artist"] = "Artist is required."
    if not data.get("writers", "").strip():
        errors["writers"] = "Writers field cannot be empty."
    if not data.get("album", "").strip():
        errors["album"] = "Album field cannot be empty."
    if not data.get("year", "").strip().isdigit():
        errors["year"] = "Year must be a number."
    # Ensure duration is in x:xx format
    duration = data.get("duration", "").strip()
    if not re.match(r'^\d+:[0-5][0-9]$', duration):
        errors["duration"] = "Duration must be in x:xx format."


    if not data.get("song_cover", "").strip().startswith("http"):
        errors["song_cover"] = "Song cover must be a valid URL."
    if not data.get("lyrics_link", "").strip().startswith("http"):
        errors["lyrics_link"] = "Lyrics link must be a valid URL."
    if not data.get("music_video", "").strip().startswith("http"):
        errors["music_video"] = "Music video link must be a valid URL."

    if errors:
        return jsonify(success=False, errors=errors)

    similar_songs = data.get("similar_song_ids", [])

    song_id = data.get("id")
    all_data[song_id].update({
        "title": data["title"],
        "artist": data["artist"],
        "writers": data["writers"].split(", "),
        "album": data["album"],
        "year": data["year"],
        "summary": data["summary"],
        "genre": data["genre"].split(", "),
        "duration": data["duration"],
        "song_cover": data["song_cover"],
        "lyrics_link": data["lyrics_link"],
        "music_video": data["music_video"],
        "similar_song_ids": similar_songs
    })
    return jsonify(success=True, id=song_id, message="Item successfully updated.")

if __name__ == '__main__':
   app.run(debug = True, port=5001)




