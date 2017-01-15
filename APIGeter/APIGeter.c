/*
	此程序用于查找系统API和DLL内存地址
*/

#include "stdafx.h"
#include "windows.h"
#include "stdio.h"

 
void Usage()
{
        char *syb = "*";
        char tag[60];
        for(int i=0;i<60;i++)
        {
                tag = *syb;
        }
        printf("%s",tag);
        printf("\nAPIGeter\n[Usage]APIGeter [DLLName] [APIName]\n");
        printf("%s",tag);
}
 
int main(int argc,char* argv[])
{
        if(argc!=3)
        {
                Usage();
                return 1;
        }
	printf("--------------------------------------------------------\n\r")
        HINSTANCE DLLAddr = LoadLibrary(argv[1]);
        DWORD APIAddr = (DWORD)GetProcAddress(DLLAddr,argv[2]);
 
        printf("[APIGeter]Welcome to use the APIGeter\n");
 
        printf("DLL-Name:%s\nAddress:0x%x\n",argv[1],DLLAddr);
        printf("API-Name:%s\nAddress:0x%x\n",argv[2],APIAddr);
	printf("--------------------------------------------------------\n\r")
 
        return 0;
}