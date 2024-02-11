from itertools import permutations
from Core.OptimizerCore import *


def getOperandPermutationsForOperator(operator: ObjectElement) -> List[ObjectElement]:
    results: List[ObjectElement] = []

    pins = operator.pins
    data_pins = []
    data_names = []
    for p in pins:
        if p.type == PinType.BOOl and p.direction == PinDirection.IN:
            data_pins.append(p)
            data_names.append(str(p))

    pin_perms = list(permutations(data_names))
    for perm in pin_perms:
        new_operator_content = operator.content
        for idx, name in enumerate(perm):
            old_pin_content = data_pins[idx].content
            new_pin_content = old_pin_content.replace('PinName="' + data_names[idx] + '"', 'PinName=@@@@"' + name + '"')
            new_operator_content = new_operator_content.replace(old_pin_content, new_pin_content)

        new_operator_content = new_operator_content.replace('PinName=@@@@"', 'PinName="')
        results.append(ObjectElement(stringData=new_operator_content))

    return results


def generateElementListsForOperatorByOperandPermutations(operator: ObjectElement, bp_elements: List[ObjectElement]) \
        -> List[List[ObjectElement]]:

    permutations: List[List[ObjectElement]] = []
    op_perms = getOperandPermutationsForOperator(operator)
    for p in op_perms:
        new_list = bp_elements.copy()
        new_list.remove(operator)
        new_list.append(p)
        permutations.append(new_list)

    return permutations


def generateAllOperandPermutations(bp_elements: List[ObjectElement]) -> List[List[ObjectElement]]:
    original_elements = bp_elements.copy()
    permutations: List[List[ObjectElement]] = [original_elements]

    operators = findAllAndOrOperatorsAmongElements(original_elements)

    for op in operators:
        to_check = permutations.copy()
        for t in to_check:
            new_lists = generateElementListsForOperatorByOperandPermutations(op, t)
            permutations.remove(t)
            permutations.extend(new_lists)

    return permutations


bp_elements = importBlueprintElementsFromFile('../SamplesBlueprintCode/SampleBlueprint_2')
search_space = generateAllOperandPermutations(bp_elements)
transformed_code = exportBlueprintElementsToCode(search_space[3])
print(transformed_code)