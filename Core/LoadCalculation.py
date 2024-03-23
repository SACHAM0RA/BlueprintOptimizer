from Core.OptimizerCore import *


def calculateLoadForElement(element: ObjectElement) -> float:
    if element.content == "":
        return 0.0

    if element.type == ElementType.BOOL_VARIABLE:
        return 1.0
    elif element.type == ElementType.PURE_FUNCTION:
        evaluationLoad = 3.0
        for pin in element.pins:
            if pin.direction == PinDirection.IN and pin.type != PinType.EXEC and str(pin) != "self":
                child = element.findPinSink(pin)
                evaluationLoad = evaluationLoad + calculateLoadForElement(child)
        return evaluationLoad
    elif element.type == ElementType.OTHER:
        evaluationLoad = 2.0
        for pin in element.pins:
            if pin.direction == PinDirection.IN and pin.type != PinType.EXEC and str(pin) != "self":
                child = element.findPinSink(pin)
                evaluationLoad = evaluationLoad + calculateLoadForElement(child)
        return evaluationLoad
    elif element.type == ElementType.AND_OPERATOR:
        evaluationLoad = 2.0
        counter = 0
        for pin in element.pins:
            if pin.direction == PinDirection.IN and pin.type != PinType.EXEC and str(pin) != "self":
                child = element.findPinSink(pin)
                evaluationLoad = evaluationLoad + (0.5**counter) * calculateLoadForElement(child)
                counter = counter + 1
        return evaluationLoad
    elif element.type == ElementType.OR_OPERATOR:
        evaluationLoad = 2.0
        counter = 0
        for pin in element.pins:
            if pin.direction == PinDirection.IN and pin.type != PinType.EXEC and str(pin) != "self":
                child = element.findPinSink(pin)
                evaluationLoad = evaluationLoad + (0.5**counter) * calculateLoadForElement(child)
                counter = counter + 1
        return evaluationLoad
    else:
        return 0.0


def calculateLoadForElements(bp_elements: List[ObjectElement]) -> float:
    evaluationLoad = 0.0
    branches = findBranchesAmongElements(bp_elements)
    for branch in branches:
        evaluationLoad = evaluationLoad + calculateLoadForElement(branch.conditionElement[0])
    return evaluationLoad


if __name__ == "__main__":
    bp_elements = importBlueprintElementsFromFile('../SamplesBlueprintCode/SampleBlueprint_2')
    load = calculateLoadForElements(bp_elements)
    print(load)
