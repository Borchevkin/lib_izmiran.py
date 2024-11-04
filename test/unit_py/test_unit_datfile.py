import pytest
from izmiran.datfile import *

def test_unit_parse_record_from_line_happy_flow():
    result = DatFile.parse_record_from_line("0\t1\t2")
    assert ["0","1","2"] == result, "Parsing failed"

def test_unit_record_to_float_happy_flow():
    record = ["0.5","1.2","2.2"]
    result = DatFile.record_to_float(record)
    assert [0.5,1.2,2.2] == result, "To float conversion failed"

def test_unit_record_to_str_happy_flow():
    record = [0.5,1.2,2.2]
    result = DatFile.record_to_str(record)
    assert ["0.5","1.2","2.2"] == result, "Conversion to string is failed"

def test_unit_line_from_record_happy_flow():
    record = ["0.5","1.2","2.2"]
    result = DatFile.build_line_from_record(record)
    assert "0.5\t1.2\t2.2\n" == result, "Wrong build string" 

def test_calc_avg_for_records_happy_flow():
    records = [
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"]
    ]

    result = DatFile.calc_avg_for_records(records)
    assert ["1.0", "2.0", "3.0", "4.0"] == result, "Wrong avg calculation"

    records = [
        ["0", "1", "2", "3"],
        ["1", "2", "3", "4"],
        ["2", "3", "4", "5"],
    ]

    result = DatFile.calc_avg_for_records(records)
    assert ["1.0", "2.0", "3.0", "4.0"] == result, "Wrong avg calculation"

def test_unit_get_columns_count():
    datfile = DatFile()
    ret = datfile.get_columns_count()
    assert 0 == ret, "Wrong columns count returned"
    
    datfile.add_record(["0","1","2"])
    ret = datfile.get_columns_count()
    assert 3 == ret, "Wrong columns count returned"

def test_unit_get_set_columns_names():
    datfile = DatFile()

    with pytest.raises(NoColumnsNameError, match="No columns names"):
        _ = datfile.get_columns_names()
        assert False, "No appropriate exception was raised for absent names"

    datfile.add_record([1, 2, 3])
    datfile.set_columns_names(["p1", "p2", "p3"])

    assert ["p1", "p2", "p3"] == datfile.get_columns_names(), "Wrong column names"

def test_unit_get_records_count():
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

def test_unit_get_records():
    datfile = DatFile()

    test_records = [
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"]
    ]

    for record in test_records:
        datfile.add_record(record)

    assert test_records == datfile.get_records(), "Added and saved records are not equal"

def test_unit_get_record():
    datfile = DatFile()

    test_records = [[
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["2.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["3.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["4.0", "1.0", "2.0", "3.0" ,"4.0"]
    ]]

    for record in test_records:
        datfile.add_record(record)
    
    for idx, record in enumerate(test_records):
        assert test_records[idx] == datfile.get_record(idx), "Wrong order or value of record"

def test_unit_add_record():
    datfile = DatFile()
    datfile.add_record(["0","1","2"])
    
    assert 1 == datfile.get_records_count(), "Invalid records count after adding one record"
    assert ["0","1","2"] == datfile.get_record(0), "Wrong record value" 
