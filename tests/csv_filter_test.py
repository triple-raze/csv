import csv
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))    # sps python

from libs.core import csv_aggregate, csv_filter

@pytest.fixture
def data():
    with open('example.csv', 'r') as f:
        return list(csv.DictReader(f))

def test_csv_filter(data):
    apple_data = csv_filter(data, 'brand=apple')
    high_rating_data = csv_filter(data, 'rating>4.5')
    cheap_data = csv_filter(data, 'price<500')
    
    assert len(apple_data) == 4
    assert len(high_rating_data) == 5
    assert len(cheap_data) == 5
    assert all(row['brand'] == 'apple' for row in apple_data)
    assert all(float(row['rating']) > 4.5 for row in high_rating_data)
    assert all(int(row['price']) < 500 for row in cheap_data)

