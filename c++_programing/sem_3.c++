//if statement----->

// #include<iostream>
// using namespace std;
// int main(){
//     int age;
//     cout<<"enter your age:";
//     cin>>age;
//     if(age>=18){
//         cout<<"you are eligible for voting";
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main(){
//     int marks;
//     cout<<"enter marks scored:";
//     cin>>marks;
//     if(marks>40){
//         cout<<"PASS";
//     }
//     return 0;
// }

//if-else statement---->

// #include<iostream>
// using namespace std;
// int main(){
//     int age;
//     cout<<"enter your age:";
//     cin>>age;
//     if(age>=18){
//         cout<<"you are eligible for voting";
//     }
//     else{
//         cout<<"Not eligible"<<endl;
//         cout<<"wait for "<<18-age <<" years";
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main(){
//     int marks;
//     cout<<"enter marks scored:";
//     cin>>marks;
//     if(marks>40){
//         cout<<"PASS";
//     }
//     else{
//         cout<<"FAIL"<<endl;
//         cout<<"Try to improve";
//     }
//     return 0;
// }

//nested if-else statement

// #include<iostream>
// using namespace std;
// int main(){
//     int a,b;
//     cout<<"enter the numbers:";
//     cin>>a>>b;
//     if(a>b){
//         cout<<a<<" is greater than "<< b;
//     }
//     else if(b>a){
//         cout<<b<<" is greater than "<< a;
//     }
//     else{
//         cout<<"both are equal";
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main(){
//     int marks;
//     cout<<"enter obtained marks:";
//     cin>>marks;
//     if(marks<=100 && marks>=90){
//         cout<<"Your grade is O";
//     }
//     else if(marks<90 && marks>=80){
//         cout<<"Your grade is E";
//     }
//     else if(marks<80 && marks>=70){
//         cout<<"Your grade is A";
//     }
//     else if(marks<70 && marks>=60){
//         cout<<"Your grade is B";
//     }
//     else if(marks<60 && marks>=50){
//         cout<<"Your grade is C";
//     }
//     else if(marks<50 && marks>=40){
//         cout<<"Your grade is D";
//     }
//     else{
//         cout<<"Your grade is F";
//     }
//     return 0;
// }


//Break statement----->

// #include<iostream>
// using namespace std;
// int main(){
//     for(int i=0; i<10; i++){
//         if(i==6){
//             break;
//         }
//         cout<<i;
//     }
// }

// #include<iostream>
// using namespace std;
// int main(){
//     int number;
//     while(true){
//     cout<<"enter a number:";
//     cin>>number;
    
//     if(number<0)
//         break;
//     }
// }


//Continue statement------>

// #include<iostream>
// using namespace std;
// int main(){
//     for(int i=0; i<10; i++){
//         if(i==4){
//             continue;
//         }
//         else{
//             cout<<i;
//         }
//     }
//     return 0;
// }


// #include <iostream>
// using namespace std;
// int main()
// {
  
//     for (int i = 1; i <= 2; i++) {
//         for (int j = 0; j <= 4; j++) {
//             if (j == 2) {
//                 continue;
//             }
//             cout << j << " ";
//         }
//         cout << endl;
//     }
  
//     return 0;
// }



//For loop------->

// #include<iostream>
// using namespace std;
// int main(){
//     for(char ch='A'; ch<='Z'; ch++){
//         cout<<ch;
//     }
//     return 0;

// }

// #include<iostream>
// using namespace std;
// int main(){
//         for(int i=1; i<=5; i++){
//             cout<<"hello world\n";
//         }
//         return 0;
// }



//While loop----->

// #include<iostream>
// using namespace std;
// int main(){
//     int i=1;
//     while(i<=3){
//         cout<<"hi, my name is Prachi\n";
//         i=i+1;
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main(){
//     int x;
//     int i=1;
//     cout<<"enter a number:";
//     cin>>x;
//     while(i<=x){
//         cout<<i;
//         i++;
//     }
//     return 0;
// }


//Do-While loop----->

// #include<iostream>
// using namespace std;
// int main(){
//     int i=1;
//     do{
//        cout<<i;
//        i++; 
//     } while (i<=5);
//     return 0;
// }


//Switch statement----->

// #include<iostream>
// using namespace std;
// int main()
// {
//     int month;
//     cout<<"\nEnter the Month's number :";
//     cin>>month;
//     switch (month)
//     {
//     case 1:
//         cout<<"January";
//         break;
//     case 2:
//         cout<<"Febrauary";
//         break;
//     case 3:
//         cout<<"March";
//         break;
//     case 4:
//         cout<<"April";
//         break;
//     case 5:
//         cout<<"May";
//         break;
//     case 6:
//         cout<<"June";
//         break;
//     case 7:
//         cout<<"July";
//         break;
//     case 8:
//         cout<<"August";
//         break;
//     case 9:
//         cout<<"September";
//         break;
//     case 10:
//         cout<<"October";
//         break;
//     case 11:
//         cout<<"November";
//         break;
//     case 12:
//         cout<<"December";
//         break;
//     }
//     return 0;
// }


// #include<iostream>
// using namespace std;
// int main()
// {
//     int day;
//     cout<<"\nEnter the day's number :";
//     cin>>day;
//     switch (day){
//         case 1: 
//             cout<<"monday";
//             break;
//         case 2:
//             cout<<"tuesday";
//             break;
//         case 3:
//             cout<<"wednesday";
//             break;
//         case 4:
//             cout<<"thursday";
//             break;
//         case 5:
//             cout<<"friday";
//             break;
//         case 6:
//             cout<<"saturday";
//             break;
//         case 7:
//             cout<<"sunday";
//             break;
//         default:
//             cout<<"invalid entry";
//     }
//     return 0;
// }





// #include <iostream>
// using namespace std;
// class simple_interest {
// private:
//     int p, r, t, s;
//     void input();
//     void process();
// public:
//     void output();  
// };

// void simple_interest::input() {
//     cout << "Enter p, r, t: ";
//     cin >> p >> r >> t;
// }
// void simple_interest::process() {
//     s = (p * r * t) / 100;
// }
// void simple_interest::output() {
//     input();      
//     process();    
//     cout << "The calculated interest is: " << s;
// }
// int main() {
//     simple_interest si;
//     si.output();  
//     return 0;
// }






#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string emp_name;
    string emp_designation;
    double emp_salary;
    char performance_grade;

public:
    // Function to input employee details
    void input_details() {
        cout << "Enter employee name: ";
        cin >> emp_name;

        cout << "Enter employee designation: ";
        cin >> emp_designation;

        cout << "Enter employee salary: ";
        cin >> emp_salary;

        cout << "Enter performance grade (A+ to F): ";
        cin >> performance_grade;
    }

    // Function to display employee details along with bonus
    void display_details() {
        cout << "Employee Name: " << emp_name << endl;
        cout << "Employee Designation: " << emp_designation << endl;
        cout << "Employee Salary: " << emp_salary << endl;
        cout << "Performance Grade: " << performance_grade << endl;

        double bonus = calculate_bonus();
        cout << "Bonus: " << bonus << endl;
    }

    // Function to calculate bonus based on performance grade
    double calculate_bonus() {
        double bonus = 0.0;

        switch (performance_grade) {
            case 'A+':
                bonus = 5000;
                break;
            case 'A':
                bonus = 4000;
                break;
            case 'B':
                bonus = 3000;
                break;
            case 'C':
                bonus = 2000;
                break;
            case 'D':
                bonus = 1000;
                break;
            case 'E':
                bonus = 500;
                break;
            case 'F':
                bonus = 0;
                break;
            default:
                cout << "Invalid performance grade" << endl;
        }

        return bonus;
    }
};

int main() {
    Employee emp;
    emp.input_details();
    emp.display_details();

    return 0;
}


