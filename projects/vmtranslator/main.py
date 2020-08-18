import os
import sys
from vmtranslator import codewriter
from vmtranslator import parser


def main():
    fn = sys.argv[1]
    fn = os.path.join("C:\\MarcoDocs\\projects\\nand2tetris\\projects\\", fn)
    outfile = sys.argv[1].replace(".vm", ".asm")
    outfn = os.path.join("C:\\MarcoDocs\\projects\\nand2tetris\\projects\\", outfile)
    if os.path.exists(fn):
        with open(outfn, 'w') as asmf:
            w = codewriter.CodeWriter(asmf)
            p = parser.Parser(fn)
            while p.hasMoreCommands():
                p.advance()
                if p.command_type() == "C_ARITHMETIC":
                    w.writeArithmetic(p.arg1())
                elif p.command_type() in ["C_PUSH", "C_POP"]:
                    w.writePushPop(p.command_type(), p.arg1(), p.arg2())
                elif p.command_type() == "C_FUNCTION":
                    w.writeFunction(p.get_fname(), p.get_numLocals())
                elif p.command_type() == "C_RETURN":
                    w.writeReturn()
                elif p.command_type() == "C_CALL":
                    w.writeCall(p.get_fname, p.get_numLocals)
                elif p.command_type() == "C_LABEL":
                    w.writeLabel(p.get_labelname())
                elif p.command_type() == "C_GOTO":
                    w.writeGoTo(p.get_labelname())
                elif p.command_type() == "C_IF":
                    w.writeGoTo(p.get_labelname())
    else:
        print("Incorrect path.")
        sys.exit()


if __name__ == "__main__":
    main()