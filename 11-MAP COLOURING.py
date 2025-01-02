class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_variables = [v for v in self.variables if v not in assignment]
        var = unassigned_variables[0]

        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                assignment.pop(var)

        return None


def main():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {
        'WA': ['r', 'g', 'b'],
        'NT': ['r', 'g', 'b'],
        'SA': ['r', 'g', 'b'],
        'Q': ['r', 'g', 'b'],
        'NSW': ['r', 'g', 'b'],
        'V': ['r', 'g', 'b'],
        'T': ['r', 'g', 'b']
    }
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }

    csp = MapColoringCSP(variables, domains, constraints)
    assignment = csp.backtracking_search()
    if assignment:
        print("Solution found:")
        for var, value in assignment.items():
            print(f"{var}: {value}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
