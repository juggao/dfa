class StateMachine:
    def __init__(self, symbols, initial_state, accepting_states, transitions):
        self.symbols = symbols
        self.current_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
        self.output = ""
        
    def process_symbols(self, input_symbols):
        for symbol in input_symbols:
            if symbol not in self.symbols:
                print("Invalid symbol:", symbol)
                return False
            
            if self.current_state in self.transitions and symbol in self.transitions[self.current_state]:
                self.output += self.current_state
                self.current_state = self.transitions[self.current_state][symbol]
            else:
                print("Invalid transition:", self.current_state, "-->", symbol)
                return False
        
        if self.current_state in self.accepting_states:
            print("Input Accepted: ", self.output)
        else:
            print("Input Rejected: ", self.output)
        
        return True

states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['0', '1']
initial_state = 'D'
accepting_states = ['D']

transitions = {
    'A': {'0': 'B', '1': 'M'},
    'B': {'0': 'C', '1': 'A'},
    'C': {'0': 'D', '1': 'A'},
    'D': {'0': 'E', '1': 'O'},
    'E': {'0': 'F', '1': 'A'},
    'F': {'0': 'G', '1': 'A'},
    'G': {'0': 'H', '1': 'A'},
    'H': {'0': 'I', '1': 'A'},
    'I': {'0': 'J', '1': 'A'},
    'J': {'0': 'K', '1': 'A'},
    'K': {'0': 'L', '1': 'A'},
    'L': {'0': 'M', '1': 'A'},
    'M': {'0': 'N', '1': 'A'},
    'N': {'0': 'O', '1': 'A'},
    'O': {'0': 'P', '1': 'D'},
    'P': {'0': 'A', '1': 'P'},
    'Q': {'0': 'R', '1': 'A'},
    'R': {'0': 'S', '1': 'A'},
    'S': {'0': 'T', '1': 'A'},
    'T': {'0': 'U', '1': 'A'},
    'U': {'0': 'V', '1': 'A'},
    'V': {'0': 'W', '1': 'A'},
    'W': {'0': 'X', '1': 'A'},
    'X': {'0': 'Y', '1': 'A'},
    'Y': {'0': 'Z', '1': 'A'},
    'Z': {'0': 'A', '1': 'Z'}
}


# Create a state machine object
state_machine = StateMachine(symbols, initial_state, accepting_states, transitions)


import sys

# Check if filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the filename as a command-line argument.")
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename, 'rb') as file:
        binary_data = file.read()
        binary_symbols = [bin(byte)[2:].zfill(8) for byte in binary_data]
        binary_string = ''.join(binary_symbols)
        binary_array = list(binary_string)
        state_machine.process_symbols(binary_array)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
# Process input symbols
#input_symbols = ['0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0']
#state_machine.process_symbols(input_symbols)

