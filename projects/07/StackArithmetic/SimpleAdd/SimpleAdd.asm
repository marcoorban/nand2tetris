@7
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@8
D=A
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
