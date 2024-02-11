from typing import List
from enum import Enum
import re

########################################
############### GLOBALS ################
########################################

PIN_ID_COUNTER = 0


def getPinCounter():
    global PIN_ID_COUNTER
    PIN_ID_COUNTER += 1
    return str(PIN_ID_COUNTER).zfill(32)


########################################
############### HELPERS ################
########################################

def extractStringBetween(text, start_substring, end_substring):
    # Create a regular expression pattern to match the substring between the start and end substrings
    pattern = re.compile(fr"{re.escape(start_substring)}(.*?){re.escape(end_substring)}")

    # Use the re.search method to find a match
    match = pattern.search(text)

    if match:
        extracted_string: str = match.group(1)
        return extracted_string
    else:
        return ""


def matchStartAndEnd(text, start_substring, end_substring):
    # Create a regular expression pattern to match the string
    pattern = re.compile(fr"^{re.escape(start_substring)}.*{re.escape(end_substring)}$")

    # Use the re.search method to find a match
    match = pattern.search(text)

    if match:
        matched_string: str = match.group()
        return matched_string
    else:
        return ""


def findAllSubString(text, substring):
    returnList = []
    start = 0
    while start < len(text):
        index = text.find(substring, start)
        if index == -1:
            break
        returnList.append(index)
        start = index + 1
    return returnList


########################################
############### CLASSES ################
########################################

class PinType(Enum):
    EXEC = 0
    BOOl = 1
    OTHER = 3


class PinDirection(Enum):
    IN = 0
    OUT = 1


class ObjectPin(object):
    def __init__(self, stringData: str, source):
        self.content = ""
        self.id = ""
        self.linkSection = ""
        self.linkElementName = ""
        self.linkID = ""
        self.type = PinType.OTHER
        self.direction = PinDirection.IN
        self.source: ObjectElement = source

        self.content = stringData
        if self.content == "":
            return
        self.id = extractStringBetween(self.content, "PinId=", ",")
        self.linkSection = extractStringBetween(self.content, "LinkedTo=(", "),")
        if self.linkSection != "":
            self.linkElementName = self.linkSection.split(" ")[0]
            self.linkID = self.linkSection.split(" ")[1]
            self.linkID = self.linkID.split(",")[0]

        if self.content.find('PinType.PinCategory="exec"') != -1:
            self.type = PinType.EXEC
        else:
            if self.content.find('PinType.PinCategory="bool"') != -1:
                self.type = PinType.BOOl
            else:
                self.type = PinType.OTHER

        if self.content.find('Direction="EGPD_Output"') != -1:
            self.direction = PinDirection.OUT
        else:
            self.direction = PinDirection.IN

    def __str__(self):
        return extractStringBetween(self.content, 'PinName="', '",')

    def __repr__(self):
        return extractStringBetween(self.content, 'PinName="', '",')

    def isConnectedTo(self, otherPin, otherElement):
        return (self.linkID == otherPin.id) and (self.linkElementName == str(otherElement))

    def getSink(self):
        return self.source.findPinSink(self)


class ElementType(Enum):
    BRANCH = 0
    AND_OPERATOR = 1
    OR_OPERATOR = 2
    BOOL_VARIABLE = 3
    PURE_FUNCTION = 4
    OTHER = 5


