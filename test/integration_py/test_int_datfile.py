import pytest
from datfile import *

def test_int_open_read_file():
    datfile = DatFile()

    datfile.parse_from("./examples/ep_109705_25.dat")
    assert 4 == datfile.get_columns_count(), "Invalid count of columns"
    
    datfile.set_columns_names(["c1", "c2", "c3", "c4"])
    assert ["c1", "c2", "c3", "c4"] == datfile.get_columns_names(), "Invalid names of columns"

    assert 185 == datfile.get_records_count(), "Invalid count of records"

    records = datfile.get_records()

    assert 185 == len(records), "Wrong count of records"

    record_42 = datfile.get_record(42)
    assert records[42] == record_42