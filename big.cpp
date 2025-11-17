#include <iostream>
#include <string>

using namespace std;

int main() {
    string buff;
    bool pass = false;

    cout << "\nEnter the password: ";

    getline(cin, buff);

    if (buff == "darsh") {
        cout << "\nCorrect Password\n";
        pass = true;
    } else {
        cout << "\nWrong Password\n";
    }

    if (pass) {
        cout << "\nRoot/admin rights granted to user\n";
    }

    return 0;
}