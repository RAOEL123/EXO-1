def table_de_verite(expression):
    variables = []
    for char in expression:
        if char.isalpha() and char not in variables:
            variables.append(char)

    num_variables = len(variables)
    table = []

    for i in range(2 ** num_variables):
        binary = bin(i)[2:].zfill(num_variables)
        values = {variables[j]: int(binary[j]) for j in range(num_variables)}
        result = eval(expression, values)
        row = [values[var] for var in variables] + [result]
        table.append(row)

    return variables, table

def obtenir_premiere_forme_canonique(expression):
    variables, truth_table = table_de_verite(expression)
    minterms = []

    for i, row in enumerate(truth_table):
        if row[-1]:  # Si le résultat est True
            minterm = []
            for j, value in enumerate(row[:-1]):
                if value:  # Si la variable est True
                    minterm.append(variables[j])
                else:  # Si la variable est False
                    minterm.append('~' + variables[j])
            minterms.append("".join(minterm))

    return " + ".join(minterms)

expression = input("Entrez la fonction logique (utilisez des opérateurs logiques comme &, |, ^, ~ pour AND, OR, XOR, NOT) : ")
premiere_forme_canonique = obtenir_premiere_forme_canonique(expression)

print("La première forme canonique de l'expression logique est :", premiere_forme_canonique)
