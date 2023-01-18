from scripts import data_processor
import pytest


@pytest.fixture(scope="module")
def get_location_clean_data():
    return 'tests/resources/cities/clean_map.csv'


def get_data(get_location_clean_data):
    data = data_processor.csv_reader(get_location_clean_data)
    assert (type(data[0]['Country']) == str)
    assert (type(data[0]['City']) == str)
    assert (type(data[0]['State_Or_Province']) == str)
    assert (type(data[0]['Lat']) == float)
    assert (type(data[0]['Long']) == float)
    assert (type(data[0]['Altitude']) == float)
