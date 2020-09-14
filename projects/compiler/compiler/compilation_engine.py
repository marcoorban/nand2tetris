import re
import sys
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
        self.current_class = ""
        self.ftype = ""
        self.returntype = ""
        self.labelno = -1
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

    def write_token(self):
        pass

    def write_tag(self, tag):
        pass

    def token_content(self):
        return self.current_token.split("<")[1].split(">")[-1].strip()

    def token_tag(self):
        return self.current_token.split(">")[0].split("<")[-1].strip()

    def compileClass(self):
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
        # erase the symbol table and start a new one
        self.symbol_table.startSubroutine()
        # constructor|method|function
        # type
        self.ftype = self.token_content()
        self.get_next_token()
        self.returntype = self.token_content()
        # subroutine Name
        self.get_next_token()
        subroutine_name = self.token_content()
        self.vmwriter.writeComment(f"START OF {self.current_class}.{subroutine_name}")
        # open paren
        self.get_next_token()
        # param list
        self.get_next_token()
        params = 0
        # If the current function is a method, then arg[0] should be assigned to THIS, which is the address of the current object.
        if self.ftype == "method":
            self.symbol_table.define("this", f"{self.current_class}", "arg")
            params += 1

        if self.token_content() != ")":
            params += self.compileParameterList()
            # params list exits with token already moved forward
        # closed paren
        # subroutine Body
        self.get_next_token()
        self.compileSubroutineBody(f"{self.current_class}.{subroutine_name}")

    def compileParameterList(self):
        params = 1
        # type
        varType = self.token_content()
        # varName
        self.get_next_token()
        varName = self.token_content()
        # add to symbol table
        self.symbol_table.define(varName, varType, "arg")
        # check for comma to see if more variables
        self.get_next_token()
        while self.token_content() == ",":
            params += 1
            # ,
            # type
            self.get_next_token()
            varType = self.token_content()
            # varname
            self.get_next_token()
            varName = self.token_content()
            # add to symbol table
            self.symbol_table.define(varName, varType, "arg")
            # check for comma
            self.get_next_token()
        return params

    def compileSubroutineBody(self, fname):
        # clear symbol subroutine table
        # increase the vm writer indent for easier reading
        # {
        self.write_token()
        # varDec*
        # check for var token to see if more vars declared
        self.get_next_token()
        # Adding variables to the symbol table
        while self.token_content() == "var":
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
        # Now that the symbol table has been created, the vmwriter can write function (function name) (no of local vars)
        self.vmwriter.writeFunction(fname, self.symbol_table.varCount("var"))
        # if the subroutine is a constructor, push number of args and call Alloc.
        if self.ftype == "constructor":
            size = self.symbol_table.varCount("field")
            self.vmwriter.writePush(f"constant", f"{size}")
            self.vmwriter.writeCall("Memory.alloc", "1")
            self.vmwriter.writePop("pointer", "0")
        # if the subroutine is a method, then push argument 0 (the address of the object) and pop it into pointer 0 so that the this segment can be aligned with the start of the object.
        elif self.ftype == "method":
            self.vmwriter.writePush("argument", "0")
            self.vmwriter.writePop("pointer", "0")
        # statements
        self.compileStatements()
        # }
        self.get_next_token()

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

    def compileLet(self):
        # let
        # varName
        self.get_next_token()
        varName = self.token_content()
        # check if the variable exists in the symbol table. If it doesn't exist, then raise an error.
        if not self.symbol_table.segmentOf(varName):
            sys.exit(f"Compiler error: variable {self.token_content()} referenced before initialized.")
        # check for open square bracket
        self.get_next_token()
        if self.token_content() == '[':
            # [
            # expression
            self.get_next_token()
            self.compileExpression()
            # ]
            self.get_next_token()
            # go to equal sign
            self.get_next_token()
        # =
        # expression
        self.get_next_token()
        self.compileExpression()
        # after Expression is compiled, push the value to the variable
        self.vmwriter.writePop(self.symbol_table.segmentOf(varName), self.symbol_table.indexOf(varName))
        # ;
        self.get_next_token()
        # tag

    def compileIf(self):
        self.labelno += 1
        label = self.labelno
        L1 = f"IF_FALSE{label}"
        L2 = f"IF_TRUE{label}"
        # if
        # open paren
        self.get_next_token()
        # COMPILED EXPRESSION
        # expression
        self.get_next_token()
        self.compileExpression()
        # closed paren
        # NOT
        self.vmwriter.writeArithmetic("~")
        # IF_GOTO L1
        self.vmwriter.writeIf(L1)
        self.get_next_token()
        # {
        self.get_next_token()
        # COMPILED STATEMENTS
        # statements
        self.get_next_token()
        self.compileStatements()
        # }
        # GOTO L2
        self.vmwriter.writeGoto(L2)
        self.get_next_token()
        # check for else keyword
        self.get_next_token()
        look_ahead_token = self.token_content()
        self.go_back_one_token()
        self.vmwriter.writeLabel(L1)
        # COMPILE ELSE STATEMENTS (IF THERE'S ANY)
        if look_ahead_token == "else":
            # else
            self.get_next_token()
            # {
            self.get_next_token()
            # statements
            self.get_next_token()
            self.compileStatements()
            # }
            self.get_next_token()
        # LABEL 2 AND CONTINUE EXECUTION OF THE CODE
        self.vmwriter.writeLabel(L2)

    def compileWhile(self):
        self.labelno += 1
        label = str(self.labelno)
        L1 = f"WHILE_FALSE{label}"
        L2 = f"WHILE_TRUE{label}"
        # while
        # LABEL L1
        self.vmwriter.writeLabel(L1)
        # open paren
        self.get_next_token()
        # STATEMENTS
        # expression
        self.get_next_token()
        self.compileExpression()
        # closed paren
        self.get_next_token()
        # NEGATE AND IF-GOTO L2
        self.vmwriter.writeArithmetic("~")
        self.vmwriter.writeIf(L2)
        # STATEMENTS AGAIN
        # {
        self.get_next_token()
        # statements
        self.get_next_token()
        self.compileStatements()
        # }
        # GOTO L1
        self.vmwriter.writeGoto(L1)
        self.get_next_token()
        self.vmwriter.writeLabel(L2)
        self.labelno += 1

    def compileDo(self):
        # do 
        # subroutineCall
        self.get_next_token()
        self.compileSubroutineCall()
        # ;
        self.get_next_token()
        self.write_token()
        # tag

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
        if self.returntype == "void":
            self.vmwriter.writePush("constant", "0")
            self.vmwriter.writeReturn()
            self.vmwriter.writePop("temp", "0")
        # If the function is a constructor, we need to push pointer 0 to the stack, since this is the address of the object that must be returned to the caller
        elif self.ftype == "constructor":
            self.vmwriter.writePush("pointer", "0")
            self.vmwriter.writeReturn()
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

    def compileExpressionList(self):
        # if current token is just closed paren, then just return
        args = 0
        if self.token_content() == ")":
            self.go_back_one_token()
            return args
        args += 1
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
        elif self.token_tag() in ["integerConstant", "stringConstant", "keyword"]:
            # integer constants:
            if self.token_tag() == "integerConstant":
                integer = self.token_content()
                self.vmwriter.writePush("constant", integer)
            # keyworkConstants:
            if self.token_content() in ["null", "false"]:
                self.vmwriter.writePush("constant", "0")
            elif self.token_content() == "true":
                self.vmwriter.writePush("constant", "1")
                self.vmwriter.writeArithmetic("--")
            elif self.token_content() == "this":
                self.vmwriter.writePush("argument", "0")
        elif self.token_content() == "(":
            # (
            # expression
            self.get_next_token()
            self.compileExpression()
            # )
            self.get_next_token()
        # If none of the above work, then the current token is a variable and should be looked up in the symbol table, and then pushed
        else:
            #varname
            segment = self.symbol_table.segmentOf(self.token_content())
            index = self.symbol_table.indexOf(self.token_content())
            self.vmwriter.writePush(segment, index)
            self.write_token()

    def compileSubroutineCall(self):
        # get the subroutine name. This has to be passed to vm writer's writeCall function at the end.
        callLabel = ""
        subroutine_name = self.token_content()
        # initialize args to zero
        args = 0
        self.get_next_token()
        look_ahead_token = self.token_content()
        self.go_back_one_token()
        # subroutine call
        if look_ahead_token == "(":
            callLabel = self.current_class + '.' + subroutine_name
            # subroutineName
            # (
            self.get_next_token()
            # expressionList
            self.get_next_token()
            args += self.compileExpressionList()
            # ) 
            self.get_next_token()
            # push the value of THIS (pointer 0) to the stack
            self.vmwriter.writePush("pointer", "0")
            args += 1
        elif look_ahead_token == ".":
            # className|varName
            # First we have to determine what class of object it is
            class_name = self.token_content()
            objectName = class_name
            callLabel += class_name
            # .
            self.get_next_token()
            # add the dot to the method call
            callLabel += self.token_content()
            # subroutineName
            self.get_next_token()
            subroutine_name = self.token_content()
            # add the actual subroutine name to the whole method call
            callLabel += subroutine_name
            # (
            self.get_next_token()
            # expressionList
            self.get_next_token()
            args += self.compileExpressionList()
            # ) 
            self.get_next_token()

        # The following code runs if the current subroutine call is a method of an existing object. If so, then the first argument passed should be the memory location of the object, which is saved in the variable that it has been assigned to. The way the compiler knows if it's a method is by checking if the current object actually exists. Otherwise, it's just a function of an existing class, this piece of code won't run, and the label and arguments will be the ones set in the code that goes before this section.
            if self.symbol_table.segmentOf(objectName):
                callLabel = self.symbol_table.typeOf(objectName) + "." + subroutine_name
                self.vmwriter.writePush(self.symbol_table.segmentOf(objectName), self.symbol_table.indexOf(objectName))
                args += 1

        self.vmwriter.writeCall(callLabel, args)

    def is_valid_identifier(self):
        if self.token_content()[0].isdigit():
            return False
        if re.match(r'^[A-Za-z0-9_]+$', self.token_content()[1:]):
            return True

    def add_to_symbol_table(self):

        return

        



        
        

