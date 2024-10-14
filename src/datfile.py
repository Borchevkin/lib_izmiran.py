class DatFileError(Exception):
    pass

class RecordIndexError(DatFileError):
    pass

class NoColumnsNameError(DatFileError):
    pass

class NoDataInObjectError(DatFileError):
    pass

class NoColumnError(DatFileError):
    pass

class InvalidColumnError(DatFileError):
    pass


class DatFile(object):
    """
    Class for represent *.dat files
    """

    def __init__(self) -> None:
        '''
        DatFile constructor
        '''
        self.columns_names = []
        self.data_list_of_records = []

    def __del__(self) -> None:
        '''
        DatFile deconstruction
        '''
        pass # TODO

    @staticmethod
    def parse_record_from_line(line: str, reject_columns: list=[]) -> list:
        '''
        Parse record from line.
        '''
        line_list = []

        for idx, val in enumerate(line.split('\t')):
            if idx not in reject_columns:
                line_list.append(val.replace("\n", ""))
        
        return line_list
    
    @staticmethod
    def parse_string_val_to_float(val: str) -> float:
        '''
        Convert string value to float falue
        '''
        return float(val)

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
                column_names = DatFile.parse_record_from_line(line, reject_columns)
                self.set_columns_names(column_names)

            line_list = DatFile.parse_record_from_line(line, reject_columns)
            self.data_list_of_records.append(line_list)

    def get_columns_count(self) -> int:
        '''
        Get columns count.
        '''
        if len(self.data_list_of_records) == 0:
            return 0
        
        return len(self.data_list_of_records[0])

    def get_columns_names(self) -> list:
        '''
        Get columns names.
        '''
        if len(self.columns_names) == 0:
            raise NoColumnsNameError("No columns names")
        return self.columns_names.copy()

    def set_columns_names(self, names: list) -> None:
        '''
        Set column names.
        '''
        if self.get_columns_count() != len(names):
            raise InvalidColumnError("Invalid column count")

        self.columns_names = names.copy()

    def get_records_count(self) -> int:
        '''
        Get records count.
        '''
        return len(self.data_list_of_records)

    def get_records(self) -> list:
        '''
        Get all records.
        '''
        return self.data_list_of_records

    def get_record(self, index: int) -> list:
        '''
        Get record by index.
        '''
        if index >= len(self.data_list_of_records):
            raise RecordIndexError("Index out of range")
        
        return self.data_list_of_records[index].copy()
    
    def add_record(self, record: list) -> None:
        if self.get_columns_count() == 0:
            pass
        else:
            if len(record) != self.get_columns_count():
                raise InvalidColumnError("Invalid column count")
        
        self.data_list_of_records.append(record.copy())


