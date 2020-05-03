class SendMoreMoneyConstrain:
    def __init__(self,letters):
        self.letters = letters

    def satisfied(self, assignment):
        if len(set(assignment.values()))<len(assignment):
            return False

        if len(assignment) == len(self.letters):
            #Getting all the assignment values
            c = assignment['C']
            r = assignment['R']
            o = assignment['O']
            s = assignment['S']
            a = assignment['A']
            d = assignment['D']
            n = assignment['N']
            g = assignment['G']
            e = assignment['E']

            #checking if the assignment is right
            cross = c * 10000 + r * 1000 + o * 100 + s*10 + s
            road = r * 10000 + o * 1000 + a * 100 + d*10 + s
            danger = d * 100000 + a * 10000 + n*1000 + g * 100 + e*10 + r
            return cross+road == danger
        return True

class CSP():
    def __init__(self,variables,domain):
        self.variables = variables
        self.domain = domain
        self.constraints= {}

        for var in self.variables:
            self.constraints[var] = []
            if var not in self.domain:
                print("Domain Assignment Error")
                raise LookupError("Domain Assignment Error")

    def add_constraint(self,constraint):
        for variable in constraint.letters:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self,variable,assignment):
        '''To check all the constraints'''
        for cons in self.constraints[variable]:
            if not cons.satisfied(assignment):
                return False
        return True

    def backtracking_search(self,assignment={}):
        '''To run a backtracking algorithm with constraints'''
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domain[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first,local_assignment):
                #print(local_assignment)
                #print()
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None


if __name__ == "__main__":
    letters = list("CROSADNGE")
    possible_digits = {}
    for letter in letters:
        possible_digits[letter] = [0,1,2,3,4,5,6,7,8,9]
    #The greatest possible carry C4 can be 1
    possible_digits["D"] = [1]
    csp = CSP(letters,possible_digits)
    csp.add_constraint(SendMoreMoneyConstrain(letters))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found")
    else:
        print(solution)


#Output
#{'C': 9, 'R': 6, 'O': 2, 'S': 3, 'A': 5, 'D': 1, 'N': 8, 'G': 7, 'E': 4}



        
