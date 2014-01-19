global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
x:	resd	1
SECTION .text

cv:	
push ebp
mov ebp, esp
pop	dword ebx
mov	ebx,1
mov	dword [z1],1
push	dword [z1]
push formati
call printf
mov esp, ebp
pop dword ebp
ret
main:	
push ebp
mov ebp, esp
mov	dword [x],100
push	dword [x]
push formati
call printf
mov	ebx,x
mov	eax,[ebx]
push	eax
call	cv
push	dword [x]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

