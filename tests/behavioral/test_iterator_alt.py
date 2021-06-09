import pytest

from patterns.behavioral.iterator_alt import NumberWords


@pytest.fixture(scope="function")
def num_words(request):
    start, stop = request.param

    return NumberWords(start=start, stop=stop)


@pytest.mark.parametrize(
    "num_words", [
        (1,2),
        (1,5)
    ],
    indirect=["num_words"]
)
def test_raises_stop_iteration(num_words):
    with pytest.raises(StopIteration) as exc_info:
        while True:
            next(num_words)

        assert exc_info.type is StopIteration
