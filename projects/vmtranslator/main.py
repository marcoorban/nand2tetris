from os import listdir
from os.path import isfile, join, splitext, exists
from pathlib import Path
from sys import exit, argv
from vmtranslator import codewriter
from vmtranslator import parser

def main():
    path = Path(argv[1])
    try:
        exists(path)
    except:
        print(f"Path {path} does not exist.")
        exit()
    vm_files = [join(path, f) for f in listdir(path) if (isfile(join(path, f)) and splitext(f)[1] == '.vm')]
    asm_file_name = argv[1].split('/')[-1] + '.asm'
    asm_file_path = join(path, asm_file_name)

    with open(asm_file_path, 'w') as asmf:
        w = codewriter.CodeWriter(asmf)
        # Write bootstrap code
        w.writeInit()
        # Loop through all vm files
        for vmfile in vm_files:
            p = parser.Parser(vmfile)
            while p.hasMoreCommands():
                w.static_name = p.current_file.replace(".vm", "")
                p.advance()
                if p.command_type() == "C_ARITHMETIC":
                    w.writeArithmetic(p.arg1())
                elif p.command_type() == "C_PUSH":
                    w.writePush(p.arg1(), p.arg2())
                elif p.command_type() == "C_POP":
                    w.writePop(p.arg1(), p.arg2())
                elif p.command_type() == "C_FUNCTION":
                    w.writeFunction(p.get_fname(), p.get_numLocals())
                elif p.command_type() == "C_RETURN":
                    w.writeReturn()
                elif p.command_type() == "C_CALL":
                    w.writeCall(p.get_fname(), p.get_numLocals())
                elif p.command_type() == "C_LABEL":
                    w.writeLabel(p.get_labelname())
                elif p.command_type() == "C_GOTO":
                    w.writeGoTo(p.get_labelname())
                elif p.command_type() == "C_IF":
                    w.writeIf(p.get_labelname())

if __name__ == "__main__":
    main()