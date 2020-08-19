@3030
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
@R3
D=A+D
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@3040
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@1
D=A
@R3
D=A+D
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@32
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@2
D=A
@THIS
D=D+M
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@46
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@6
D=A
@THAT
D=D+M
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@0
D=A
@R3
A=A+D
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@1
D=A
@R3
A=A+D
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
@2
D=A
@THIS
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
@6
D=A
@THAT
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
