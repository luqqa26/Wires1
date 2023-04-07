from typing import List, Dict, Optional


def add_new_cable():
    cable_sequence = input("At which position is the cable: ")
    color = input("What is the color: ")
    cable_module[cable_sequence] = color
    print("Saved input", cable_sequence, color)


def show_module():
    cable_sequence = input("At which point is the cable: ")
    if name in cable_module:
        print(cable_sequence, ":", cable_module[cable_sequence])
    else:
        print("Error no input found:", cable_sequence)

    while True:
        print("\nCable Menu:")
        print("1. Add Cable")
        print("2. Show Module")
        print("3. Stop")

        choice = input("Your choice: ")
        if choice == "1":
            add_new_cable()
        elif choice == "2":
            show_module()
        elif choice == "3":
            break
        else:
            print("Invalid input. Please select 1, 2 or 3.")


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


def defuseModule(module):
    pass


def test():
    pass


if __name__ == "__main__":
    # test()
    print("Start program")
    colors = ["red", "blue", "yellow", "white", "black"]

    wire1 = Wire(color=colors[0])
    wire2 = Wire(color=colors[3])
    wire3 = Wire(color=colors[4])
    wire4 = Wire(color=colors[4])
    wire5 = Wire(color=colors[1])
    wire6 = Wire(color=colors[4])

    wireModule = Module(cable_quantity=0, serialnumber=0)  # Instance
    wireModule.addcableobject(cable=wire1)
    wireModule.addcableobject(cable=wire2)
    wireModule.addcableobject(cable=wire3)
    wireModule.addcableobject(cable=wire4)
    wireModule.addcableobject(cable=wire5)
    wireModule.addcableobject(cable=wire6)

    cablelist = wireModule.getCablesequence()
    print(cablelist)
    # 3 Kabel:
    if len(cablelist) == 3:
        if cablelist[0].color != colors[0]:
            print("Cut second wire")
        elif cablelist[-1] == colors[3]:
            print("Cut last wire")
        elif cablelist[1].color <= colors[1]:
            print("Cut last blue wire")
        else:
            print("Cut last wire")

    # 4 Kabel:
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

    # 5 Kabel:
    if len(cablelist) == 5:
        if cablelist[-1] == colors[4] and wireModule.serial % 2 == 1:
            print("Cut fourth wire")
        elif cablelist[0].color == colors[0] and cablelist[2].color <= colors[2]:
            print("Cut first wire")
        elif cablelist[-1].color != colors[4]:
            print("Cut second wire")
        else:
            print("Cut first wire")

    # 6 Kabel:
    if len(cablelist) == 6:
        if not(colors[2] in cablelist) and wireModule.serial % 2 == 1:
            print("Cut third wire")
        elif sum([1 for cable in cablelist if cable.color == colors[2]]) == 1 and cablelist[3].color <= colors[3]:
            print("Cut fourth wire")
        elif cablelist[0].color != colors[0]:
            print("Cut last wire")
        else:
            print("Cut fourth wire")
