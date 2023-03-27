from src.pre_built.counter import count_ocurrences


def test_counter():
    dois_gremio = count_ocurrences('tests/counter/mock.csv', 'Gremio')
    assert dois_gremio == 2
