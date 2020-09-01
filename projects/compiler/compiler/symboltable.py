class SymbolTable():

    def __init__(self):
        self.class_table = {}
        self.subroutine_table = {}
        self.staticNo = -1
        self.fieldNo = -1
        self.argNo = -1
        self.varNo = -1

    def __repr__(self):
        return f'{self.class_table}\n{self.subroutine_table}'

    def startSubroutine(self):
        self.subroutine_table = {}
        self.argNo = -1
        self.varNo = -1

    def define(self, name, varType, kind):
        if kind == "static":
            self.staticNo += 1
            self.class_table[name] = {"type":varType, "kind":kind, "no":self.staticNo}
        elif kind == "field":
            self.fieldNo += 1
            self.class_table[name] = {"type":varType, "kind":kind, "no":self.fieldNo}
        elif kind == "var":
            self.varNo += 1
            self.subroutine_table[name] = {"type":varType, "kind":kind, "no":self.varNo}
        elif kind == "arg":
            self.argNo += 1
            self.subroutine_table[name] = {"type":varType, "kind":kind, "no":self.argNo}
        else: 
            raise ValueError("Variable kind not recognized!")

    def varCount(self, kind):
        if kind == "static":
            return self.staticNo + 1
        elif kind == "field":
            return self.fieldNo + 1
        elif kind == "var":
            return self.varNo + 1
        elif kind == "arg":
            return self.argNo + 1

    def kindOf(self, name):
        try:
            return self.subroutine_table[name]["kind"]
        except KeyError:
            try:
                return self.class_table[name]["kind"]
            except:
                return None

    def typeOf(self, name):
        try:
            return self.subroutine_table[name]["type"]
        except KeyError:
            try:
                return self.class_table[name]["type"]
            except:
                return None

    def indexOf(self, name):
        try:
            return self.subroutine_table[name]["no"]
        except KeyError:
            try:
                return self.class_table[name]["no"]
            except:
                return None

