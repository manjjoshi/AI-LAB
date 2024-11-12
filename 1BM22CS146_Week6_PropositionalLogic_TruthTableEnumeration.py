import itertools


def evaluate_formula(formula, valuation):
    
    formula = formula.replace('p', str(valuation['p']))
    formula = formula.replace('q', str(valuation['q']))

    
    return eval(formula)

def extract_variables(formula):
    variables = set()
    for char in formula:
        if char.isalpha():  
            variables.add(char)
    return list(variables)

def generate_truth_table(KB, query):
    
    variables = extract_variables(KB) + extract_variables(query)
    variables = list(set(variables))  

    
    print("Truth Table:")
    print(" | ".join(variables + ["KB", "Query"]))
    print("-" * (len(variables) * 4 + 12))

    
    entails_query = True

    
    for assignment in itertools.product([False, True], repeat=len(variables)):
        valuation = dict(zip(variables, assignment))

        
        KB_truth = evaluate_formula(KB, valuation)
        query_truth = evaluate_formula(query, valuation)

        
        row = [str('T' if valuation[var] else 'F') for var in variables] 
        row.append(str('T' if KB_truth else 'F'))  
        row.append(str('T' if query_truth else 'F'))  
        print(" | ".join(row))

        if KB_truth and not query_truth:
            entails_query = False

    print("\nKB entails query:", entails_query)

KB = input("Enter the knowledge base (e.g., 'p and (p != q)'): ")
query = input("Enter the query (e.g., 'q'): ")

generate_truth_table(KB, query)
