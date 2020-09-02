OPERATORS = {
    "+":"add",
    "-":"sub",
    "*":"call Math.multiply 2",
    "/":"call Math.divide 2",
    "&amp":"and",
    "|":"or",
    "&lt":"lt",
    "&gt":"gt",
    "=":"eq",
    "--":"neg",
    "~":"not"
}

class VMWriter():

    def __init__(self, vm_file):
        self.vm = vm_file
        self.indent_level = 0

    def increase_indent(self):
        self.indent_level += 1

    def decrease_indent(self):
        self.indent_level -= 1

    def writePush(self, segment, index):
        self.writex(f"push {segment} {index}\n")

    def writePop(self, segment, index):
        self.writex(f"pop {segment} {index}\n")

    def writeArithmetic(self, operator):
        self.writex(f"{OPERATORS[operator]}\n")

    def writeLabel(self, label):
        self.writex(f"label {label}\n")

    def writeGoto(self, label):
        self.writex(f"goto {label}\n")

    def writeIf(self, label):
        self.writex(f"if-goto {label}\n")

    def writeCall(self, label, args):
        self.writex(f"call {label} {args}\n")

    def writeFunction(self, label):
        self.writex(f"function {label}\n")

    def writeReturn(self):
        self.writex(f"return\n")

    def writex(self, content):
        spaces = "  " * self.indent_level
        self.vm.write(f"{spaces}{content}" )

