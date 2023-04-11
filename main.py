from typing import List, Dict, Optional
import sys


class Wire:
    def __init__(self, color: str) -> Optional[str]:
        self.color = color


class Module:
    def __init__(self, cable_quantity: int, serialnumber: int) -> Optional[int]:
        self.cable = cable_quantity
        self.serial = serialnumber
        self.__sequence = None
        self.is_serialnumber_odd = True if int(serialnumber) % 2 == 0 else False

    def addcableobject(self, cable: []) -> Optional[List[Wire]]:
        if self.__sequence is None:
            self.__sequence = []
        self.__sequence.append(cable)

    def getCablesequence(self):
        return self.__sequence

def add_new_cable():
    cable_sequence = input("At which position is the cable: ")
    color = input("What is the color: ")
    cable_module[cable_sequence] = color
    print("Saved input", cable_sequence, color)


def show_module():
    print("You can now start with typing the serialnumber and wires")

    while True:
        print("\nWire Menu:")
        print("1. Input serialnumber and wires")
        print("2. Stop the program")

        choice = input("Your choice: ")
        if choice == "1":
            defuseModule()
            break
        elif choice == "2":
            print("Program terminated.")
            sys.exit()
        else:
            print("Invalid input. Please select 1, 2 or 3.")

def getSerialNumber():
    # User input for serial number
    serial_number = input("Enter serial number: ")

    # Check if serial number is valid
    if not serial_number.isdigit():
        print("Error: Invalid serial number. Please enter a number.")
        return None

    # Convert serial number to integer
    serial_number = int(serial_number)

    # Check if serial number is within valid range
    if not (1 <= serial_number <= 999):
        print("Error: Serial number must be between 1 and 999.")
        return None

    return serial_number


def defuseModule():
    # User input 
    serial_number = getSerialNumber()
    colors = ["red", "blue", "yellow", "white", "black"]
    input_str = input("Enter wire names separated by commas: ")
    wire_names = list(map(str.strip, input_str.split(",")))

      # User input for serial number
    if serial_number is None:
        return None
    
    # Create wire objects and add them to wireModule
    wireModule = Module(cable_quantity = 0, serialnumber=serial_number)  # Instance
    for name in wire_names:
        if name == "wire1":
            wire = Wire(color=colors[0])
        elif name == "wire2":
            wire = Wire(color=colors[1])
        elif name == "wire3":
            wire = Wire(color=colors[2])
        elif name == "wire4":
            wire = Wire(color=colors[3])
        elif name == "wire5":
            wire = Wire(color=colors[4])
        elif name == "wire6":
            wire = Wire(color=colors[0])
        else:
            print(f"Error: Invalid wire name '{name}'. Skipping...")
            continue
        
        wireModule.addcableobject(cable=wire)
    
    return wireModule


if __name__ == "__main__":
    show_module()
    colors = ["red", "blue", "yellow", "white", "black"]
    wireModule = defuseModule()
    print("Start program")
   
    cablelist = wireModule.getCablesequence()
    print(cablelist)
    
    # 3 Wire:
    if len(cablelist) == 3:
        if cablelist[0].color != colors[0]:
            print("Cut second wire")
        elif cablelist[-1] == colors[3]:
            print("Cut last wire")
        elif cablelist[1].color <= colors[1]:
            print("Cut last blue wire")
        else:
            print("Cut last wire")

    
    # 4 Wire:
    if len(cablelist) == 4:
        if sum([1 for cable in cablelist if cable.color == colors[0]]) > 1 and wireModule.serial % 2 == 1:
            print("Cut last red wire")
        elif cablelist[-1].color == colors[2] and colors[0] not in [cable.color for cable in cablelist]:
            print("Cut first wire")
        elif sum([1 for cable in cablelist if cable.color == colors[1]]) == 1:
            print("Cut first wire")
        elif sum([1 for cable in cablelist if cable.color == colors[2]]) > 1:
            print("Cut last wire")
        else:
            print("Cut second wire")

    # 5 Wire:
    if len(cablelist) == 5:
        if cablelist[-1] == colors[4] and wireModule.serial % 2 == 1:
            print("Cut fourth wire")
        elif cablelist[0].color == colors[0] and cablelist[2].color <= colors[2]:
            print("Cut first wire")
        elif cablelist[-1].color != colors[4]:
            print("Cut second wire")
        else:
            print("Cut first wire")

    # 6 Wire:
    if len(cablelist) == 6:
        if not(colors[2] in cablelist) and wireModule.serial % 2 == 1:
            print("Cut third wire")
        elif sum([1 for cable in cablelist if cable.color == colors[2]]) == 1 and cablelist[3].color <= colors[3]:
            print("Cut fourth wire")
        elif cablelist[0].color != colors[0]:
            print("Cut last wire")
        else:
            print("Cut fourth wire")
