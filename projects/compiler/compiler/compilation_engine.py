import re
from compiler import vmwriter
from compiler import symboltable

class CompilationEngine():

    op = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']

    unary_op = ['-', '~']

    keyword_constant = ['true', 'false', 'null', 'this']

    def __init__(self, token_file, vm_file):
        self.tokens = self.get_tokens(token_file)
        self.current_token = ''
        self.idx = -1
        self.indent_level = 0
        self.current_class = ""
        self.current_function_type = ""
        self.vmwriter = vmwriter.VMWriter(vm_file)
        self.symbol_table = symboltable.SymbolTable()

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
        pass

    def write_tag(self, tag):
        pass

    def token_content(self):
        return self.current_token.split("<")[1].split(">")[-1].strip()

    def token_tag(self):
        return self.current_token.split(">")[0].split("<")[-1].strip()

    def compileClass(self):
        self.increase_indent()
        # class
        self.get_next_token()
        # className
        self.get_next_token()
        self.current_class = self.token_content()
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
        # static|field
        varkind = self.token_content()
        # type
        self.get_next_token()
        vartype = self.token_content()
        # varName
        self.get_next_token()
        varname = self.token_content()
        # add class variable to table
        self.symbol_table.define(varname, vartype, varkind)
        # check if there is comma
        self.get_next_token()
        while self.token_content() == ",":
            # varName
            self.get_next_token()
            varname = self.token_content()
            # add to table
            self.symbol_table.define(varname, vartype, varkind)
            # get next token to check if it's a comma
            self.get_next_token()
        # ;

    def compileSubroutineDec(self):
        # constructor|method|function
        # type
        self.get_next_token()
        self.current_function_type = self.token_content()
        # subroutine Name
        self.get_next_token()
        subroutine_name = self.token_content()
        # open paren
        self.get_next_token()
        # param list
        self.get_next_token()
        params = 0
        if self.token_content() != ")":
            params += self.compileParameterList()
            # params list exits with token already moved forward
        # closed paren
        self.vmwriter.writeFunction(f"{self.current_class}.{subroutine_name} {params}")
        # subroutine Body
        self.get_next_token()
        self.compileSubroutineBody()

    def compileParameterList(self):
        params = 1
        # type
        self.write_token()
        # varName
        self.get_next_token()
        self.write_token()
        # check for comma to see if more variables
        self.get_next_token()
        while self.token_content() == ",":
            params += 1
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
        return params

    def compileSubroutineBody(self):
        # clear symbol subroutine table
        self.symbol_table.startSubroutine()
        # increase the vm writer indent for easier reading
        self.vmwriter.increase_indent()
        # {
        self.write_token()
        # varDec*
        # check for var token to see if more vars declared
        self.get_next_token()
        while self.token_content() == "var":
            self.write_tag("<varDec>")
            self.increase_indent()
            # var
            varkind = self.token_content()
            # type
            self.get_next_token()
            vartype = self.token_content()
            # varName
            self.get_next_token()
            varname = self.token_content()
            # define variable in symbol token
            self.symbol_table.define(varname, vartype, varkind)
            # check for comma
            self.get_next_token()
            while self.token_content() == ",":
                # ,
                self.write_token()
                # varName
                self.get_next_token()
                varname = self.token_content()
                # check for comma
                self.symbol_table.define(varname, vartype, varkind)
                self.get_next_token()
            # ;
            # check if next keyword is var for while loop
            self.get_next_token()

        # statements
        self.compileStatements()
        # }
        self.get_next_token()
        # decrease the vm writer's indent for easier reading.
        self.vmwriter.decrease_indent()
        # close tag
        """Delete this later"""
        print(self.symbol_table)

    def compileStatements(self):
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
        # do 
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
        # return
        # get next token to check for expression
        self.get_next_token()
        if self.token_content() != ';':
            self.compileExpression()
            self.get_next_token()
        # ;
        # tag
        # Vm writer needs to write return now. Remember to push and pop for void functions.
        if self.current_function_type == "void":
            self.vmwriter.writePush("constant", "0")
            self.vmwriter.writeReturn()
            self.vmwriter.writePop("temp", "0")
        else:
            self.vmwriter.writeReturn()

    def compileExpression(self):
        # the current token is already loaded and there is no need to call get_next_token first
        self.compileTerm()
        # check for operator
        self.get_next_token()
        while self.token_content() in CompilationEngine.op:
            # op
            op = self.token_content()
            # term
            self.get_next_token()
            self.compileTerm()
            # get next token to check while loop
            # the operator has to be written at the end
            self.vmwriter.writeArithmetic(op)
            self.get_next_token()
        # must go back one token because this function is always followed by a get next token, and we've moved one token forward to check the while loop.
        self.go_back_one_token()
        self.decrease_indent()
        self.write_tag("</expression>")

    def compileExpressionList(self):
        # if current token is just closed paren, then just return
        args = 1
        if self.token_content() == ")":
            self.go_back_one_token()
            return
        # expression
        self.compileExpression()
        # check if next token is comma
        self.get_next_token()
        while self.token_content() == ",":
            args += 1
            # ,
            self.write_token()
            # expression
            self.get_next_token()
            self.compileExpression()
            # get next token to check while loop
            self.get_next_token()
        self.go_back_one_token()
        return args     

    def compileTerm(self):
        # the first term is already loaded and no need to call next_token from the start
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
            operator = self.token_content()
            # term
            self.get_next_token()
            self.compileTerm()
            # to differentiate minus vs. neg, neg will be represented as double minus sign.
            if operator == "-":
                operator = "--"
            # write the unary op at the end of the term compilation
            self.vmwriter.writeArithmetic(operator)
        elif self.token_tag() in ["integerConstant", "stringConstant", "keywordConstant"]:
            # integer constants:
            if self.token_tag() == "integerConstant":
                integer = self.token_content()
                self.vmwriter.writePush("constant", integer)
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
        # get the subroutine name. This has to be passed to vm writer's writeCall function at the end.
        subroutine_name = self.token_content()
        # initialize args to zero
        args = 0
        self.get_next_token()
        look_ahead_token = self.token_content()
        self.go_back_one_token()
        # subroutine call
        if look_ahead_token == "(":
            # subroutineName
            # (
            self.get_next_token()
            self.write_token()
            # expressionList
            self.get_next_token()
            self.write_tag("<expressionList>")
            self.increase_indent()
            args += self.compileExpressionList()
            self.decrease_indent()
            self.write_tag("</expressionList>")
            # ) 
            self.get_next_token()
            self.write_token()
        elif look_ahead_token == ".":
            # className|varName
            # .
            self.get_next_token()
            # add the dot to the method call
            subroutine_name += self.token_content()
            # subroutineName
            self.get_next_token()
            # add the actual subroutine name to the whole method call
            subroutine_name += self.token_content()
            # (
            self.get_next_token()
            self.write_token()
            # expressionList
            self.get_next_token()
            self.write_tag("<expressionList>")
            self.increase_indent()
            args += self.compileExpressionList()
            self.decrease_indent()
            self.write_tag("</expressionList>")
            # ) 
            self.get_next_token()
            self.write_token()
        # At the very end, call the subroutine with the correct number of arguments. The number of arguments depends on the amount of commas found in expression list.
        self.vmwriter.writeCall(subroutine_name, args)

    def is_valid_identifier(self):
        if self.token_content()[0].isdigit():
            return False
        if re.match(r'^[A-Za-z0-9_]+$', self.token_content()[1:]):
            return True
        



        
        

