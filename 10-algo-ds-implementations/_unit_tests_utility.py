# This class reads inputs from the CLI or a file return a list of inputs
# The input format is:
#   # Test cases comments
#   [n] # Number of lines comment
#   [input type 1] [values] # Comment: int, float, str ar accepted
#   [input type 2] [values] # Comment: int, float, str ar accepted
# Example:
#   # This is an axample of a test case
#   3 # This is the number of line
#   int 1 2 3 4 5 # This is integer values
#   float 1.2 3 4.5 # This is float values
#   str Azul Hey Salut Hola # This is str values
#   Output:
#      1    2   3       4   5
#      1.2  3.0 4.5
#      Azul Hey Salut   Hola
class Unit_Tests_Utility:
    def __init__(self):
        self._line_count = 0
        self.comments = []
        self.inputs = []

    def get_inputs(self):
        self.comments = []
        self.inputs = []

        # Read the test case description
        input_line = input().split(' ')
        while input_line[0] == '#':
            self.comments.append(' '.join(input_line))
            input_line = input().split(' ')

        # Read the number of inputs
        assert(input_line[0].isnumeric())
        for i in range(1, len(input_line)):
            
            assert(input_line[i] == '' or input_line[i][0] == '#')
            if len(input_line[i]) != 0 and input_line[i][0] == '#':
                self.comments.append(' '.join(input_line[i:]))
                break
        self._line_count = int(input_line[0])

        # Read the inputs + their attached comment
        for _ in range(self._line_count):
            
            input_line = input().split(' ')
            
            assert(len(input_line) > 1)
            assert(input_line[0] in ('int', 'float', 'str'))

            # Find the start positions of inputs and comment:
            input_start = -1
            comment_start = 1
            while comment_start < len(input_line):
                            
                if len(input_line[comment_start]) != 0:
                    if input_line[comment_start][0] == '#':
                        break

                    elif input_start == -1 and len(input_line[comment_start]) != 0:
                        input_start = comment_start
                
                comment_start += 1
            
            assert(comment_start > input_start) # Make sure that the comment is after the input

            if comment_start < len(input_line):
                self.comments.append(' '.join(input_line[comment_start:]))
            
            if input_start == -1:
                self.inputs.append([])
                
            else:
                if input_line[0] == 'int':
                    self.inputs.append([int(input_line[i]) for i in range(1, comment_start)])

                elif  input_line[0] == 'float':
                    self.inputs.append([float(input_line[i]) for i in range(1, comment_start)])

                elif  input_line[0] == 'str':
                    self.inputs.append(input_line[1:comment_start])

def print_list(list, list_name):

    print("List Name: ", list_name)
    for i in range(len(list)):
        print(list[i])

if __name__ == "__main__":
    unit_tests = Unit_Tests_Utility()

    unit_tests.get_inputs()

    print_list(unit_tests.comments, "Comments")
    print_list(unit_tests.inputs, "Inputs")
