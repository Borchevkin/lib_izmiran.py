import pytest
from izmiran.datfile import *

def test_int_datfile_open_read_file():
    datfile = DatFile()

    datfile.read("./examples/ep_109705_25.dat")
    assert 4 == datfile.get_columns_count(), "Invalid count of columns"
    
    datfile.set_columns_names(["c1", "c2", "c3", "c4"])
    assert ["c1", "c2", "c3", "c4"] == datfile.get_columns_names(), "Invalid names of columns"

    assert 185 == datfile.get_records_count(), "Invalid count of records"

    records = datfile.get_records()

    assert 185 == len(records), "Wrong count of records"

    record_42 = datfile.get_record(42)
    assert records[42] == record_42, "Records doesn't equal"

def test_int_datfile_create_new_write_read_wo_headers():
    datfile_write = DatFile()

    test_records = [
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"]
    ]

    for record in test_records:
        datfile_write.add_record(record)

    datfile_write.write("test_output.dat")

    datfile_read = DatFile()
    datfile_read.read("test_output.dat")

    assert test_records == datfile_read.get_records(), "Records in two files not equal"

def test_int_datfile_create_new_write_read_with_headers():
    datfile_write = DatFile()

    test_records = [
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"],
        ["0.0", "1.0", "2.0", "3.0" ,"4.0"]
    ]

    for record in test_records:
        datfile_write.add_record(record)

    datfile_write.set_columns_names(["c1", "c2", "c3", "c4", "c5"])
    datfile_write.write("test_output.dat", is_include_header=True)

    datfile_read = DatFile()
    datfile_read.read("test_output.dat", has_header=True)

    assert test_records == datfile_read.get_records(), "Records in two files not equal"
    assert datfile_write.get_columns_names() == datfile_read.get_columns_names(), "Columns names in two files not equal"

def test_int_datfile_avg_happy_flow_simple():
    datfile_main = DatFile()

    test_records = [
        ["1.0", "2.0", "3.0"],
        ["1.0", "2.0", "3.0"],
        ["1.0", "2.0", "3.0"],
        ["2.0", "3.0", "4.0"],
        ["2.0", "3.0", "4.0"],
        ["2.0", "3.0", "4.0"],
        ["3.0", "4.0", "5.0"],
        ["3.0", "4.0", "5.0"],
        ["3.0", "4.0", "5.0"],
        ["4.0", "5.0", "6.0"],
        ["4.0", "5.0", "6.0"],
        ["4.0", "5.0", "6.0"]
    ]

    for record in test_records:
        datfile_main.add_record(record)

    datfile_avg = datfile_main.avg(3)

    avg_test_records = [
        ["1.0", "2.0", "3.0"],
        ["2.0", "3.0", "4.0"],
        ["3.0", "4.0", "5.0"],
        ["4.0", "5.0", "6.0"]
    ]

    assert avg_test_records == datfile_avg.get_records()

def test_int_datfile_avg_happy_flow_avg_calc():
    datfile_main = DatFile()

    test_records = [
        ["1.0", "2.0", "3.0"],
        ["2.0", "2.0", "3.0"],
        ["3.0", "2.0", "3.0"],
        ["2.0", "3.0", "4.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "3.0", "4.0"],
        ["3.0", "4.0", "5.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "4.0", "5.0"],
        ["4.0", "5.0", "6.0"],
        ["5.0", "5.0", "6.0"],
        ["6.0", "5.0", "6.0"]
    ]

    for record in test_records:
        datfile_main.add_record(record)

    datfile_avg = datfile_main.avg(3)

    avg_test_records = [
        ["2.0", "2.0", "3.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "5.0", "6.0"]
    ]

    assert avg_test_records == datfile_avg.get_records()

def test_int_datfile_avg_leftover_records():
    datfile_main = DatFile()

    test_records = [
        ["1.0", "2.0", "3.0"],
        ["2.0", "2.0", "3.0"],
        ["3.0", "2.0", "3.0"],
        ["2.0", "3.0", "4.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "3.0", "4.0"],
        ["3.0", "4.0", "5.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "4.0", "5.0"],
        ["4.0", "5.0", "6.0"],
        ["5.0", "5.0", "6.0"],
        ["6.0", "5.0", "6.0"],
        ["42.0", "42.0", "42.0"],
        ["42.0", "42.0", "42.0"],
    ]

    for record in test_records:
        datfile_main.add_record(record)

    datfile_avg = datfile_main.avg(3)

    avg_test_records = [
        ["2.0", "2.0", "3.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "5.0", "6.0"]
    ]

    assert avg_test_records == datfile_avg.get_records()

def test_int_datfile_avg_start_end():
    datfile_main = DatFile()

    test_records = [
        ["1.0", "2.0", "3.0"],
        ["2.0", "2.0", "3.0"],
        ["3.0", "2.0", "3.0"],
        ["2.0", "3.0", "4.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "3.0", "4.0"],
        ["3.0", "4.0", "5.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "4.0", "5.0"],
        ["4.0", "5.0", "6.0"],
        ["5.0", "5.0", "6.0"],
        ["6.0", "5.0", "6.0"],
        ["42.0", "42.0", "42.0"],
        ["42.0", "42.0", "42.0"],
        ["42.0", "42.0", "42.0"]
    ]

    for record in test_records:
        datfile_main.add_record(record)

    datfile_avg = datfile_main.avg(3, start_idx=0, end_idx=14)

    avg_test_records = [
        ["2.0", "2.0", "3.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "5.0", "6.0"]
    ]

    assert avg_test_records == datfile_avg.get_records()

def test_int_datfile_avg_start_not_0():
    datfile_main = DatFile()

    test_records = [
        ["1.0", "2.0", "3.0"],
        ["2.0", "2.0", "3.0"],
        ["3.0", "2.0", "3.0"],
        ["2.0", "3.0", "4.0"],
        ["3.0", "3.0", "4.0"],
        ["4.0", "3.0", "4.0"],
        ["3.0", "4.0", "5.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "4.0", "5.0"],
        ["4.0", "5.0", "6.0"],
        ["5.0", "5.0", "6.0"],
        ["6.0", "5.0", "6.0"],
        ["42.0", "42.0", "42.0"],
        ["42.0", "42.0", "42.0"],
        ["42.0", "42.0", "42.0"]
    ]

    for record in test_records:
        datfile_main.add_record(record)

    datfile_avg = datfile_main.avg(3, start_idx=3)

    avg_test_records = [
        ["3.0", "3.0", "4.0"],
        ["4.0", "4.0", "5.0"],
        ["5.0", "5.0", "6.0"],
        ["42.0", "42.0", "42.0"]
    ]

    assert avg_test_records == datfile_avg.get_records()