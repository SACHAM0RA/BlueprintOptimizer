from Core.OptimizerCore import *

INST_TEMPLATE = \
    '''Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="{START_NAME}" ExportPath=/Script/BlueprintGraph.K2Node_CallFunction'"/Game/RTS_Project/Logic/EntitySystem/EntityTypes/Structures/NewBlueprint.NewBlueprint:NewFunction.{START_NAME}"'
   FunctionReference=(MemberName="StartProfile",MemberGuid=2398C32A48B76964B00CC38CCA9A76DB,bSelfContext=True)
   NodePosX={START_X}
   NodePosY={START_Y}
   NodeGuid=2D0A7C6949308FE6B1279D84A38256D2
   CustomProperties Pin (PinId={START_EXEC_ID},PinName="execute",PinToolTip="\\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId={START_THEN_ID},PinName="then",PinToolTip="\\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=({END_NAME} {END_EXEC_ID},),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=6054A041443C43E02D8F3A88DF43DBD4,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nSelf Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="self",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=A00F07AA47FB53FB169DA6B622993C4B,PinName="Label",PinToolTip="Label\\nName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="{LABEL}",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name="{END_NAME}" ExportPath=/Script/BlueprintGraph.K2Node_CallFunction'"/Game/RTS_Project/Logic/EntitySystem/EntityTypes/Structures/NewBlueprint.NewBlueprint:NewFunction.{END_NAME}"'
   FunctionReference=(MemberName="EndProfile",MemberGuid=59C70B8040A87890497BDDAD523D8226,bSelfContext=True)
   NodePosX={END_X}
   NodePosY={END_Y}
   NodeGuid=73E661FB4729F7C58B979C96EB395825
   CustomProperties Pin (PinId={END_EXEC_ID},PinName="execute",PinToolTip="\\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=({START_NAME} {START_THEN_ID},),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=F28AA84E41F0D474D12D2EBEDF26E997,PinName="then",PinToolTip="\\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=318111EB46A9738609517F88F568C1C4,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\\nSelf Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="self",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId=F41795EB4F77C2919FF2C1A919302955,PinName="Label",PinToolTip="Label\\nName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="{LABEL}",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
   CustomProperties Pin (PinId={VALUE_PIN_ID},PinName="Value",PinToolTip="Value\\nBoolean",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="false",AutogeneratedDefaultValue="false",LinkedTo=({OPERAND_NAME} {OPERAND_PIN_ID},),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
'''

SEQ_TEMPLATE = \
    '''Begin Object Class=/Script/BlueprintGraph.K2Node_ExecutionSequence Name="INST_SEQ_NODE" ExportPath=/Script/BlueprintGraph.K2Node_ExecutionSequence'"/Game/RTS_Project/Logic/EntitySystem/EntityTypes/Structures/NewBlueprint.NewBlueprint:NewFunction.INST_SEQ_NODE"'
   NodePosX=0
   NodePosY=0
   NodeGuid=4097BAB94DD53966A70C1091814B2B51
   CustomProperties Pin (PinId=3106857D430BD47CCFCBDC8AF9CF6CB6,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
{THEN_PINS}
End Object
'''
SEQ_PIN_TEMPLATE = 'CustomProperties Pin (PinId={ID},PinName="then_{COUNTER}",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=({LINK_NAME} {LINK_PIN_ID},),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)'


def extractOperands(root: ObjectElement, result: List[ObjectElement]):
    for pin in root.pins:
        if pin.type == PinType.BOOl and pin.direction == PinDirection.IN:
            if pin.getSink().type != ElementType.AND_OPERATOR and pin.getSink().type != ElementType.OR_OPERATOR:
                result.append(pin.getSink())
            else:
                extractOperands(pin.getSink(), result)


