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
// Pop local 0
@0
D=A
@LCL
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
(X$LOOP_START)
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
// Pop local 0
@0
D=A
@LCL
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
@X$LOOP_START
D;JNE
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
