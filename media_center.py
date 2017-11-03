from media import Movie
import fresh_tomatoes

piper = Movie(
    'Piper',
    'Bird vs ocean',
    'http://is2.mzstatic.com/image/thumb/Video51/v4/3c/94/22/3c942244-ccb5-08f0-d0e1-1937af8c09cd/source/227x227bb.jpg',
    'https://www.youtube.com/watch?v=72a27aLQ5B8'
    )

cuerdas = Movie(
    'Cartel Cuerdas',
    'Girl vs school',
    'https://www.premiosgoya.com/wp-content/uploads/2015/12/cartel_cuerdas_low-320x457.jpg',
    'https://www.youtube.com/watch?v=QUhmfeR9OZc'
)

nubes = Movie(
    'La Nube y la Ciguena',
    'Baby vs weather',
    'https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Partly_Cloudy_poster.jpg/220px-Partly_Cloudy_poster.jpg',
    'https://www.youtube.com/watch?v=yMgW0NRH9zQ'
)

regalo = Movie(
    'El Regalo',
    'Boy vs dog',
    'https://i.ytimg.com/vi/9iFWyihDvCE/hqdefault.jpg',
    'https://www.youtube.com/watch?v=WjqiU5FgsYc'
)

dustin = Movie(
    'Dustin',
    'Dog vs bone',
    'https://i.pinimg.com/564x/c5/c0/d0/c5c0d0ff04680bf1fdfef78cbdb1b468--shorts-movie-film-youtube.jpg',
    'https://www.youtube.com/watch?v=BTSH3hxdk_A'
)

omoleto = Movie(
    'Omoleto',
    'Omlette vs the world',
    'https://i.ytimg.com/vi/oTVTtWq5wHo/hqdefault.jpg',
    'https://www.youtube.com/watch?v=yQkvayPz3iw'
)

movies = [piper, cuerdas, regalo, nubes, dustin, omoleto]

for movie in movies:
    print movie.trailer_youtube_url

fresh_tomatoes.open_movies_page(movies)
