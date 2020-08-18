DEST_DICT = {
        'null':'000',
        'M':'001',
        'D':'010',
        'MD':'011',
        'A':'100',
        'AM':'101',
        'AD':'110',
        'AMD':'111'
    }

COMP_DICT = {
        '0':'0101010',
        '1':'0111111',
        '-1':'0111010',
        'D':'0001100',
        'A':'0110000',
        '!D':'0001101',
        '!A':'0110001',
        '-D':'0001111',
        '-A':'0110011',
        'D+1':'0011111',
        'A+1':'0110111',
        'D-1':'0001110',
        'A-1':'0110010',
        'D+A':'0000010',
        'D-A':'0010011',
        'A-D':'0000111',
        'D&A':'0000000',
        'D|A':'0010101',
        'M':'1110000',
        '!M':'1110001',
        '-M':'1110011',
        'M+1':'1110111',
        'M-1':'1110010',
        'D+M':'1000010',
        'D-M':'1010011',
        'M-D':'1000111',
        'D&M':'1000000',
        'D|M':'1010101'
    }

JUMP_DICT = {
        'null':'000',
        'JGT':'001',
        'JEQ':'010',
        'JGE':'011',
        'JLT':'100',
        'JNE':'101',
        'JLE':'110',
        'JMP':'111'
    }

def dest(mnemonic):
    """returns the binary code (3 bits) of the dest mnemonic"""
    return DEST_DICT[mnemonic]

def comp(mnemonic):
    """Returns the binary code (7 bits) of the comp mnemonic"""
    return COMP_DICT[mnemonic]

def jump(mnemonic):
    """Returns the binary code ( 3 bits) of the jump mnemonic"""
    return JUMP_DICT[mnemonic]

class Parser():

    def __init__(self, input_file):

        with open(input_file) as f:
            self.commands = self.clean_lines(f.readlines())
        self.idx = -1
        self.cur_cmd = ""

    def clean_lines(self, lines):
        cleaned_lines = []
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            elif "//" in line:
                line = line.split('//')[0].strip()
                if line == "":
                    continue
            cleaned_lines.append(line)
        return cleaned_lines
        
    def hasMoreCommands(self):
        """Are there more commands in the input?"""
        if self.idx + 1 < len(self.commands):
            return True
        return False

    def advance(self):
        """Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands() is true. Initially there is no current command.
        """
        self.idx += 1
        self.cur_cmd = self.commands[self.idx]

    def commandType(self):
        """Returns the type of the current command:
        A Command for @XXX where XXX is either a symbol or a decimal number. C Command for dest=comp;jump. L Commands for (Xxx) where Xxx is a symbol."""
        if "@" in self.cur_cmd:
            return 'A_COMMAND'
        elif "(" and ")" in self.cur_cmd:
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        """Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). Should be called only when commandType() is A Command or L Command"""
        if "@" in self.cur_cmd:
            return self.cur_cmd[1:]
        elif "(" and ")" in self.cur_cmd:
            return self.cur_cmd[1:-1]

    def dest(self):
        """Returns the dest menmonic in the current C-command (8 possibilities). Should be called only when commandType() is C_Command."""
        if '=' in self.cur_cmd:
            return self.cur_cmd.split('=')[0]
        else:
            return 'null'

    def comp(self):
        """Returns the comp menmonic in the current C-command (28 possibilities). Should be called only when commandType() is C_Command"""
        if "=" in self.cur_cmd and ';' in self.cur_cmd:
            return self.cur_cmd.split(';')[0].split('=')[1]
        elif "=" in self.cur_cmd:
            return self.cur_cmd.split('=')[1]
        elif ";" in self.cur_cmd:
            return self.cur_cmd.split(';')[0]
        else:
            return self.cur_cmd

    def jump(self):
        """Returns the jump mnemonic in the current C-command(8 possibilities). Should be called only when commandType() is C-Command"""
        if ';' in self.cur_cmd:
            return self.cur_cmd.split(';')[1]
        else:
            return "null"
    

class Symbol_Table():

    def __init__(self):
        self.table = {
            'SP':'0',
            'LCL':'1',
            'ARG':'2',
            'THIS':'3',
            'THAT':'4',
            'R0':'0',
            'R1':'1',
            'R2':'2',
            'R3':'3',
            'R4':'4',
            'R5':'5',
            'R6':'6',
            'R7':'7',
            'R8':'8',
            'R9':'9',
            'R10':'10',
            'R11':'11',
            'R12':'12',
            'R13':'13',
            'R14':'14',
            'R15':'15',
            'SCREEN':'16384',
            'KBD':'24576'
            }

    def addEntry(self, symbol, address):
        """Adds the pair(symbol, address) to the table"""
        self.table[symbol] = address

    def contains(self, symbol):
        """Does the symbol table contain the given symbol?"""
        return symbol in self.table

    def getAddress(self, symbol):
        """Returns the address associated with the symbol"""
        return self.table[symbol]
