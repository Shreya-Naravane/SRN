#include<stdio.h>
int sum(int a){
	if(a==0)
		return;
	else
		return a+sum(a-1);
}

int main(){
	int a=3;
	int result=sum(a);
	printf("The result is:%d",result);
}
