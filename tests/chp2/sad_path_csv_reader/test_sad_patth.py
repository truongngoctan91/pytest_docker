from scripts import data_processor
import pytest


@pytest.fixture(scope="module")
def get_location_clean_data():
    return 'tests/resources/cities/malformed_map.csv'


def test_get_data(get_location_clean_data):

    with pytest.raises(Exception) as exp:
        data_processor.csv_reader(get_location_clean_data)
    assert (str(exp.value) == "could not convert string to float: 'not_an_altitude'")
