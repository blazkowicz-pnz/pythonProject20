from dao.genre import GenreDAO
from service.genre import GenreService
from dao.model.genre import Genre

from unittest.mock import MagicMock
import os
import pytest

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="genre1")
    genre_2 = Genre(id=2, name="genre2")
    genre_3 = Genre(id=3, name="genre3")

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_t = {
            "name": "genre4"
        }
        genre = self.genre_service.create(genre_t)
        assert genre.id is not None

    def test_update(self):
        genre_t = {
            "id": 4,
            "name": "genre5"
        }
        self.genre_service.update(genre_t)

    def test_delete(self):
        self.genre_service.delete(1)


if __name__ == "__main__":
    os.system("pytest")
