import os
import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from service.movie import MovieService
from dao.movie import MovieDAO


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_1 = Movie(id=1, title="film1", description="description_1", trailer="trailer_1", year=1900, rating=1.1, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="film2", description="description_2", trailer="trailer_2", year=1901, rating=1.2, genre_id=1, director_id=1)
    movie_3 = Movie(id=3, title="film3", description="description_3", trailer="trailer_3", year=1902, rating=1.3, genre_id=1, director_id=1)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_any = {"title": "film1",
                     "description": "description_1",
                     "trailer": "trailer_1",
                     "year": 1900,
                     "rating": 1.1
                     }
        movie = self.movie_service.create(movie_any)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def update(self):
        movie_new = {"title": "film1",
                     "description": "description_1",
                     "trailer": "trailer_1",
                     "year": 1900,
                     "rating": 1.1
                     }
        self.movie_service.update(movie_new)


if __name__ == "__main__":
    os.system("pytest")
