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

    def token_tag(self):
        return self.current_token.split(">")[0].split("<")[-1].strip()

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

        self.compileStatements()
 
        # }
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
        while self.token_content() in ["let", "if", "while", "do", "return"]:
            if self.token_content() == "let":
                self.compileLet()
                self.get_next_token()
            elif self.token_content() == "if":
                self.compileIf()
                self.get_next_token()
            elif self.token_content() == "while":
                self.compileWhile()
                self.get_next_token()
            elif self.token_content() == "do":
                self.compileDo()
                self.get_next_token()
            elif self.token_content() == "return":
                self.compileReturn()
                self.get_next_token()
        self.go_back_one_token()
        self.decrease_indent()
        self.write_tag("</statements>")

    def compileDo(self):
        self.write_tag("<doStatement>")
        self.increase_indent()
        # do
        self.write_token()
        self.compileSubroutineCall()
        # ;
        self.get_next_token()
        self.write_token()
        # close tag
        self.decrease_indent()
        self.write_tag("</doStatement>")

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

            self.compileExpression()
            # ]
            self.get_next_token()
            self.write_token()
            # get ready for =
            self.get_next_token()
        # = 
        self.write_token()
        # expression
        self.compileExpression()
        # ;
        self.get_next_token()
        self.write_token()
        # close tag
        self.decrease_indent()
        self.write_tag("</letStatement>")

    def compileWhile(self):
        self.write_tag("<whileStatement>")
        self.increase_indent()
        # while
        self.write_token()
        # ( 
        self.get_next_token()
        self.write_token()
        # expression
        self.compileExpression()
        # )
        self.get_next_token()
        self.write_token()
        # {
        self.get_next_token()
        self.write_token()
        # statements 
        self.get_next_token()
        self.compileStatements()
        # } 
        self.get_next_token()
        self.write_token()
        self.decrease_indent()
        self.write_tag("</whileStatement>")

    def compileReturn(self):
        self.write_tag("<returnStatement>")
        self.increase_indent()
        # return
        self.write_token()
        # check if semicolon -> if not, then expression
        self.get_next_token()
        if self.token_content() != ";":
            self.compileExpression()
            self.get_next_token()
        # ;
        self.write_token()
        self.decrease_indent()
        self.write_tag("</returnStatement>")

    def compileIf(self):
        self.write_tag("<ifStatement>")
        self.increase_indent()
        # if
        self.write_token()
        # (
        self.get_next_token()
        self.write_token()
        # expression
        self.compileExpression()
        # )
        self.get_next_token()
        self.write_token()
        # {
        self.get_next_token()
        self.write_token()
        # statements
        self.compileStatements()
        # }
        self.get_next_token()
        self.write_token()
        # (else {statements} )?
        self.get_next_token()
        if self.token_content() == "else":
            # else
            self.write_token()
            # {
            self.get_next_token()
            self.write_token()
            # statements 
            self.compileStatements()
            # }
            self.get_next_token()
            self.write_token()
        # if there wasn't an else keyword, then go back to previous token.
        else:
            self.go_back_one_token()
        self.decrease_indent()
        self.write_tag("</ifStatement>")

    def compileExpression(self):
        self.write_tag("<expression>")
        self.increase_indent()
        self.compileTerm()
        self.get_next_token()
        if self.token_content() in CompilationEngine.op:
            self.write_token()
            self.compileTerm()
        else:
            self.go_back_one_token()
        self.decrease_indent()
        self.write_tag("</expression>")

    def compileTerm(self):
        self.write_tag("<term>")
        self.increase_indent()
        # get next token and check if it's a unary operator
        self.get_next_token()

        # save the next next token in a variable, then go back to where we were
        self.get_next_token()
        next_token = self.token_content()
        self.go_back_one_token()
        #### 

        if self.token_content() in CompilationEngine.unary_op:
            self.write_token()
            self.compileTerm()
        # check if it's a keyword constant
        elif self.token_content() in CompilationEngine.keyword_constant:
            self.write_token()
        # check if it's an integer constant
        elif self.token_tag() == "integerConstant":
            self.write_token()
        # check if it's a string constant
        elif self.token_tag() == "stringConstant":
            self.write_token()
        # check if it's another expression:
        elif self.token_content() == "(":
            self.compileExpression()
        # check if it's a subroutine call (next token is '(')
        elif next_token in ["(", "[", "."]:
            if next_token in ["(", "."]:
                self.compileSubroutineCall()
            # check if it's varName[expression] (next token is '[')
            elif next_token == "[":
                #varName[ expression ]
                # write varname
                self.write_token()
                # write [
                self.get_next_token()
                self.write_token()
                # compile expression
                self.compileExpression()
                # write ]
                self.get_next_token()
                self.write_token()
        # If all of the above cases fail, then it's just a varname and we can just write it down
        else:
            # Need to go back one token because it was moved forward to see if there was an open paren or bracket in the comparison above.
            self.write_token()
        # Remove indentation and close brackets and return
        self.decrease_indent()
        self.write_tag("</term>")
        return 

    def compileExpressionList(self):
        self.write_tag("<expressionList>")
        self.increase_indent()
        self.compileExpression()
        while self.token_content() == ",":
            self.write_token()
            self.compileExpression()
        self.decrease_indent()
        self.write_tag("</expressionList>")

    def compileSubroutineCall(self):
        # current token is either on the open paren or dot
        self.get_next_token()
        if self.token_content() == "(":
            self.go_back_one_token()
            self.write_token()
            # (
            self.get_next_token()
            self.write_token()
            # expressionList, but only call if next token is not closed paren
            self.get_next_token()
            if self.token_content() != ")":
                self.go_back_one_token()
                self.compileExpressionList()
                self.get_next_token()
            # )
            self.write_token()
            return
        elif self.token_content() == ".":
            # className | varName
            self.go_back_one_token()
            self.write_token()
            # .
            self.get_next_token()
            self.write_token()
            # subroutine Name
            self.get_next_token()
            self.write_token()
            # (
            self.get_next_token()
            self.write_token()
            # expressionList, but only call if next token is not a closed parenthesis
            self.get_next_token()
            if self.token_content() != ")":
                self.go_back_one_token()
                self.compileExpressionList()
            # ) 
            self.get_next_token()
            self.write_token()
            return