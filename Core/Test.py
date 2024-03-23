from Core.LoadCalculation import *
from Core.ShortCircuit import *
from Core.OperandPermutations import *

if __name__ == "__main__":
    bp_elements = importBlueprintElementsFromFile('../SamplesBlueprintCode/SampleBlueprint_2')
    search_space = generateAllOperandPermutations(bp_elements)
    best_permutation = min(search_space, key=lambda permutation: calculateLoadForElements(permutation))
    short_circuited_best = transformToShortCircuitFormat(best_permutation)
    transformed_code = exportBlueprintElementsToCode(short_circuited_best)
    print(transformed_code)
