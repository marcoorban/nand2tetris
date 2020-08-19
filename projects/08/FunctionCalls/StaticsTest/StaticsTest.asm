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
(Class1.set)
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
// Pop static 0
@Class1.0
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
// Pop static 1
@Class1.1
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
(Class1.get)
// Push static 0
@Class1.0
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push static 1
@Class1.1
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
(Class2.set)
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
// Pop static 0
@Class2.0
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
// Pop static 1
@Class2.1
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
(Class2.get)
// Push static 0
@Class2.0
D=M
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push static 1
@Class2.1
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
(Sys.init)
// Push constant 6
@6
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push constant 8
@8
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// CALLING Class1.set 2
// Save return address
@RTN_ADDR_1__Class1.set
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
@2
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
// Jump to Class1.set
@Class1.set
0;JMP
// This is the point to return after Class1.set is called
(RTN_ADDR_1__Class1.set)
// Pop temp 0
@0
D=A
@R5
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
// Push constant 23
@23
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push constant 15
@15
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// CALLING Class2.set 2
// Save return address
@RTN_ADDR_2__Class2.set
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
@2
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
// Jump to Class2.set
@Class2.set
0;JMP
// This is the point to return after Class2.set is called
(RTN_ADDR_2__Class2.set)
// Pop temp 0
@0
D=A
@R5
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
// CALLING Class1.get 0
// Save return address
@RTN_ADDR_3__Class1.get
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
// Jump to Class1.get
@Class1.get
0;JMP
// This is the point to return after Class1.get is called
(RTN_ADDR_3__Class1.get)
// CALLING Class2.get 0
// Save return address
@RTN_ADDR_4__Class2.get
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
// Jump to Class2.get
@Class2.get
0;JMP
// This is the point to return after Class2.get is called
(RTN_ADDR_4__Class2.get)
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
