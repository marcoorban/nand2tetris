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
(Sys.init)
// Push constant 4000
@4000
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop pointer 0
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
// Push constant 5000
@5000
D=A
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
// CALLING Sys.main 0
// Save return address
@RTN_ADDR_1__Sys.main
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
// Jump to Sys.main
@Sys.main
0;JMP
// This is the point to return after Sys.main is called
(RTN_ADDR_1__Sys.main)
// Pop temp 1
@1
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
(Sys.init$LOOP)
// goto
@Sys.init$LOOP
0;JMP
(Sys.main)
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
@0
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Push constant 4001
@4001
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop pointer 0
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
// Push constant 5001
@5001
D=A
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
// Push constant 200
@200
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop local 1
@1
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
// Push constant 40
@40
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop local 2
@2
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
// Pop local 3
@3
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
// Push constant 123
@123
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// CALLING Sys.add12 1
// Save return address
@RTN_ADDR_2__Sys.add12
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
// Jump to Sys.add12
@Sys.add12
0;JMP
// This is the point to return after Sys.add12 is called
(RTN_ADDR_2__Sys.add12)
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
// Push local 2
@2
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
// Push local 3
@3
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
// Push local 4
@4
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
(Sys.add12)
// Push constant 4002
@4002
D=A
// PUSH TO STACK 
@SP
A=M
M=D
// SP++
@SP
AM=M+1
// Pop pointer 0
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
// Push constant 5002
@5002
D=A
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
// Push constant 12
@12
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
