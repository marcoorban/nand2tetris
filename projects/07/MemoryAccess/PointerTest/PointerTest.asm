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
A=A+D
D=M
@R16
M=D
// SP-- 
@SP
AM=M-1
D=M
@R16
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
A=A+D
D=M
@R16
M=D
// SP-- 
@SP
AM=M-1
D=M
@R16
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
D=M+D
@R16
M=D
// SP-- 
@SP
AM=M-1
D=M
@R16
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
D=M+D
@R16
M=D
// SP-- 
@SP
AM=M-1
D=M
@R16
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
D=M+D
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
D=M+D
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
