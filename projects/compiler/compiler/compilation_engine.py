class CompilationEngine():

    op = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']

    unary_op = ['-', '~']

    keyword_constant = ['true', 'false', 'null', 'this']

    def __init__(self, token_file, xml_file):
        self.xml = xml_file
        self.tokens = self.get_tokens(token_file)
        self.current_token = ''
        self.idx = -1
        self.indent_level = 0

    def get_tokens(self, token_file):
        token_list = []
        with open(token_file) as f:
            lines = f.readlines()
            for line in lines[1:-1]:
                token_list.append(line.strip())
            return token_list

    def get_next_token(self):
        self.idx += 1
        self.current_token = self.tokens[self.idx]

    def go_back_one_token(self):
        self.idx -= 1
        self.current_token = self.tokens[self.idx]

    def increase_indent(self):
        self.indent_level += 1

    def decrease_indent(self):
        self.indent_level -= 1

    def write_token(self):
        i = 0
        while i < (self.indent_level):
            self.xml.write("  ")
            i += 1
        self.xml.write(self.current_token)
        self.xml.write("\n")

    def write_tag(self, tag):
        i = 0
        while i < (self.indent_level):
            self.xml.write("  ")
            i += 1  
        self.xml.write(tag)
        self.xml.write("\n")

    def token_content(self):
        return self.current_token.split("<")[1].split(">")[-1].strip()

    def compileClass(self):
        self.write_tag("<class>")
        self.increase_indent()
        # class
        self.get_next_token()
        self.write_token()
        # className
        self.get_next_token()
        self.write_token()
        # {
        self.get_next_token()
        self.write_token()
        # classVarDec*
        self.compileClassVarDec()
        # subroutineDec* 
        self.compileSubroutineDec()
        # }
        self.get_next_token()
        self.write_token()
        # close tag
        self.decrease_indent()
        self.write_tag("</class>")

    def compileClassVarDec(self):
        self.get_next_token()
        if self.token_content() not in ["static", "field"]:
            self.go_back_one_token()
            return
        self.write_tag("<classVarDec>")
        self.increase_indent()
        self.decrease_indent()
        self.write_tag("</classVarDec>")

    def compileSubroutineDec(self):
        self.get_next_token()
        if self.token_content() not in ["constructor", "function", "method"]:
            self.go_back_one_token()
            return
        self.write_tag("<subroutineDec>")
        self.increase_indent()
        # write constructor, function or method
        self.write_token()
        # return type
        self.get_next_token()
        self.write_token()
        # subroutine name
        self.get_next_token()
        self.write_token()
        # (
        self.get_next_token()
        self.write_token()
        # parameterList
        self.get_next_token()
        self.compileParameterList()
        # )
        self.get_next_token()
        self.write_token()
        # subroutineBody 
        self.compileSubroutineBody()
        self.decrease_indent()
        self.write_tag("</subroutineDec>")

    def compileSubroutineBody(self):
        self.write_tag("<subroutineBody>")
        self.increase_indent()
        # {
        self.get_next_token()
        self.write_token()
        # varDec*
        self.get_next_token()
        while self.token_content() == "var":
            self.compileVarDec()
            self.get_next_token()
        while self.token_content() in ["let", "if", "while", "do", "return"]:
            self.compileStatements()
        # }
        self.get_next_token()
        self.write_token()
        self.decrease_indent()
        self.write_tag("</subroutineBody>")

    def compileParameterList(self):
        self.write_tag("<parameterList>")
        self.increase_indent()
        if self.token_content() == ")":
            self.decrease_indent()
            self.write_tag("</parameterList>")
            self.go_back_one_token()
            return
        # type
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        self.get_next_token()
        while self.token_content() == ",":
            self.write_token()
            self.get_next_token()
            self.write_token()
            self.get_next_token()
        self.decrease_indent()
        self.write_tag("</parameterList>")
        self.go_back_one_token()

    def compileVarDec(self):
        self.write_tag("<varDec>")
        self.increase_indent()
        # var
        self.write_token()
        # type
        self.get_next_token()
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        # comma or semicolon
        self.get_next_token()
        while self.token_content() == ",":
            # comma
            self.write_token()
            # varName
            self.get_next_token()
            self.write_token()
            # next to see if comma
            self.get_next_token()
        # semicolon
        self.write_token()
        self.decrease_indent()
        self.write_tag("</varDec>")

    def compileStatements(self):
        self.write_tag("<statements>")
        self.increase_indent()
        if self.token_content() == "let":
            self.compileLet()
        elif self.token_content() == "if":
            self.compileIf()
        elif self.token_content() == "while":
            self.compileWhile()
        elif self.token_content() == "do":
            self.compileDo()
        elif self.token_content() == "return":
            self.compileReturn()
        self.decrease_indent()
        self.write_tag("</statements>")

    def compileDo(self):
        pass

    def compileLet(self):
        self.write_tag("<letStatement>")
        self.increase_indent()
        # let
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        # check for [expression]
        self.get_next_token()
        if self.token_content() == '[':
            self.write_token()
            self.get_next_token()
            self.compileExpression()
            self.get_next_token()
            self.write_token()
            self.get_next_token()
        # = 
        self.write_token()
        # expression
        self.compileExpression()
        # ;
        self.get_next_token()
        self.write_token()
        self.decrease_indent()
        self.write_tag("</letStatement>")

    def compileWhile(self):
        pass

    def compileReturn(self):
        pass

    def compileIf(self):
        pass

    def compileExpression(self):
        self.write_tag("<expression>")
        self.increase_indent()
        self.compileTerm()
        self.get_next_token()
        if self.token_content() in CompilationEngine.op:
            self.write_token()
            self.compileTerm()
        self.decrease_indent()
        self.write_tag("</expression>")

    def compileTerm(self):
        self.write_tag("<term>")
        self.increase_indent()
        # get next token and check if it's a unary operator
        self.get_next_token()
        if self.token_content() in CompilationEngine.unary_op:
            self.write_token()
            self.compileTerm()
        # check if it's a keyword constant
        elif self.token_content() in CompilationEngine.keyword_constant:
            pass
        # check if it's an integer constant
        elif self.token_tag() == "integerConstant":
            pass
        # check if it's a string constant
        elif self.token_tag() == "stringConstant":
            pass
        # check if it's another expression:
        elif self.token_content() == "(":
            pass
        # check if it's a subroutine call (next token is '(')

        # check if it's varName[expression] (next token is '[')

        self.decrease_indent()
        self.write_tag("</term>")

    def compileExpressionList(self):
        pass