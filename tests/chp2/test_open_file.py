# from scripts import data_processor
# import pytest


# @pytest.fixture(scope="function")
# def get_location_clean_data():
#     return 'tests/resources/cities/malformed_map11.csv'


# def test_open_file(get_location_clean_data):
#     with pytest.raises(FileExistsError) as exp:
#         data = data_processor.csv_reader(get_location_clean_data)
#     assert (str(exp.value) == "something wrong")
