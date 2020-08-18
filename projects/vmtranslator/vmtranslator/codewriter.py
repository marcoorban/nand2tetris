class CodeWriter():

    def __init__(self, output_file):
        self.output_file = output_file
        self.static_name = output_file.name.split("/")[-1].split(".asm")[0]
        self.comp_counter = 0
        self.returnL = 0
        self.functionLabel = 'X'

    def writeArithmetic(self, operation):
        """Arithmetic operations have two types: binary and unary. First check which type of operation it is and then execute. True is -1 and False is 0."""
        if operation not in ["neg", "not"]:
            self.decrease_stackptr()
            self.save_to_Dreg()
            self.decrease_stackptr()
            if operation in ["add","sub", "and","or"]:
                if operation == "add":
                    self.output_file.write("M=M+D\n")
                elif operation == "sub":
                    self.output_file.write("M=M-D\n")
                elif operation == "and":
                    self.output_file.write("M=M&D\n")
                elif operation == "or":
                    self.output_file.write("M=M|D\n")
            elif operation in ["eq", "gt", "lt"]:
                self.output_file.write(f"// ***COMP_{self.comp_counter} START***\n")
                self.output_file.write("D=M-D\n")
                self.output_file.write(f"@COMP_{self.comp_counter}_TRUE\n")
                if operation == "eq":
                    self.output_file.write("D;JEQ\n")
                elif operation == "gt":
                    self.output_file.write("D;JGT\n")
                elif operation == "lt":
                    self.output_file.write("D;JLT\n")
                self.output_file.write(f"// COMP_{self.comp_counter}_FALSE\n")
                self.output_file.write("@0\n")
                self.output_file.write("D=A\n")
                self.save_to_Dreg()
                self.output_file.write(f"@COMP_{self.comp_counter}_END\n")
                self.output_file.write("0;JMP\n")
                self.output_file.write(f"(COMP_{self.comp_counter}_TRUE)\n")
                self.output_file.write("@1\n")
                self.output_file.write("D=-A\n")
                self.save_to_Dreg()
                self.output_file.write(f"(COMP_{self.comp_counter}_END)\n")
                self.comp_counter += 1

        elif operation in ["neg", "not"]:
            self.decrease_stackptr()
            self.save_to_Dreg()
            if operation == "neg":
                self.neg()
            elif operation == "not":
                self.nott()
            
        self.increase_stackptr()

    def writePushPop(self, cmd_type, segment, index):
        # need to be able to differentiate between constant and non-c
        segd = {
            'local':'LCL',
            'argument': 'ARG',
            'this':'THIS',
            'that':'THAT',
            'pointer':'3',
            'temp':'5'
        }
        if segment == "constant":
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
        elif segment in ["argument", "local", "this", "that"]:
            # Calculate the destination address
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
            self.output_file.write(f"@{segd[segment]}\n")
            self.output_file.write("A=M+D\n")
        elif segment in ["pointer","temp"]:
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
            self.output_file.write(f"@R{segd[segment]}\n")
            self.output_file.write("A=A+D\n")
        elif segment == "static":
            self.output_file.write(f"@{self.static_name}.{index}\n")
            self.output_file.write("D=M\n")
            # Stack++
        
        if cmd_type == "C_PUSH":
            if segment in ["argument", "local", "this", "that"]:
                self.output_file.write("D=M\n")
            self.push_Dreg_to_stack()
            self.increase_stackptr()
            return
        elif cmd_type == "C_POP":
            if segment == "static":
                self.output_file.write(f"@{self.static_name}.{index}\n")
                self.output_file.write("D=A\n")
            # save address in register 15
            self.output_file.write("@R15\n")
            self.output_file.write("M=D\n")
            # get top of stack and save in D register
            self.decrease_stackptr()
            self.output_file.write("D=M\n")
            # go to destination
            self.output_file.write("@R15\n")
            self.output_file.write("A=M\n")
            # save D register value in destination
            self.output_file.write("M=D\n")     
            return  

    def writeInit(self):
        pass

    def writeLabel(self, label):
        self.output_file.write(f"({self.functionLabel}${label})\n")

    def writeGoTo(self, label):
        self.output_file.write(f"@{self.functionLabel}${label}\n")
        self.output_file.write("0;JMP\n")

    def writeIf(self, label):
        self.decrease_stackptr()
        self.save_to_Dreg()
        self.output_file.write(f"@{self.functionLabel}${label}\n")
        self.output_file.write("D;JNE\n")

    def writeCall(self, f, nArgs):
        # push return Address
        self.output_file.write(f"@RTN_{f}${self.returnL}")
        self.output_file.write("D=A\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # push LCL segment
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # push ARG
        self.output_file.write("@ARG\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # Push THIS
        self.output_file.write("@THIS\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # Push THAT
        self.output_file.write("@THAT\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # Set ARG segment to SP-5-nArgs
        self.output_file.write("@5\n")
        self.output_file.write("D=A\n")
        self.output_file.write(f"@{nArgs}\n")
        self.output_file.write("D=D+A\n")
        self.output_file.write("@SP\n")
        self.output_file.write("D=M-D\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")
        # Reposition LCL (LCL = SP)
        self.output_file.write("@SP\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")
        # Goto F
        self.output_file.write(f"@{f}\n")
        self.output_file.write("0;JMP\n")
        # Declare a label for the return address
        self.output_file.write(f"(RTN_{f}${self.returnL})\n")
        self.returnL += 1

    def writeReturn(self):
        # Save return address in Register 13
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@5\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@R13\n")
        self.output_file.write("M=D\n")
        # Place return value in Arg0 slot of caller
        self.decrease_stackptr()
        self.save_to_Dreg()
        self.output_file.write("@ARG\n")
        self.output_file.write("A=M\n")
        self.output_file.write("M=D\n")
        # Restore memory segments
            # Restore THAT
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@1\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@THAT\n")
        self.output_file.write("M=D\n")
            # Restore THIS
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@2\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("M=D\n")
            # Restore ARG
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@3\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")
            # Restore LCL
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@4\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")
        # Go to return address
        self.output_file.write("@R13\n")
        self.output_file.write("0;JMP\n")

    def writeFunction(self, functionName, numLocals):
        self.functionLabel = functionName
        i = 0
        self.output_file.write(f"({functionName})\n")
        while i < numLocals:
            self.output_file.write("@0\n")
            self.save_to_Dreg()
            self.push_Dreg_to_stack()
            self.increase_stackptr()
            i += 1

    def decrease_stackptr(self):
        self.output_file.write("// SP-- \n")
        self.output_file.write("@SP\n")
        self.output_file.write("AM=M-1\n")

    def increase_stackptr(self):
        self.output_file.write("// SP++\n")
        self.output_file.write("@SP\n")
        self.output_file.write("AM=M+1\n")

    def save_to_Dreg(self):
        "Saves the top of the stack to the D register"
        self.output_file.write("@SP\n")
        self.output_file.write("A=M\n")
        self.output_file.write("D=M\n")

    def push_Dreg_to_stack(self):
        self.output_file.write("// PUSH TO STACK \n")
        self.output_file.write("@SP\n")
        self.output_file.write("A=M\n")
        self.output_file.write("M=D\n")       

    def neg(self):
        self.output_file.write("M=-D\n")

    def nott(self):
        self.output_file.write("M=!D\n")

    