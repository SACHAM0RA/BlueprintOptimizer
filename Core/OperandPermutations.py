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
        orders = []
        new_pin_contents = []
        for idx, name in enumerate(perm):
            orders.append(data_names.index(name))
            old_pin_content = data_pins[idx].content
            new_pin_contents.append(old_pin_content.replace('PinName="' + data_names[idx] + '"', 'PinName="' + name + '"'))
            new_operator_content = new_operator_content.replace(old_pin_content, "@@@" + str(idx) + "@@@")

        for idx, order in enumerate(orders):
            new_operator_content = new_operator_content.replace("@@@" + str(order) + "@@@", new_pin_contents[idx])

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

    r_permutations: List[List[ObjectElement]] = []
    for p in permutations:
        text = exportBlueprintElementsToCode(p)
        n = importBlueprintElementsFromString(text)
        r_permutations.append(n)
    return r_permutations


if __name__ == "__main__":
    bp_elements = importBlueprintElementsFromFile('../SamplesBlueprintCode/SampleBlueprint_2')
    search_space = generateAllOperandPermutations(bp_elements)
    code = exportBlueprintElementsToCode(search_space[3])
    print(code)