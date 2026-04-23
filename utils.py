from rich.console import Console
from config import FILENAME_P1, FILENAME_MARKS
import json
console = Console()
class Utils:
    def __init__(self) -> None:
        pass
    @staticmethod
    def load_file():
        """load the CSV file """
        with open(FILENAME_P1,"r",newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    @staticmethod
    def show_error(message):
        """Displays all errors """
        console.print(
           f":x: [bold red]{message}[/bold red]"
        )
    @staticmethod
    def show_success(message):
        """Displays all successs messages"""
        console.print(
              f":white_check_mark: [bold green]{message}[/bold green]" 
        )
    @staticmethod
    def load_json(filename=FILENAME_MARKS):
        """Load json file
            param: data, FILENAME_MARKS
            returns data
        """
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        return data
    @staticmethod
    def dump_json(data):
         """
            dumps data in the  json file
            param: data, FILENAME_MARKS
            returns data
        """
        with open(FILENAME_MARKS, 'w') as f:
            json.dump(data,f, indent=4)
            