def instrumentElement(bp_element: ObjectElement, baseX: int = 0, baseY: int = 0) -> (str, str, str):
    operand_code = bp_element.content

    pos_x_section = extractStringBetween(operand_code, 'NodePosX=', '\n')
    pos_y_section = extractStringBetween(operand_code, 'NodePosY=', '\n')
    operand_code = operand_code.replace(pos_x_section, str(baseX + 350))
    operand_code = operand_code.replace(pos_y_section, str(baseY + 150))

    current_operand_name = extractStringBetween(bp_element.content, 'Name="', '"')
    new_operand_name = current_operand_name + '_INST'
    operand_name_section = 'Name="' + current_operand_name + '"'
    operand_code = operand_code.replace(operand_name_section, 'Name="' + new_operand_name + '"')

    new_operand_pin_id = getPinCounter()
    start_name = new_operand_name + "_START"
    end_name = new_operand_name + "_END"
    end_value_pin_id = getPinCounter()
    start_exec_id = getPinCounter()

    for pin in bp_element.pins:
        if pin.type == PinType.BOOl and pin.direction == PinDirection.OUT:
            new_pin_content = pin.content.replace(pin.id, new_operand_pin_id)
            new_pin_content = new_pin_content.replace(pin.linkElementName, end_name)
            new_pin_content = new_pin_content.replace(pin.linkID, end_value_pin_id)
            operand_code = operand_code.replace(pin.content, new_pin_content)
            break

    instrument = INST_TEMPLATE.replace("{START_NAME}", start_name)
    instrument = instrument.replace("{END_NAME}", end_name)
    instrument = instrument.replace("{START_THEN_ID}", getPinCounter())
    instrument = instrument.replace("{START_EXEC_ID}", start_exec_id)
    instrument = instrument.replace("{END_EXEC_ID}", getPinCounter())
    instrument = instrument.replace("{VALUE_PIN_ID}", end_value_pin_id)
    instrument = instrument.replace("{OPERAND_NAME}", new_operand_name)
    instrument = instrument.replace("{OPERAND_PIN_ID}", new_operand_pin_id)
    instrument = instrument.replace("{LABEL}", str(bp_element))

    instrument = instrument.replace("{START_X}", str(baseX))
    instrument = instrument.replace("{START_Y}", str(baseY))
    instrument = instrument.replace("{END_X}", str(baseX + 550))
    instrument = instrument.replace("{END_Y}", str(baseY))

    instrument = instrument + '\n' + operand_code

    return instrument, start_name, start_exec_id


def createDummySequence(index: int) -> str:
    dummy_seq_pin = SEQ_PIN_TEMPLATE
    dummy_seq_pin = dummy_seq_pin.replace("{ID}", str(getPinCounter()))
    dummy_seq_pin = dummy_seq_pin.replace("{COUNTER}", str(index))
    dummy_seq_pin = dummy_seq_pin.replace("LinkedTo=({LINK_NAME} {LINK_PIN_ID},),", "")
    return dummy_seq_pin


def InstrumentBlueprint(bp_elements: List[ObjectElement]) -> str:
    branches: List[ObjectElement] = findBranchesAmongElements(bp_elements)
    operands: List[ObjectElement] = []
    for branch in branches:
        extractOperands(branch.conditionElement[0], operands)

    sequence_content = SEQ_TEMPLATE
    seq_then_pins_section = ""
    final_code = ""
    for index, operand in enumerate(operands):
        inst, start_name, exec_pin = instrumentElement(operand, 350, -350*(len(operands)-index) + len(operands)*250)
        final_code = final_code + '\n' + inst

        pin_id = getPinCounter()
        seq_pin = SEQ_PIN_TEMPLATE
        seq_pin = seq_pin.replace("{ID}", str(pin_id))
        seq_pin = seq_pin.replace("{COUNTER}", str(index))
        seq_pin = seq_pin.replace("{LINK_NAME}", start_name)
        seq_pin = seq_pin.replace("{LINK_PIN_ID}", exec_pin)
        seq_then_pins_section = seq_then_pins_section + "   " + seq_pin + '\n'

    if len(operands) == 0:
        seq_then_pins_section + "   " + createDummySequence(0) + '\n'
        seq_then_pins_section + "   " + createDummySequence(1) + '\n'
    if len(operands) == 1:
        seq_then_pins_section + "   " + createDummySequence(1) + '\n'

    sequence_content = sequence_content.replace("{THEN_PINS}", seq_then_pins_section)
    final_code = final_code + '\n' + sequence_content

    return final_code


bp_elements = importBlueprintElementsFromFile('../SamplesBlueprintCode/SampleBlueprint_1')
instrumented = InstrumentBlueprint(bp_elements)
print(instrumented)
