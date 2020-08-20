class CompilationEngine():

    def __init__(self, token_file, xml_file):
        self.f = xml_file
        self.tokens = self.get_tokens(token_file)
        self.current_token = ''
        self.idx = -1

    def get_tokens(self, token_file):
        token_list = []
        with open(token_file) as f:
            lines = f.readlines()
            for line in lines[1:-1]:
                line = line.split("<")[1].split(">")[1].strip()
                token_list.append(line)
            self.get_next_token()
            return token_list

    def get_next_token(self):
        self.idx += 1
        self.current_token = self.tokens[self.idx]
    
    def compileClass(self):
        self.f.write("this!")

    def compileClassVarDec(self):
        pass

    def compileSubroutine(self):
        pass

    def compilerParemeterList(self):
        pass

    def compileVarDec(self):
        pass

    def compileStatements(self):
        pass

    def compileDo(self):
        pass

    def compileLet(self):
        pass

    def compileWhile(self):
        pass

    def compileReturn(self):
        pass

    def compileIf(self):
        pass

    def compileExpression(self):
        pass

    def compileTerm(self):
        pass

    def compileExpressionList(self):
        pass