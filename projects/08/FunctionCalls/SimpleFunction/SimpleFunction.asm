(SimpleFunction.test)
@0
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@0
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push local 0
@0
D=A
@LCL
A=M+D
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push local 1
@1
D=A
@LCL
A=M+D
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// SP-- 
@SP
AM=M-1
@SP
A=M
D=M
// SP-- 
@SP
AM=M-1
M=M+D
// SP++
@SP
AM=M+1
// SP-- 
@SP
AM=M-1
@SP
A=M
D=M
M=!D
// SP++
@SP
AM=M+1
// Push argument 0
@0
D=A
@ARG
A=M+D
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// SP-- 
@SP
AM=M-1
@SP
A=M
D=M
// SP-- 
@SP
AM=M-1
M=M+D
// SP++
@SP
AM=M+1
// Push argument 1
@1
D=A
@ARG
A=M+D
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// SP-- 
@SP
AM=M-1
@SP
A=M
D=M
// SP-- 
@SP
AM=M-1
M=M-D
// SP++
@SP
AM=M+1
// RETURN
// Save return address 
@LCL
D=M
@5
A=D-A
D=M
@R13
M=D
// SP-- 
@SP
AM=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@LCL
D=M
@1
A=D-A
D=M
@THAT
M=D
@LCL
D=M
@2
A=D-A
D=M
@THIS
M=D
@LCL
D=M
@3
A=D-A
D=M
@ARG
M=D
@LCL
D=M
@4
A=D-A
D=M
@LCL
M=D
@R13
A=M
0;JMP
