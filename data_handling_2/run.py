from config_p2 import subjects
from data_handling.Input import Input
from data_handling.exception import *
from data_handling.run import Utils
from Console.rich import Console
from rich.table import Table
from config import FILENAME_MARKS
import os
import json

from utils import Utils

class controller:
    def __init__(self, input_obj, marks) -> None:
        self.input_obj = input_obj
        self.marks = marks
        self.UUID = controller.get_UUID()
        
        
    def dumpData(self):
        highestmarks, highestname = self.calculations("highest_marks")
        curr_data_marks = {
            'maths' : self.marks['maths'],
            'physics' : self.marks['physics'],
            'computer science' : self.marks['computer science'],
            'oops': self.marks['oops'],
            'system design' : self.marks['system design'], 
        }
        curr_indentification = {
            "name" : self.input_obj.name,
            "contact" : self.input_obj.contact,
            "Email" : self.input_obj.Email,
            'average' : self.calculations("average"), 
            "highest_marks" : highestmarks,
            "highest_subject" : highestname
        }
        
        inden = Utils.load_json("identification.json")
        inden.append(curr_indentification)
        Utils.dump_json(inden)
        
        
        
        data = Utils.load_json()
        data.append(curr_data_marks)
        Utils.dump_json(data)
    
    def calculations(self, choice):
        total = sum(self.marks.values())
        total_len = len(self.marks)
        match choice:
            case "average" :
                return total/total_len
            case "highest_marks":
                highest = max(self.marks.values())
                subject = [sub for sub, score in self.marks.items() if score == highest]
                return subject,highest
    
    def calc_DB(self):
        data = Utils.load_json()
        if data:
            highest = []
                
                

def main():
    name = input("Enter your name : ")
    contact = input("Enter your contact : ")
    Email = input("Enter your Email : ")
    try:
        input_obj = Input(name=name, contact=contact, Email=Email)
    except (InvalidContactFormat, InvalidContactLength, InvalidEmailExtension, InvalidEmailFormat) as e:
        Utils.show_error(e)
    print("Enter your marks : ")
    mark_data = {}
    for subject in subjects:
        mark_data[subject] = int(input(f"Enter your marks in {subject} : ")) 
    if not os.path.exists(FILENAME_MARKS):
        with open(FILENAME_MARKS, "w") as f:
            json.dump([],f,indent=4)
    else:
        controller(input_obj, mark_data)
     
main()