class ObjectElement(object):
    def __init__(self, stringData: str):
        self.content = stringData
        self.connectionsByData = []
        self.connectionsByFlow = []
        self.conditionElement: ObjectElement

        self.type = ElementType.OTHER
        self.fillType()

        self.pins: List[ObjectPin] = []
        self.conditionPin = ObjectPin
        self.execPin: ObjectPin
        self.thenPin: ObjectPin
        self.elsePin: ObjectPin
        self.fillPins()

    def __str__(self):
        return extractStringBetween(self.content, 'Name="', '" ')

    def __repr__(self):
        return extractStringBetween(self.content, 'Name="', '" ')

    def __eq__(self, other):
        return str(self) == str(other)

    def isValid(self):
        return self.content != ""

    def fillPins(self):
        self.pins.clear()
        indices = findAllSubString(self.content, "CustomProperties Pin ")
        for index in indices:
            line_start = self.content.rfind('\n', 0, index) + 1
            line_end = self.content.find('\n', index)
            if line_end == -1:
                line_end = len(self.content)
            line = self.content[line_start:line_end]
            pin = ObjectPin(line, self)
            self.pins.append(pin)

            if str(pin) == "execute":
                self.execPin = pin
            if str(pin) == "then":
                self.thenPin = pin
            if str(pin) == "else":
                self.elsePin = pin
            if str(pin) == "Condition":
                self.conditionPin = pin

    def fillType(self):
        if "Class=/Script/BlueprintGraph.K2Node_IfThenElse" in self.content:
            self.type = ElementType.BRANCH
            return

        if 'MemberName="BooleanAND"' in self.content:
            self.type = ElementType.AND_OPERATOR
            return

        if 'MemberName="BooleanOR"' in self.content:
            self.type = ElementType.OR_OPERATOR
            return

        if "Class=/Script/BlueprintGraph.K2Node_VariableGet" in self.content:
            if 'PinType.PinCategory="bool"' in self.content:
                self.type = ElementType.BOOL_VARIABLE
                return

        if self.content.find("bIsPureFunc=True"):
            self.type = ElementType.PURE_FUNCTION
            return

        self.type = ElementType.OTHER

    def isConnectedByFlowTo(self, otherElement):
        for pin in self.pins:
            if pin.type == PinType.EXEC:
                for o_pin in otherElement.pins:
                    if pin.isConnectedTo(o_pin, otherElement):
                        return True, pin, o_pin
        return False, None, None

    def isConnectedByDataTo(self, otherElement):
        for pin in self.pins:
            if pin.type != PinType.EXEC:
                for o_pin in otherElement.pins:
                    if pin.isConnectedTo(o_pin, otherElement):
                        return True, pin, o_pin
        return False, None, None

    def fillConnectionsByFlow(self, allElements: List):
        self.connectionsByFlow.clear()
        for other in allElements:
            (success, pin, otherPin) = self.isConnectedByFlowTo(other)
            if success:
                self.connectionsByFlow.append((other, pin, otherPin))

    def fillConnectionsByData(self, allElements: List):
        self.connectionsByData.clear()
        for other in allElements:
            (success, pin, otherPin) = self.isConnectedByDataTo(other)
            if success:
                self.connectionsByData.append((other, pin, otherPin))
                if self.type == ElementType.BRANCH:
                    self.conditionElement = (other, pin, otherPin)

    def findPinSink(self, pin: ObjectPin):
        for connection in self.connectionsByData:
            if connection[1] == pin:
                return connection[0]

        for connection in self.connectionsByFlow:
            if connection[1] == pin:
                return connection[0]

        return ObjectElement("")

    def getLocation(self) -> (int, int):
        if not self.isValid():
            return 0, 0

        X_str = extractStringBetween(self.content, "NodePosX=", "\n")
        X = int(X_str)

        Y_str = extractStringBetween(self.content, "NodePosY=", "\n")
        Y = int(Y_str)

        return [X, Y]

    def move(self, deltaX: int, deltaY: int):
        if not self.isValid():
            return

        X_str = extractStringBetween(self.content, "NodePosX=", "\n")
        X: int = int(X_str)
        currentX = "NodePosX=" + X_str
        self.content = self.content.replace(currentX, "NodePosX=" + str(X + deltaX))

        Y_str = extractStringBetween(self.content, "NodePosY=", "\n")
        Y = int(Y_str)
        currentY = "NodePosY=" + Y_str
        self.content = self.content.replace(currentY, "NodePosY=" + str(Y + deltaY))

    def moveAndPropagate(self, deltaX: int, deltaY: int):
        if not self.isValid():
            return

        self.move(deltaX, deltaY)
        for pin in self.pins:
            if (pin.type == PinType.BOOl and pin.direction == PinDirection.IN) or \
                    (pin.type == PinType.OTHER and pin.direction == PinDirection.IN) or \
                    (pin.type == PinType.EXEC and pin.direction == PinDirection.OUT):
                pin.getSink().moveAndPropagate(deltaX, deltaY)

    def moveToAndPropagate(self, X: int, Y: int):
        currentLocation = self.getLocation()
        delta = X - currentLocation[0], Y - currentLocation[1]
        self.moveAndPropagate(delta[0], delta[1])


def syncConnections(allElements: List[ObjectElement]):
    for element in allElements:
        element.fillPins()

    for element in allElements:
        element.fillConnectionsByData(allElements)
        element.fillConnectionsByFlow(allElements)


def findBranchesAmongElements(allElements):
    branches = []
    for elem in allElements:
        if elem.type == ElementType.BRANCH:
            branches.append(elem)
    return branches


def findAllAndOperatorsAmongElements(allElements):
    ands = []
    for elem in allElements:
        if elem.type == ElementType.AND_OPERATOR:
            ands.append(elem)
    return ands


def findAllOrOperatorsAmongElements(allElements):
    ors = []
    for elem in allElements:
        if elem.type == ElementType.OR_OPERATOR:
            ors.append(elem)
    return ors


def findAllAndOrOperatorsAmongElements(allElements):
    ands = []
    for elem in allElements:
        if elem.type == ElementType.AND_OPERATOR or elem.type == ElementType.OR_OPERATOR:
            ands.append(elem)
    return ands


def importBlueprintElementsFromString(originalContent: str):
    contents = originalContent.replace("End Object", "End Object####").split("####")[:-1]

    bp_elements: List[ObjectElement] = []
    for content in contents:
        bp_elements.append(ObjectElement(stringData=content))

    syncConnections(bp_elements)
    return bp_elements


def importBlueprintElementsFromFile(fileName: str):
    with open(fileName, 'r') as file:
        originalContent = file.read()

    contents = originalContent.replace("End Object", "End Object####").split("####")[:-1]

    bp_elements: List[ObjectElement] = []
    for content in contents:
        bp_elements.append(ObjectElement(stringData=content))

    syncConnections(bp_elements)
    return bp_elements


def exportBlueprintElementsToCode(bp_elements: List[ObjectElement]) -> str:
    newCode: str = ""
    for element in bp_elements:
        newCode = newCode + '\n' + element.content

    return newCode
