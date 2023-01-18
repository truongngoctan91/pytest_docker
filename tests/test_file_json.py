import pytest
from scripts import json_processor


@pytest.fixture()
def file_json_location():
    return "tests/resources/sample2.json"


@pytest.fixture()
def get_data_file_json(file_json_location):
    return json_processor.json_reader(file_json_location)


def test_data_json(get_data_file_json):
    assert (get_data_file_json["firstName"] == "Joe")
    assert (get_data_file_json["lastName"] == "Jackson")
