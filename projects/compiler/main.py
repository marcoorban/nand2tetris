import sys
import pathlib
from os import listdir
from os.path import join, isfile, splitext
from compiler import tokenizer, compilation_engine

jack_folder_path = pathlib.Path(sys.argv[1])
jack_files = [join(jack_folder_path, f) for f in listdir(jack_folder_path) if (isfile(join(jack_folder_path, f)) and splitext(f)[1] == '.jack')]

for jack_file in jack_files:
    # Creating the token files
    t = tokenizer.Tokenizer(jack_file)
    token_file = jack_file.replace(".jack", "T2.xml")
    with open(token_file, "w") as f:
        f.write("<tokens>\n")
        while t.hasMoreTokens():
            t.advance()
            if t.tokenType() == "KEYWORD":
                token = f"<keyword> {t.current_token} </keyword>"
            elif t.tokenType() == "SYMBOL":
                tk = t.current_token
                if tk == "<":
                    tk = "&lt;"
                elif tk == ">":
                    tk = "&gt;"
                elif tk == "&":
                    tk = "&amp;"
                token = f"<symbol> {tk} </symbol>"
            elif t.tokenType() == "IDENTIFIER":
                token = f"<identifier> {t.current_token} </identifier>"
            elif t.tokenType() == "INT_CONST":
                token = f"<integerConstant> {t.current_token} </integerConstant>"
            elif t.tokenType() == "STRING_CONST":
                tk = t.current_token.replace('"', "")
                token = f"<stringConstant> {tk} </stringConstant>"

            f.write(token + "\n")
        f.write("</tokens>\n")

    # Creating the code xml files

token_files  = [join(jack_folder_path, f) for f in listdir(jack_folder_path) if (isfile(join(jack_folder_path, f)) and "T2.xml" in str(f))]
print(token_files)

for token_file in token_files:
    xml_file = token_file.replace("T2.xml", "2.xml")
    with open(xml_file, "w") as xml:
        e = compilation_engine.CompilationEngine(token_file, xml)
        e.compileClass()


