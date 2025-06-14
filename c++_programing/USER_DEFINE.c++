//Function -> Without Return type With Argument
// #include<iostream>
// using namespace std;
// class sum
// {
// 	int n1,n2,n3;
// 	public:
// 		void input();
// 		void process(int,int);
// 		void output();
// };
// void sum ::input()
// {
// 	cout<<"enter 2 no.s";
// 	cin>>n1>>n2;
// 	process(n1,n2);
// }
// void sum::	process(int x,int y)
// {
// 	n3=x+y;
// }
// void sum::	output()
// {
// 	cout<<"Result is:"<<n3;
// }
// int main()
// {
// 	sum s;
// 	s.input();
// 	s.output();
// 	return 0;

// }




// Function -> Without Return type Without Argument
// #include<iostream>
// using namespace std;
// class sum
// {
// 	int n1,n2,n3;
// 	public:
// 		void input();
// 		void process();
// 		void output();
// };
// void sum ::input()
// {
// 	cout<<"enter 2 no.s";
// 	cin>>n1>>n2;
	
// }
// void sum::	process()
// {
// 	n3=n1+n2;
// }
// void sum::	output()
// {
// 	cout<<"Result is:"<<n3;
// }
// int main()
// {
// 	sum s;
// 	s.input();
// 	s.process();
// 	s.output();
// 	return 0;
// }








// Function -> With Return type With Argument
// #include<iostream>
// using namespace std;
// class sum
// {
// 	int n1,n2,n3,n4;
// 	public:
// 		void input();
// 		int process(int,int);
// 		void output();
// };
// void sum ::input()
// {
// 	cout<<"enter 2 no.s";
// 	cin>>n1>>n2;
// 	n3=process(n1,n2);
	
// }
// int sum:: process(int x, int y)
// {
// 	n4=x+y;
// 	return n4;
// }
// void sum::	output()
// {
// 	cout<<"Result is:"<<n3;
// }
// int main()
// {
// 	sum s;
// 	s.input();
// 	s.output();
// 	return 0;
// }









// Function -> With Return type Without Argument
// #include<iostream>
// using namespace std;
// class sum
// {
// 	int n1,n2,n3,n4;
// 	public:
// 		void input();
// 		int process();
// 		void output();
// };
// void sum ::input()
// {
// 	cout<<"enter 2 no.s";
// 	cin>>n1>>n2;
// 	n3=process();
	
// }
// int sum:: process()
// {
// 	n4=n1+n2;
// 	return n4;
// }
// void sum::	output()
// {
// 	cout<<"Result is:"<<n3;
// }
// int main()
// {
// 	sum s;
// 	s.input();
// 	s.output();
// 	return 0;
// }







// Object as an Argument
// Function -> Without Return type With Argument
// #include<iostream>
// using namespace std;
// class sum
// {
// 	int n1,n2,n3;
// 	public:
// 		void input();
// 		void process(sum ,sum );
// 		void output();
// };
// void sum ::input()
// {
// 	cout<<"enter 2 no.s";
// 	cin>>n1>>n2;

// }
// void sum::	process(sum x,sum y)
// {
// 	n3=x.n1+y.n2;
// }
// void sum::	output()
// {
// 	cout<<"Result is:"<<n3;
// }
// int main()
// {
// 	sum s;
// 	s.input();
// 	s.process(s,s);
// 	s.output();
// 	return 0;
// }








// #include <iostream>
// using namespace std;
// class recursive_factorial
// {
// 	int n, result;
// 	public:
// 		void input();
// 		int factorial(int);
// 		void output();
// };
// void recursive_factorial::input()
// {
// 	cout << "Enter a non-negative number: ";
//     cin >> n;	
//     result=factorial(n);
    
// }

// int recursive_factorial::factorial(int n)
//  {
//     if (n > 1)
// 	{
//         return n * factorial(n - 1);
//     }
// 	else 
// 	{
//         return 1;
//     }
// }
// void recursive_factorial::output()
// {
// 	cout << "Factorial of " << n << " = " << result;
// }
// int main()
// {
    
// 	recursive_factorial r;
//     r.input();
//     r.output();
//     return 0;
// }


//Clearly Understand About the use of friend function 
// #include<iostream>
// using namespace std;
// class about_friend
// {
// 	char name[10];
// 	int age;
// 	float cgpa;
// 	public:
// 		void input();
// 	friend void output(about_friend);
// };
// void about_friend :: input()
// {
// 	cout<<"enter the name, age and cgpa of student";
// 	cin>>name>>age>>cgpa;
// }
// void output(about_friend a)
// {
// 	cout<<"Name is:"<<a.name<<endl<<"Age is:"<<a.age<<endl<<"Cgpa is:"<<a.cgpa;
// }
// int main()
// {
// 	about_friend af;
// 	af.input();
// 	output(af);
// 	return 0;
// }










// #include<iostream>
// using namespace std;

// class first
// {
// 	int b;
// 	public:
// 	first()
// 	{
// 		b=10;
// 	}
// 	void display()
// 	{
// 		cout<<"\n b= "<<b;
// 	}
		
// };
// class second : public first
// {
// 	int d;
// 	public:
// 	second()
// 	{
// 		d=20;
// 	}
// 	void display()
// 	{
// 		cout<<"\n d= "<<d;
// 	}		
// };
// int main()
// {
// 	first f,*p;
// 	second s;
// 	p=&f;
// 	p->display();
// 	p=&s;
// 	p->display();
// 	return 0;
// }









// #include<iostream>
// using namespace std;
// class about_friend
// {
// 	char name[10];
// 	int age;
// 	float cgpa;
// 	public:
// 		void input();
// 	friend void output(about_friend);
// };
// void about_friend :: input()
// {
// 	cout<<"enter the name, age and cgpa of student";
// 	cin>>name>>age>>cgpa;
// }
// void output(about_friend a)
// {
// 	cout<<"Name is:"<<a.name<<endl<<"Age is:"<<a.age<<endl<<"Cgpa is:"<<a.cgpa<<endl;
// }

// int main()
// {
// 	about_friend af[2];
// 	for(int i=0;i<2;i++)
// 	{
// 		af[i].input();
// 		output(af[i]);
// 	}
// 	return 0;
// }






#include<iostream>
using namespace std;
class sum
{
	int n3;
	public:
		sum(int p, int q);
};


sum ::sum(int p, int q)
{
	n3=p+q;
	cout<<"Result is:"<<n3<<endl;
}

int main()
{
	sum s(5,6); // Implicit Call
	sum x=sum(9,10);// Explicit call
	return 0;
}
