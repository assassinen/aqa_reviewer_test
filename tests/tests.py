import pytest

from code import main


@pytest.mark.parametrize('distance,result', [
    ((), -1),
    ({}, -1),
    ([], -1),
    ('', -1),
    ('500', -1),
    (-500, -1),
    (-0.01, -1),
    (0, -1),
    (0.01, 50),
    (1.99, 50),
    (2, 100),
    (9.99, 100),
    (10, 200),
    (29.99, 200),
    (30, 300),
    (500, 300),
])
def test_get_distance_surcharge(distance, result):
    assert main.get_distance_surcharge(distance) == result


@pytest.mark.parametrize('length, width, height, result', [
    ((), 1, 1, -1),
    (1, {}, 1, -1),
    (1, 1, [], -1),
    (-0.1, 1, 1, -1),
    (1, -0.1, 1, -1),
    (1, 1, -0.1, -1),
    (0, 1, 1, -1),
    (1, 0, 1, -1),
    (1, 1, 0, -1),
    (1.5, 1, 1, -1),
    (1, 1.5, 1, -1),
    (1, 1, 1.5, -1),
    (1, 1, 1, 100),
    (1, 1, 147, 100),
    (1, 147, 1, 100),
    (147, 1, 1, 100),
    (49, 50, 50, 100),
    (50, 49, 50, 100),
    (50, 50, 49, 100),
    (50, 50, 50, 200),
    (1, 1, 148, 200),
    (1, 148, 1, 200),
    (148, 1, 1, 200),
    (500, 500, 500, 200),
])
def test_get_cargo_size_surcharge(length, width, height, result):
    assert main.get_cargo_size_surcharge(length, width, height) == result


@pytest.mark.parametrize('is_fragile, result', [
    (True, 300),
    (False, 0),
    (1, -1),
    (0, -1),
    ('', -1),
    ({}, -1),
    ((), -1),
    ([], -1),
])
def test_get_fragility_of_cargo_surcharge(is_fragile, result):
    assert main.get_fragility_of_cargo_surcharge(is_fragile) == result


@pytest.mark.parametrize('workload, result', [
    ('normal', 1),
    ('high', 1.2),
    ('very_high', 1.4),
    ('extra_high', 1.6),
    ('unknown', 1),
    ('', 1),
    (True, -1),
    ({}, -1),
    ((), -1),
    ([], -1),
])
def test_get_workload_surcharge(workload, result):
    assert main.get_workload_surcharge(workload) == result


@pytest.mark.parametrize('distance,	length,	width, height, is_fragile, workload, result', [
    [2, 50, 50, 50, True, 'very_high', 840],
    [2, 49, 49, 49, False, 'extra_high', 400],
    [2, 50, 50, 50, True, 'normal', 600],
    [2, 49, 49, 49, False, 'high', 400],
    [10, 50, 49, 50, True, 'extra_high', 960],
    [10, 49, 50, 50, False, 'normal', 400],
    [10, 50, 50, 49, True, 'high', 720],
    [10, 50, 49, 50, False, 'very_high', 420],
    [30, 49, 50, 50, True, 'extra_high', 1120],
    [30.01, 50, 50, 50, True, 'extra_high', -1],
    [30, 50, 49, 49, True, 'normal', 700],
    [30, 50, 50, 50, False, 'high', 600],
    [30, 49, 49, 50, True, 'very_high', 980],
    [50, 50, 50, 50, False, 'extra_high', 800],
    [50, 50, 49, 49, True, 'normal', -1],
    [50, 49, 50, 50, True, 'high', -1],
    [50, 50, 50, 49, False, 'very_high', 560],
    [1, 50, 49, 50, False, 'very_high', 400],
    [1, 50, 50, 49, True, 'extra_high', 720],
    [1, 49, 50, 50, False, 'normal', 400],
    [1, 50, 49, 50, True, 'high', 540],
    [1, 49, 50, 49, True, 'very_high', 630],
])
def test_get_delivery_price(distance, length, width, height, is_fragile, workload, result):
    assert main.get_delivery_price(distance, length, width, height, is_fragile, workload) == result
