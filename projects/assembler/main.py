import sys
import pathlib
import assembler

def main(argv):
    directory = "C:\\MarcoDocs\\projects\\nand2tetris\\projects\\06"
    file = pathlib.Path(directory, argv[1])
    out = argv[1].replace('.asm', '.hack')
    out_path = pathlib.Path(directory, out)
    parser = assembler.Parser(file)
    # First pass: go through the code and construct symbol table
    symbol_table = assembler.Symbol_Table()
    address = 0  # Starting ROM address of the program
    while parser.hasMoreCommands():
        parser.advance()
        # Incremente the ROM address of program if A or C cmd is encountered.
        if parser.commandType() in ["A_COMMAND", "C_COMMAND"]:
            address += 1
        # If L command is encountered, extract the symbol and check if
        # symbol exists in symbol table. Add if it doesn't exist in sym table.
        elif parser.commandType() == "L_COMMAND":
            symbol = parser.cur_cmd[1:-1]
            if not symbol_table.contains(symbol):
                symbol_table.addEntry(symbol, str(address))
    # Second pass; handle variables
    parser.idx = -1
    with open(out_path, 'w') as hackFile:
        ram_Addr = 16
        while parser.hasMoreCommands():
            parser.advance()
            if parser.commandType() == "A_COMMAND":
                symbol = parser.symbol()
                opcode = "0"
                # If symbol is regular int, get it's binary representation
                if symbol.isnumeric():
                    value = symbol
                # If it's a variable, look it up in the symbol table
                else:
                    # If it exists, retrieve its value
                    if symbol_table.contains(symbol):
                        value = symbol_table.getAddress(symbol)
                    # If it doesn't, add it to symbol table
                    else:
                        value = ram_Addr
                        symbol_table.addEntry(symbol, value)
                        ram_Addr += 1
                value = format(int(value), '015b')
                hackFile.write(opcode + value + '\n')
            elif parser.commandType() == "C_COMMAND":
                opcode = "111"
                # Get comp bytecode
                comp_mnemonic = parser.comp()
                comp = assembler.comp(comp_mnemonic)
                # Get destination bytecode
                dest_mnemonic = parser.dest()
                dest = assembler.dest(dest_mnemonic)
                # Get jump code
                jump_mnemonic = parser.jump()
                jump = assembler.jump(jump_mnemonic)
                hackFile.write(opcode + comp + dest + jump + '\n')
            elif parser.commandType() == "L_COMMAND":
                continue

if __name__ == "__main__":
    main(sys.argv)
