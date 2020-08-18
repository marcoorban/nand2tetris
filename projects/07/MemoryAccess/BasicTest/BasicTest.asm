@10
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
@LCL
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
@21
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@22
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
@ARG
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
@1
D=A
@ARG
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
@36
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
@42
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@45
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@5
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
@2
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
@510
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
@5
D=A+D@R16
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
@LCL
D=M+D
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@5
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
@1
D=A
@ARG
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
@THIS
D=M+D
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@6
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
// SP-- 
@SP
AM=M-1
M=M-D
// SP++
@SP
AM=M+1
@6
D=A
@5
D=A+D// PUSH TO STACK 
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
