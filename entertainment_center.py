import media
import fresh_tomatoes
movie1 = media.Movie("Despicable Me 3", "http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx", "https://www.youtube.com/watch?v=MxL66M8cj50")
movie2 = media.Movie("Spider-Man: Homecoming", "http://t0.gstatic.com/images?q=tbn:ANd9GcT8W3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t", "https://www.youtube.com/watch?v=NbLP_SmhtuM");
movie3 = media.Movie("Wonder Woman", "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H", "https://www.youtube.com/watch?v=F0lZgaz0CIE");

movies = [movie1, movie2, movie3];
fresh_tomatoes.open_movies_page(movies)
