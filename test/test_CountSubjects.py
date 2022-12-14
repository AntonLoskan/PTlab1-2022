from src.Types import DataType
from src.CountSubjects import CountSubjects
import pytest

RatingsType = dict[str, float]


class TestCountSubjects:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 90),
                    ("физика", 76),
                    ("география", 76)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ],

            "Петров Игорь Вячеславович":
                [
                    ("математика", 76),
                    ("русский язык", 12),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 3,
            "Петров Игорь Владимирович": 0,
            "Петров Игорь Вячеславович": 1
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:

        calc_rating = CountSubjects(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:

        rating = CountSubjects(input_data[0]).calc()
        for student in rating:
            rating_score = rating[student]
            assert rating_score == input_data[1][student]
