class VMWriter():

    def __init__(self, vm_file):
        self.vm = vm_file

    def writePush(self, segment, index):
        self.vm.write(f"push {segment} {index}\n")

    def writePop(self, segment, index):
        self.vm.write(f"pop {segment} {index}\n")

    def writeArithmetic(self, command):
        self.vm.write(f"{command}\n")

    def writeLabel(self, label):
        self.vm.write(f"label {label}\n")

    def writeGoto(self, label):
        self.vm.write(f"goto {label}\n")

    def writeIf(self, label):
        self.vm.write(f"if-goto {label}\n")

    def writeCall(self, label):
        self.vm.write(f"call {label}\n")

    def writeFunction(self, label):
        self.vm.write(f"function {label}\n")

    def writeReturn(self):
        self.vm.write(f"return\n")

