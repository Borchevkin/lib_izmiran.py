import pytest
from datfile import *

def test_unit_parse_line():
    result = DatFile.parse_record_from_line("0\t1\t2")
    assert ["0","1","2"] == result, "Parsing failed"

def test_unit_parse_value():
    result = DatFile.parse_string_val_to_float("1")
    assert 1.0 == result, "Parsing failed"

def test_add_records():
    datfile = DatFile()
    datfile.add_record(["0","1","2"])
    assert True, "Adding records failed"

def test_get_columns_count():
    '''
    Get columns count.
    '''
    datfile = DatFile()
    ret = datfile.get_columns_count()
    assert 0 == ret, "Wrong columns count returned"
    
    datfile.add_record(["0","1","2"])
    ret = datfile.get_columns_count()
    assert 3 == ret, "Wrong columns count returned"

def test_get_columns_name():
    assert False, "FInish it"

def test_get_record_count():
    datfile = DatFile()
    ret = datfile.get_records_count()
    assert 0 == ret, "Wrong records count returned"

    datfile.add_record(["0","1","2"])
    ret = datfile.get_records_count()
    assert 1 == ret, "Wrong records count returned"

    datfile.add_record(["0","1","2"])
    ret = datfile.get_records_count()
    assert 2 == ret, "Wrong records count returned"

    datfile.add_record(["0","1","2"])
    ret = datfile.get_records_count()
    assert 3 == ret, "Wrong records count returned"
