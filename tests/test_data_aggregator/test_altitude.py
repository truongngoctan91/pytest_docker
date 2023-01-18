from scripts import data_aggregator, data_processor
import pytest
from io import StringIO


@pytest.fixture()
def get_file_location():
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture()
def get_data(get_file_location):
    data = data_processor.csv_reader(get_file_location)
    return data


@pytest.mark.parametrize("country,stat,expected", [('Andorra', 'Mean', 1641.42),
                                                   ('Andorra', 'Median', 1538.02),
                                                   ('Argentina', 'Median', 125.0)])
def test_atitude(get_data, country, stat, expected):
    get_atitude_stat = data_aggregator.atitude_stat_per_country(
        get_data, country, stat)
    assert get_atitude_stat == {'Country': country, stat: expected}


@pytest.mark.parametrize("country,stat,expected", [('Andorra', 'Mean', 1641.42),
                                                   ('Andorra', 'Median', 1538.02),
                                                   ('Argentina', 'Median', 125.0)])
def test_csv_writer(get_data, country, stat, expected):
    """
     TO DO: Update the function to be parametrized with 3 scenarios:
     ('Andorra', 'Mean', 1641.42),
     ('Andorra', 'Median', 1538.02),
     ('Argentina', 'Median', 125.0),

    Hint:
    - In the final assertion, you will need to use an f-string to inject the
      arguments into the final string.

    - For example: f'{stat} would inject the string statistic that we use for
      the csv writer.
    """

    output_location = StringIO()
    get_atitude_stat = data_aggregator.atitude_stat_per_country(
        get_data, country, stat)
    data_aggregator.csv_writer(get_atitude_stat, output_location)

    res = output_location.getvalue().strip('\r\n')
    assert res == f'Country,{stat}\r\n{country},{expected}'
