class DatFileError(Exception):
    pass

class RecordIndexError(DatFileError):
    pass

class NoColumnsNameError(DatFileError):
    pass

class NoDataInObjectError(DatFileError):
    pass

class DatFile(object):
    """
    Class for represent *.dat files
    """

    def __init__(self) -> None:
        self.columns_names = []
        self.data_list_of_records = []
        self.data_list_of_columns = []

    def __del__(self) -> None:
        pass # TODO

    def parse_record_from_line(self, line: str, reject_columns: list=[]) -> list:
        line_list = []

        for idx, val in enumerate(line.split('\t')):
            if idx not in reject_columns:
                line_list.append(val.replace("\n", ""))
        
        return line_list

    def parse_from(self, filepath: str, has_header: bool=False, reject_columns: list=[]) -> None:
        '''
        Parse *.dat file
        '''

        lines = None
        try:
            with open(filepath, "r", encoding='utf-8') as input_file:
                lines = input_file.readlines()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='utf-16') as input_file:
                lines = input_file.readlines()

        for idx, line in enumerate(lines):
            if has_header and idx == 0:
                column_names = self.parse_record_from_line(line, reject_columns)
                self.set_columns_names(column_names)

            line_list = self.parse_record_from_line(line, reject_columns)
            self.data_list_of_records.append(line_list)

    def get_columns_count(self) -> int:
        if len(self.data_list_of_records) == 0:
            raise NoDataInObjectError("No data in object")
        return len(self.data_list_of_records[0])
 

    def get_columns_names(self) -> list:
        if len(self.columns_names) == 0:
            raise NoColumnsNameError("No columns names")
        return self.columns_names.copy()

    def set_columns_names(self, names: list) -> None:
        self.columns_names = names.copy()

    def get_records_count(self) -> int:
        return len(self.data_list_of_records)

    def get_records(self) -> list:
        return self.data_list_of_records

    def get_record(self, index: int) -> list:
        if index >= len(self.data_list_of_records):
            raise RecordIndexError("Index out of range")