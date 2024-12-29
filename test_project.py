import pytest
from project import (
    len_convert,
    mass_convert,
    vol_convert,
    temp_convert,
    area_convert,
    speed_convert,
    time_convert,
    energy_convert,
    power_convert,
    currency_convert,
)


def test_len_convert():
    assert len_convert(1)[0] == ("cm to in", 0.393701)
    assert len_convert(1)[1] == ("in to cm", 2.54)
    assert len_convert(0)[0] == ("cm to in", 0.0)
    assert len_convert(-1)[0] == ("cm to in", -0.393701)


def test_mass_convert():
    assert mass_convert(1)[0] == ("kg to lb", 2.20462)
    assert mass_convert(1)[1] == ("lb to kg", pytest.approx(0.453592, 0.0001))
    assert mass_convert(0)[0] == ("kg to lb", 0.0)
    assert mass_convert(-1)[0] == ("kg to lb", -2.20462)


def test_vol_convert():
    assert vol_convert(1)[0] == ("L to gal", 0.264172)
    assert vol_convert(1)[1] == ("gal to L", pytest.approx(3.78541, 0.0001))
    assert vol_convert(0)[0] == ("L to gal", 0.0)
    assert vol_convert(-1)[0] == ("L to gal", -0.264172)


def test_temp_convert():
    assert temp_convert(0)[0] == ("\u00b0C to \u00b0F", 32.0)
    assert temp_convert(32)[1] == ("\u00b0F to \u00b0C", 0.0)
    assert temp_convert(-40)[0] == ("\u00b0C to \u00b0F", -40.0)  # Edge case: -40 is the same in °C and °F


def test_area_convert():
    assert area_convert(1)[0] == ("m\u00b2 to ft\u00b2", 10.7639)
    assert area_convert(1)[1] == ("ft\u00b2 to m\u00b2", pytest.approx(0.092903, 0.0001))
    assert area_convert(0)[0] == ("m\u00b2 to ft\u00b2", 0.0)
    assert area_convert(-1)[0] == ("m\u00b2 to ft\u00b2", -10.7639)


def test_speed_convert():
    assert speed_convert(1)[0] == ("mph to km/h", 1.60934)
    assert speed_convert(1)[1] == ("km/h to mph", pytest.approx(0.621371, 0.0001))
    assert speed_convert(0)[0] == ("mph to km/h", 0.0)
    assert speed_convert(-1)[0] == ("mph to km/h", -1.60934)


def test_time_convert():
    assert time_convert(60)[0] == ("s to min", 1.0)
    assert time_convert(120)[3] == ("min to h", 2)
    assert time_convert(0)[0] == ("s to min", 0.0)
    assert time_convert(-60)[0] == ("s to min", -1.0)


def test_energy_convert():
    assert energy_convert(1)[0] == ("J to cal", 0.239006)
    assert energy_convert(1)[1] == ("cal to J", pytest.approx(4.184, 0.0001))
    assert energy_convert(0)[0] == ("J to cal", 0.0)
    assert energy_convert(-1)[0] == ("J to cal", -0.239006)


def test_power_convert():
    assert power_convert(1)[0] == ("W to hp", pytest.approx(0.00134102, 0.0001))
    assert power_convert(1)[1] == ("hp to W", pytest.approx(745.7, 0.0001))
    assert power_convert(0)[0] == ("W to hp", 0.0)
    assert power_convert(-1)[0] == ("W to hp", pytest.approx(-0.00134102, 0.0001))


def test_currency_convert():
    assert currency_convert(1)[0] == ("USD to EUR", 0.92)
    assert currency_convert(1)[1] == ("EUR to USD", pytest.approx(1.087, 0.001))
    assert currency_convert(0)[0] == ("USD to EUR", 0.0)
    assert currency_convert(-1)[0] == ("USD to EUR", -0.92)