#include <sqlite3.h>
#include <iostream>
#include <string>


using namespace std;
int main() {
    sqlite3* db;
    int rc = sqlite3_open("medical_system.db", &db);

    if (rc) {
        cerr << "Can't open database: " << sqlite3_errmsg(db) << endl;
        sqlite3_close(db);
        return 1;
    }

    const char* createPatientsTable = "CREATE TABLE IF NOT EXISTS Patients ("
                                      "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                                      "Name TEXT NOT NULL,"
                                      "Age INT,"
                                      "Gender TEXT);";
    char* errMsg = 0;

    rc = sqlite3_exec(db, createPatientsTable, 0, 0, &errMsg);

    if (rc != SQLITE_OK) {
        cerr << "SQL error: " << errMsg << endl;
        sqlite3_free(errMsg);
    }

    const char* createDoctorsTable = "CREATE TABLE IF NOT EXISTS Doctors ("
                                      "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                                      "Name TEXT NOT NULL,"
                                      "Age INT,"
                                      "Gender TEXT,"
                                      "Department TEXT,"
                                      "Salary INT);";

    rc = sqlite3_exec(db, createDoctorsTable, 0, 0, &errMsg);

    if (rc != SQLITE_OK) {
        cerr << "SQL error: " << errMsg << endl;
        sqlite3_free(errMsg);
    }

    string patientName, patientGender;
    int patientAge;
    
    cout << "Enter patient name: ";
    cin >> patientName;
    cout << "Enter patient age: ";
    cin >> patientAge;
    cout << "Enter patient gender: ";
    cin >> patientGender;

    const char* insertPatient = "INSERT INTO Patients (Name, Age, Gender) VALUES (?, ?, ?);";
    sqlite3_stmt* stmt;

    rc = sqlite3_prepare_v2(db, insertPatient, -1, &stmt, 0);

    
    sqlite3_bind_text(stmt, 1, patientName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 2, patientAge);
    sqlite3_bind_text(stmt, 3, patientGender.c_str(), -1, SQLITE_STATIC);

    rc = sqlite3_step(stmt);

    if (rc != SQLITE_DONE) {
        cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
    }

    sqlite3_finalize(stmt);

    string doctorName, doctorGender, doctorDepartment;
    int doctorAge;
    int doctorSalary;

    cout << "Enter doctor name: ";
    cin >> doctorName;
    cout << "Enter doctor age: ";
    cin >> doctorAge;
    cout << "Enter doctor gender: ";
    cin >> doctorGender;
    cout << "Enter doctor department: ";
    cin >> doctorDepartment;
    cout << "Enter doctor salary: ";
    cin >> doctorSalary;

    const char* insertDoctor = "INSERT INTO Doctors (Name, Age, Gender, Department, Salary) VALUES (?, ?, ?, ?, ?);";

    rc = sqlite3_prepare_v2(db, insertDoctor, -1, &stmt, 0);
    sqlite3_bind_text(stmt, 1, doctorName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 2, doctorAge);
    sqlite3_bind_text(stmt, 3, doctorGender.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 4, doctorDepartment.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 5, doctorSalary);

    rc = sqlite3_step(stmt);

    if (rc != SQLITE_DONE) {
        cerr << "SQL error: " << sqlite3_errmsg(db) << endl;
    }

    sqlite3_finalize(stmt);

    sqlite3_close(db);

    return 0;
}

