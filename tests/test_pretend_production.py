import PretendProduction2
import pytest


def test_simple_distance():
    distance = PretendProduction2.simple_distance(3, 0, 6, 4)
    assert distance == 5
    assert PretendProduction2.simple_distance(0, 0, 6, 5) == pytest.approx(7.81024967590, .000001)


def test_add_interest():
    total = PretendProduction2.add_interest(1000, .1)
    assert total == 1100
    with pytest.raises(TypeError):
        PretendProduction2.add_interest("1000", .1)


def test_show_output():
    with open("output.txt", 'w') as output_file:
        PretendProduction2.testable_show_output(1000, .1, output_file)

    file = open("output.txt")
    line = file.readline()
    assert line.find("1100") > -1
