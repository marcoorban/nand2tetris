import sys

class Parser():

    def __init__(self, input_file):
        self.commands = self.sanitize(input_file)
        self.idx = -1
        self.current_command = ''

    def sanitize(self, input_file):
        "Sanitizes input file and removes all comments and other bad stuff (whitespace and the like)"
        with open(input_file, 'r') as f:
            cleaned_lines = []
            stuff = f.readlines()
            for line in stuff:
                line = line.split('//')[0].strip()
                if not line == "":
                    cleaned_lines.append(line)
        return cleaned_lines

    def hasMoreCommands(self):
        if self.idx + 1 < len(self.commands):
            return True
        return False
    
    def advance(self):
        self.idx += 1
        self.current_command = self.commands[self.idx]

    def command_type(self):
        cmd = self.current_command.split(' ')[0]
        # Arithmetic Commands
        if cmd in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return "C_ARITHMETIC"
        # Memory Access
        elif cmd == "push":
            return "C_PUSH"
        elif cmd == "pop":
            return "C_POP"
        # Program Flow
        elif cmd == "label":
            return "C_LABEL"
        elif cmd == "goto":
            return "C_GOTO"
        elif cmd == "if-goto":
            return "C_IF"
        # Function Calling
        elif cmd == "function":
            return "C_FUNCTION"
        elif cmd == "call":
            return "C_CALL"
        elif cmd == "return":
            return "C_RETURN"
        else:
            print("Command not recognized:")
            print(self.current_command)

    def arg1(self):
        parts = self.current_command.split(' ')
        if len(parts) > 1:
            return parts[1]
        else:
            return parts[0]

    def arg2(self):
        return self.current_command.split(' ')[2]

    def get_fname(self):
        return self.current_command.split(' ')[1]
    
    def get_numLocals(self):
        return self.current_command.split(' ')[2]

    def get_labelname(self):
        return self.current_command.split(' ')[1]

