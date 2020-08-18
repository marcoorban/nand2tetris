@111
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@333
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@888
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@StaticTest.8
D=M
@StaticTest.8
D=A
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@StaticTest.3
D=M
@StaticTest.3
D=A
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@StaticTest.1
D=M
@StaticTest.1
D=A
@R15
M=D
// SP-- 
@SP
AM=M-1
D=M
@R15
A=M
M=D
@StaticTest.3
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
@StaticTest.1
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
@StaticTest.8
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
