// INIT
@256
D=A
@SP
M=D
@1
D=-A
@LCL
M=D
@2
D=-A
@ARG
M=D
@3
D=-A
@THIS
M=D
@4
D=-A
@THAT
M=D
// CALLING Sys.init 0
// Save return address
@RTN_ADDR_0__Sys.init
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save LCL segment
@LCL
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save ARG segment
@ARG
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save this
@THIS
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save that
@THAT
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Setting new ARG segment
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Jump to Sys.init
@Sys.init
0;JMP
// This is the point to return after Sys.init is called
(RTN_ADDR_0__Sys.init)
(Main.fibonacci)
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
// ***COMP_0 START***
D=M-D
@COMP_0_TRUE
D;JLT
// COMP_0_FALSE
@0
D=A
@SP
A=M
M=D
@COMP_0_END
0;JMP
(COMP_0_TRUE)
@1
D=-A
@SP
A=M
M=D
(COMP_0_END)
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
@Main.fibonacci$IF_TRUE
D;JNE
// goto
@Main.fibonacci$IF_FALSE
0;JMP
(Main.fibonacci$IF_TRUE)
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
(Main.fibonacci$IF_FALSE)
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
// CALLING Main.fibonacci 1
// Save return address
@RTN_ADDR_1__Main.fibonacci
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save LCL segment
@LCL
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save ARG segment
@ARG
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save this
@THIS
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save that
@THAT
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Setting new ARG segment
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Jump to Main.fibonacci
@Main.fibonacci
0;JMP
// This is the point to return after Main.fibonacci is called
(RTN_ADDR_1__Main.fibonacci)
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
// CALLING Main.fibonacci 1
// Save return address
@RTN_ADDR_2__Main.fibonacci
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save LCL segment
@LCL
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save ARG segment
@ARG
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save this
@THIS
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save that
@THAT
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Setting new ARG segment
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Jump to Main.fibonacci
@Main.fibonacci
0;JMP
// This is the point to return after Main.fibonacci is called
(RTN_ADDR_2__Main.fibonacci)
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
(Sys.init)
// Push constant 4
@4
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// CALLING Main.fibonacci 1
// Save return address
@RTN_ADDR_3__Main.fibonacci
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save LCL segment
@LCL
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save ARG segment
@ARG
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save this
@THIS
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Save that
@THAT
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Setting new ARG segment
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Jump to Main.fibonacci
@Main.fibonacci
0;JMP
// This is the point to return after Main.fibonacci is called
(RTN_ADDR_3__Main.fibonacci)
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
