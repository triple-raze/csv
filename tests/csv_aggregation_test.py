import pytest
import csv
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))    # sps python

from libs.core import csv_aggregate

@pytest.fixture
def data():
    with open('example.csv', 'r') as f:
        return list(csv.DictReader(f))


def test_csv_aggregate(data):
    min_price = csv_aggregate(data, 'price=min')
    max_rating = csv_aggregate(data, 'rating=max')
    avg_price = csv_aggregate(data, 'price=avg')
    min_rating = csv_aggregate(data, 'rating=min')
    max_price = csv_aggregate(data, 'price=max')
    
    assert min_price == 149
    assert max_rating == 4.9
    assert avg_price == 602.0
    assert min_rating == 4.1
    assert max_price == 1199