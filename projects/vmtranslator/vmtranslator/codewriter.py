class CodeWriter():

    segments = {
        'local':'LCL',
        'argument': 'ARG',
        'this':'THIS',
        'that':'THAT',
        'pointer':'3',
        'temp':'5'
    }

    def __init__(self, output_file):
        self.output_file = output_file
        self.static_name = ""
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
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=D\n")
                self.output_file.write(f"@COMP_{self.comp_counter}_END\n")
                self.output_file.write("0;JMP\n")
                self.output_file.write(f"(COMP_{self.comp_counter}_TRUE)\n")
                self.output_file.write("@1\n")
                self.output_file.write("D=-A\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=D\n")
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

    def writePush(self, segment, index):
        # need to be able to differentiate between constant and non-c
        self.output_file.write(f"// Push {segment} {index}\n")
        if segment == "constant":
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
        elif segment in ["argument", "local", "this", "that"]:
            # Calculate the destination address
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
            self.output_file.write(f"@{CodeWriter.segments[segment]}\n")
            # Go to destination address
            self.output_file.write("A=M+D\n")
            # Save destination address to D register
            self.output_file.write("D=M\n")
        elif segment in ["pointer", "temp"]:
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
            self.output_file.write(f"@R{CodeWriter.segments[segment]}\n")
            # Save destination address to D register
            self.output_file.write("A=A+D\n")
            self.output_file.write("D=M\n")
        elif segment == "static":
            self.output_file.write(f"@{self.static_name}.{index}\n")
            self.output_file.write("D=M\n")
        
        # Push D to stack and SP++
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        
    def writePop(self, segment, index):
        self.output_file.write(f"// Pop {segment} {index}\n")
        if segment in ["argument", "local", "this", "that"]:
            # Calculate destination address
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
            self.output_file.write(f"@{CodeWriter.segments[segment]}\n")
            self.output_file.write("D=D+M\n")
        elif segment in ["pointer", "temp"]:
            self.output_file.write(f"@{index}\n")
            self.output_file.write("D=A\n")
            self.output_file.write(f"@R{CodeWriter.segments[segment]}\n")
            # Save destination address to D register
            self.output_file.write("D=A+D\n")
        elif segment == "static":
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
        #Initialize stack pointer
        self.output_file.write("// INIT\n")
        self.output_file.write("@256\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=D\n")
        # Initiliaze LCL, ARG, THIS, THAT to -1, -2, -3, -4
        self.output_file.write("@1\n")
        self.output_file.write("D=-A\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")
        self.output_file.write("@2\n")
        self.output_file.write("D=-A\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")
        self.output_file.write("@3\n")
        self.output_file.write("D=-A\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("M=D\n")
        self.output_file.write("@4\n")
        self.output_file.write("D=-A\n")
        self.output_file.write("@THAT\n")
        self.output_file.write("M=D\n")
        # Call init()
        self.writeCall('Sys.init', '0')

    def writeLabel(self, label):
        self.output_file.write(f"({self.functionLabel}${label})\n")

    def writeGoTo(self, label):
        self.output_file.write("// goto\n")
        self.output_file.write(f"@{self.functionLabel}${label}\n")
        self.output_file.write("0;JMP\n")

    def writeIf(self, label):
        self.output_file.write("// If goto\n")
        self.decrease_stackptr()
        self.save_to_Dreg()
        self.output_file.write(f"@{self.functionLabel}${label}\n")
        self.output_file.write("D;JNE\n")

    def writeCall(self, f, nArgs):
        self.output_file.write(f"// CALLING {f} {nArgs}\n")
        # push return Address
        self.output_file.write("// Save return address\n")
        self.output_file.write(f"@RTN_ADDR_{self.returnL}__{f}\n")
        self.output_file.write("D=A\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # push LCL segment
        self.output_file.write("// Save LCL segment\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # push ARG
        self.output_file.write("// Save ARG segment\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # Push THIS
        self.output_file.write("// Save this\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # Push THAT
        self.output_file.write("// Save that\n")
        self.output_file.write("@THAT\n")
        self.output_file.write("D=M\n")
        self.push_Dreg_to_stack()
        self.increase_stackptr()
        # Set ARG segment to SP-5-nArgs
        self.output_file.write("// Setting new ARG segment\n")
        self.output_file.write("@5\n")
        self.output_file.write("D=A\n")
        self.output_file.write(f"@{nArgs}\n")
        self.output_file.write("D=D+A\n")
        self.output_file.write("@SP\n")
        self.output_file.write("D=M-D\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")
        # Reposition LCL (LCL = SP)
        self.output_file.write("// Reposition LCL\n")
        self.output_file.write("@SP\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")
        # Goto F
        self.output_file.write(f"// Jump to {f}\n")
        self.output_file.write(f"@{f}\n")
        self.output_file.write("0;JMP\n")
        # Declare a label for the return address
        self.output_file.write(f"// This is the point to return after {f} is called\n")
        self.output_file.write(f"(RTN_ADDR_{self.returnL}__{f})\n")
        self.returnL += 1

    def writeReturn(self):
        self.output_file.write("// RETURN\n")
        # Save return address in Register 13
        self.output_file.write("// Save return address \n")
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
        # Move Stack pointer to RAM[Arg0 + 1]
        self.output_file.write("@ARG\n")
        self.output_file.write("D=M+1\n")
        self.output_file.write("@SP\n")
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
        self.output_file.write("A=M\n")
        self.output_file.write("0;JMP\n")

    def writeFunction(self, functionName, numLocals):
        self.functionLabel = functionName
        i = 0
        self.output_file.write(f"({functionName})\n")
        while i < int(numLocals):
            self.output_file.write("@0\n")
            self.output_file.write("D=A\n")
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

    