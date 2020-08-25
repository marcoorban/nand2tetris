import re

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
        self.get_next_token()
        while self.token_content() in ["static", "field"]:
            self.compileClassVarDec()
            # get next token to perform the while check
            self.get_next_token()
        # subroutine Dec
        while self.token_content() in ["constructor", "function", "method"]:
            self.compileSubroutineDec()
            # get next token to perform the while check
            self.get_next_token()
        # }
        self.write_token()
        # close tag
        self.decrease_indent()
        self.write_tag("</class>")

    def compileClassVarDec(self):
        self.write_tag("<classVarDec>")
        self.increase_indent()
        # static|field
        self.write_token()
        # type
        self.get_next_token()
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        # check if there is comma
        self.get_next_token()
        while self.token_content() == ",":
            self.write_token()
            # varName
            self.get_next_token()
            self.write_token()
            # get next token to check if it's a comma
            self.get_next_token()
        # ;
        self.write_token()
        # close tag
        self.decrease_indent()
        self.write_tag("</classVarDec>")

    def compileSubroutineDec(self):
        self.write_tag("<subroutineDec>")
        self.increase_indent()
        # constructor|method|function
        self.write_token()
        # type
        self.get_next_token()
        self.write_token()
        # subroutine Name
        self.get_next_token()
        self.write_token()
        # open paren
        self.get_next_token()
        self.write_token()
        # param list
        self.write_tag("<parameterList>")
        self.increase_indent()
        self.get_next_token()
        if self.token_content() != ")":
            self.compileParameterList()
            # params list exits with token already moved forward
        self.decrease_indent()
        self.write_tag("</parameterList>")
        # closed paren
        self.write_token()
        # subroutine Body
        self.get_next_token()
        self.compileSubroutineBody()
        self.decrease_indent()
        self.write_tag("</subroutineDec>")

    def compileParameterList(self):
        # type
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        # check for comma to see if more variables
        self.get_next_token()
        while self.token_content() == ",":
            # ,
            self.write_token()
            # type
            self.get_next_token()
            self.write_token()
            # varname
            self.get_next_token()
            self.write_token()
            # check for comma
            self.get_next_token()

    def compileSubroutineBody(self):
        self.write_tag("<subroutineBody>")
        self.increase_indent()
        # {
        self.write_token()
        # varDec*
        # check for var token to see if more vars declared
        self.get_next_token()
        while self.token_content() == "var":
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
            # check for comma
            self.get_next_token()
            while self.token_content() == ",":
                # ,
                self.write_token()
                # varName
                self.get_next_token()
                self.write_token()
                # check for comma
                self.get_next_token()
            # ;
            self.write_token()
            # check if next keyword is var for while loop
            self.decrease_indent()
            self.write_tag("</varDec>")
            self.get_next_token()
        # statements
        self.compileStatements()
        # }
        self.get_next_token()
        self.write_token()
        # close tag
        self.decrease_indent() 
        self.write_tag("</subroutineBody>")

    def compileStatements(self):
        self.write_tag("<statements>")
        self.increase_indent()
        while self.token_content() in ["let", "if", "while", "do", "return"]:
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
            # get next token to keep checking while loop
            self.get_next_token()
        self.go_back_one_token()
        self.decrease_indent()
        self.write_tag("</statements>")        

    def compileLet(self):
        self.write_tag("<letStatement>")
        self.increase_indent()
        # let
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        # check for open square bracket
        self.get_next_token()
        if self.token_content() == '[':
            # [
            self.write_token()
            # expression
            self.get_next_token()
            self.compileExpression()
            # ]
            self.get_next_token()
            self.write_token()
            # go to equal sign
            self.get_next_token()
        # =
        self.write_token()
        # expression
        self.get_next_token()
        self.compileExpression()
        # ;
        self.get_next_token()
        self.write_token()
        # tag
        self.decrease_indent()
        self.write_tag("</letStatement>")

    def compileIf(self):
        self.write_tag("<ifStatement>")
        self.increase_indent()
        # if
        self.write_token()
        # open paren
        self.get_next_token()
        self.write_token()
        # expression
        self.get_next_token()
        self.compileExpression()
        # closed paren
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
        # check for else keyword
        self.get_next_token()
        look_ahead_token = self.token_content()
        self.go_back_one_token()
        if look_ahead_token == "else":
            # else
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
            # we need to go forward one so we can then go backwards one outside of if statement
        self.decrease_indent()
        self.write_tag("</ifStatement>")

    def compileWhile(self):
        self.write_tag("<whileStatement>")
        self.increase_indent()
        # while
        self.write_token()
        # open paren
        self.get_next_token()
        self.write_token()
        # expression
        self.get_next_token()
        self.compileExpression()
        # closed paren
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

    def compileDo(self):
        self.write_tag("<doStatement>")
        self.increase_indent()
        # do 
        self.write_token()
        # subroutineCall
        self.get_next_token()
        self.compileSubroutineCall()
        # ;
        self.get_next_token()
        self.write_token()
        # tag
        self.decrease_indent()
        self.write_tag("</doStatement>")

    def compileReturn(self):
        self.write_tag("<returnStatement>")
        self.increase_indent()
        # return
        self.write_token()
        # check for expression
        self.get_next_token()
        if self.token_content() != ';':
            self.compileExpression()
            self.get_next_token()
        # ;
        self.write_token()
        # tag
        self.decrease_indent()
        self.write_tag("</returnStatement>")

    def compileExpression(self):
        # the current token is already loaded and there is no need to call get_next_token first
        self.write_tag("<expression>")
        self.increase_indent()
        self.compileTerm()
        # check for operator
        self.get_next_token()
        while self.token_content() in CompilationEngine.op:
            # op
            self.write_token()
            # term
            self.get_next_token()
            self.compileTerm()
            # get next token to check while loop
            self.get_next_token()
        # must go back one token because this function is always followed by a get next token, and we've moved one token forward to check the while loop.
        self.go_back_one_token()
        self.decrease_indent()
        self.write_tag("</expression>")

    def compileExpressionList(self):
        # if current token is just closed paren, then just return
        if self.token_content() == ")":
            self.go_back_one_token()
            return
        # expression
        self.compileExpression()
        # check if next token is comma
        self.get_next_token()
        while self.token_content() == ",":
            # ,
            self.write_token()
            # expression
            self.get_next_token()
            self.compileExpression()
            # get next token to check while loop
            self.get_next_token()
        self.go_back_one_token()        

    def compileTerm(self):
        # the first term is already loaded and no need to call next_token from the start
        self.write_tag("<term>")
        self.increase_indent()
        # need to look ahead one token to determine if it's a case of varName[expression] or subroutineName(expression)|className.subroutineName(Expression)
        self.get_next_token()
        look_ahead_token = self.token_content()
        self.go_back_one_token()
        if look_ahead_token in ['[', '(', '.'] and self.is_valid_identifier():
            if look_ahead_token == '[':
                # varName[expression]
                # varname
                self.write_token()
                # [
                self.get_next_token()
                self.write_token()
                # expression
                self.get_next_token()
                self.compileExpression()
                # ]
                self.get_next_token()
                self.write_token()
            else:
                self.compileSubroutineCall()
 
        elif self.token_content() in CompilationEngine.unary_op:
            # unary op
            self.write_token()
            # term
            self.get_next_token()
            self.compileTerm()
        elif self.token_tag() in ["integerConstant", "stringConstant", "keywordConstant"]:
            # constant
            self.write_token()
        elif self.token_content() == "(":
            # (
            self.write_token()
            # expression
            self.get_next_token()
            self.compileExpression()
            # )
            self.get_next_token()
            self.write_token()
        else:
            #varname
            self.write_token()
        self.decrease_indent()
        self.write_tag("</term>")

    def compileSubroutineCall(self):
        self.get_next_token()
        look_ahead_token = self.token_content()
        self.go_back_one_token()
        # subroutine call
        if look_ahead_token == "(":
            # subroutineName
            self.write_token()
            # (
            self.get_next_token()
            self.write_token()
            # expressionList
            self.get_next_token()
            self.write_tag("<expressionList>")
            self.increase_indent()
            self.compileExpressionList()
            self.decrease_indent()
            self.write_tag("</expressionList>")
            # ) 
            self.get_next_token()
            self.write_token()
        elif look_ahead_token == ".":
            # className|varName
            self.write_token()
            # .
            self.get_next_token()
            self.write_token()
            # subroutineName
            self.get_next_token()
            self.write_token()
            # (
            self.get_next_token()
            self.write_token()
            # expressionList
            self.get_next_token()
            self.write_tag("<expressionList>")
            self.increase_indent()
            self.compileExpressionList()
            self.decrease_indent()
            self.write_tag("</expressionList>")
            # ) 
            self.get_next_token()
            self.write_token()

    def is_valid_identifier(self):
        if self.token_content()[0].isdigit():
            return False
        if re.match(r'^[A-Za-z0-9_]+$', self.token_content()[1:]):
            return True
        



        
        

