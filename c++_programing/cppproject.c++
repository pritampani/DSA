
#include <iostream>
#include <sqlite3.h>
// Function to execute SQL queries
int executeSQL(sqlite3* db, const char* sql) {
    char* errMsg = 0;
    int result = sqlite3_exec(db, sql, 0, 0, &errMsg);
    
    if (result != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }
    return result;
}
int main() {
    sqlite3* db;
    int rc = sqlite3_open("medical_system.db", &db);

    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return 1;
    } else {
        std::cout << "Database opened successfully." << std::endl;
    }
    
    // Create tables for patients and doctors
    const char* createPatientsTableSQL = "CREATE TABLE Patients ("
        "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        "Name TEXT NOT NULL, "
        "Age INTEGER NOT NULL)";
    executeSQL(db, createPatientsTableSQL);

    const char* createDoctorsTableSQL = "CREATE TABLE Doctors ("
        "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        "Name TEXT NOT NULL, "
        "Specialty TEXT NOT NULL)";
    executeSQL(db, createDoctorsTableSQL);

    while (true) {
        // Display menu options
        std::cout << "Medical Information System Menu:" << std::endl;
        std::cout << "1. Add a patient" << std::endl;
        std::cout << "2. Add a doctor" << std::endl;
        std::cout << "0. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        
        int choice;
        std::cin >> choice;
        
        if (choice == 1) {
            // Add a patient
            std::string name;
            int age;
            std::cout << "Enter patient name: ";
            std::cin >> name;
            std::cout << "Enter patient age: ";
            std::cin >> age;

            const char* addPatientSQL = "INSERT INTO Patients (Name, Age) VALUES (?, ?)";
            sqlite3_stmt* stmt;
            sqlite3_prepare_v2(db, addPatientSQL, -1, &stmt, 0);
            sqlite3_bind_text(stmt, 1, name.c_str(), -1, SQLITE_STATIC);
            sqlite3_bind_int(stmt, 2, age);
            
            if (sqlite3_step(stmt) == SQLITE_DONE) {
                std::cout << "Patient added successfully." << std::endl;
            } else {
                std::cerr << "Failed to add patient." << std::endl;
            }
            
            sqlite3_finalize(stmt);
        } else if (choice == 2) {
            // Add a doctor
            std::string name, specialty;
            std::cout << "Enter doctor name: ";
            std::cin >> name;
            std::cout << "Enter doctor specialty: ";
            std::cin >> specialty;

            const char* addDoctorSQL = "INSERT INTO Doctors (Name, Specialty) VALUES (?, ?)";
            sqlite3_stmt* stmt;
            sqlite3_prepare_v2(db, addDoctorSQL, -1, &stmt, 0);
            sqlite3_bind_text(stmt, 1, name.c_str(), -1, SQLITE_STATIC);
            sqlite3_bind_text(stmt, 2, specialty.c_str(), -1, SQLITE_STATIC);
            
            if (sqlite3_step(stmt) == SQLITE_DONE) {
                std::cout << "Doctor added successfully." << std::endl;
            } else {
                std::cerr << "Failed to add doctor." << std::endl;
            }
            
            sqlite3_finalize(stmt);
        } else if (choice == 0) {
            break;
        } else {
            std::cout << "Invalid choice. Please try again." << std::endl;
        }
    }

    sqlite3_close(db);
    return 0;
}
