from mendeleev import element

element_list = ("Ne","Si","V","Ca","Bi","Br","Cs","Ga","Ar", "C", "Re", "Os", "As", "I")

allowed_groups = ("Noble gases", "Alkali metals", "Alakine earth metals", "Halogens")

def get_group_name(eih):
    if eih.group.name not in allowed_groups:
        print('Group Name: N/A')
    else:
        print(f'Group Name: {eih.group.name}')

def get_group(eih):
    if eih.group.symbol[-1] == "B":
        print('Group: N/A')
    else:
        print(f'Group: {eih.group.symbol[:-1]}')

x = 1
for i in element_list:
    eih = element(i)
    print(f'\n#{str(x)} Element: {eih.name}')
    
    print(f'Electron Notation: {str(eih.ec)}')

    if eih.group.name == "Noble gases":
        print('Noble Gas Conf: N/A')
    else:
        print(f'Noble Gas Conf: [{eih.ec.get_largest_core()[0]}] {str(eih.ec).replace(str(eih.ec.get_largest_core()[1]), "")} ')

    get_group(eih)
    
    get_group_name(eih)

    print(f'Block: {eih.block}')

    if eih.series not in ("Alkali metals", "Alkaline earth metals", "Transition Metals", "Metalloids"):
        metal_status = "Nonmetal"
    elif eih.series == "Metalloids":
        metal_status = "Metalloid"
    else:
        metal_status = "Metal"
    print(f'Metal Status: {metal_status}')

    x += 1
    
