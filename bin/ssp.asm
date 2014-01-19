global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
x:	resd	1
y:	resd	1
z:	resd	1
SECTION .text

ss1:	
push ebp
mov ebp, esp
pop	dword ebx
mov	dword [x],57
mov	ecx,56
mov	dword [z1],56
push	dword [x]
push formati
call printf
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
mov	dword [y],50
push	dword [x]
push formati
call printf
push	dword [y]
push formati
call printf
mov	ebx,z
mov	eax,[ebx]
push	eax
call	ss1
push	dword [x]
push formati
call printf
push	dword [y]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

