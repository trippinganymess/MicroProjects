import csv
import os
from config import FILENAME, FILEHEADER
from Input import Input
from exception import *
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()
class Utils:
    def __init__(self) -> None:
        pass
    @staticmethod
    def loadFile():
        with open(FILENAME,"r",newline='') as f:
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
class Commands:
    def __init__(self, input_obj) -> None:
        self.input_obj = input_obj
    def add(self):
        new_data = {
            "CONTACT" : self.input_obj.contact,
            "NAME" : self.input_obj.name,
            "EMAIL" : self.input_obj.Email
        }
        with open(FILENAME, 'a',newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FILEHEADER,)
            writer.writerow(new_data)
        
    @staticmethod     
    def view():
        reader = Utils.loadFile()
        table = Table(title="Contact List", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Contact", style="green")
        table.add_column("Email", style="yellow")
        for row in reader:
            table.add_row(row["NAME"], row["CONTACT"], row["EMAIL"])
        console.print(table)
        
        
    @staticmethod
    def search(searchItem):
        reader = Utils.loadFile()
        contact = [contact for contact in reader if contact['CONTACT'] == searchItem]
        if contact:
            person = contact[0]
            Utils.show_success(f"Item found, {person}")
        else:
            Utils.show_error("Item not found")
            
    @staticmethod
    def man():
        table = Table(title="List of commands", show_header=True,header_style="bold blue" )
        table.add_column("Commands", style="green")
        table.add_column("working", style="yellow")
        
        info = [
            {
            "command" : "add",
            "work" : "add data to the database"
            },
            {
            "command" : "search",
            "work" : "search the database based on the contact information, contact is used as the primary key"
            },
            {
            "command" : "view",
            "work" : "view the whole database"
            },
            {
                "command" : "man",
                "work" : "open manual"
            },
            {
                "command" : "exit",
                "work" : "exit the application"
            }
                ]
        for information in info:
            table.add_row(information['command'] , information['work'])
        console.print(table)
        

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w",newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FILEHEADER)
            writer.writeheader()
    else:
        pass     
    while(True):
        command = input("Enter your choice : ")
        match command:
            case 'exit':
                Utils.show_success("Thank you !! :heart:")
                break
            case 'add':
                name = input("Enter your name : ")
                contact = input("Enter your contact : ")
                Email = input("Enter your Email :")
                try: 
                    input_obj = Input(name, contact, Email)
                    commands_obj = Commands(input_obj)
                    commands_obj.add()
                    Utils.show_success("Successfully added!")
                except (InvalidContactLength, InvalidEmailExtension, InvalidEmailFormat) as e:
                    Utils.show_error(f"Validation error : {e}")
                    
            case 'search':
                search_Item = input("Enter the contact to be searched : ")
                Commands.search(search_Item)
            case 'view':
                Commands.view()
                
            case 'man':
                Commands.man()
            case _:
             Utils.show_error("wrong choice, try again with a valid command!!")
             
if __name__ == '__main__':       
    main()