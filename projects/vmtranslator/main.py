import os
import sys
from vmtranslator import codewriter
from vmtranslator import parser


def main():
    fn = sys.argv[1]
    projects_folder = os.getcwd() + "\\projects\\"
    fn = os.path.join(projects_folder, fn)
    outfile = sys.argv[1].replace(".vm", ".asm")
    outfn = os.path.join(projects_folder, outfile)
    if os.path.exists(fn):
        with open(outfn, 'w') as asmf:
            w = codewriter.CodeWriter(asmf)
            # Write bootstrap code
            w.writeInit()
            p = parser.Parser(fn)
            while p.hasMoreCommands():
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
    else:
        print("Incorrect path.")
        print(fn)
        sys.exit()


if __name__ == "__main__":
    main()