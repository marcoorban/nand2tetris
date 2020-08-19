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
// Pop pointer 1
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
// Push constant 0
@0
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop that 0
@0
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
// Push constant 1
@1
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop that 1
@1
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
// Push constant 2
@2
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
M=M-D
// SP++
@SP
AM=M+1
// Pop argument 0
@0
D=A
@ARG
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
(X$MAIN_LOOP_START)
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
// If goto
// SP-- 
@SP
AM=M-1
@SP
A=M
D=M
@X$COMPUTE_ELEMENT
D;JNE
// goto
@X$END_PROGRAM
0;JMP
(X$COMPUTE_ELEMENT)
// Push that 0
@0
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
// Push that 1
@1
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
// Pop that 2
@2
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
// Push pointer 1
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
// Push constant 1
@1
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
// Pop pointer 1
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
// Push constant 1
@1
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
M=M-D
// SP++
@SP
AM=M+1
// Pop argument 0
@0
D=A
@ARG
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
// goto
@X$MAIN_LOOP_START
0;JMP
(X$END_PROGRAM)
