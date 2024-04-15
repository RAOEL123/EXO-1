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

expression = input("Entrez la fonction logique (utilisez des opérateurs logiques comme &, |, ^, ~ pour AND, OR, XOR, NOT) : ")
variables, truth_table = table_de_verite(expression)

print("Table de vérité pour l'expression logique :", expression)
print("-" * (len(expression) + 20))
print(" | ".join(variables + ['Résultat']))
print("-" * (len(expression) + 20))
for row in truth_table:
    print(" | ".join(str(value) for value in row))
print("-" * (len(expression) + 20))
