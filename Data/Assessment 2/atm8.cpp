#include <iostream>
#include <ctime>
using namespace std;

class ATM {
private:
    string currentDateTime() {
        time_t now = time(0);
        tm* ltm = localtime(&now);
        string dateTime = asctime(ltm);
        //dateTime.pop_back(); // Remove the newline character
        return dateTime;
    }

    int atmPin;
    int attempts;
    double startingBalance;
    double currentBalance;

public:
    ATM() {
        atmPin = 12345;
        attempts = 1;
        startingBalance = 60000.0;
        currentBalance = 20000.0;
    }

    void displayWelcomeScreen() {
        cout << "======================================" << endl;
        cout << "         Welcome to SBI Bank ATM" << endl;
        cout << "======================================" << endl;
        cout << "Date and Time: " << currentDateTime() << endl;
        cout << "======================================" << endl;
        cout <<"Enter your acc pin access number![only one attempt allowed]";
        cout << "======================================" << endl;
        cout << "2. Help" << endl;
    }

    void enterATMPin() {
        int pin;
        cout <<"Enter your acc pin access number![only one attempt allowed]";
        cin >> pin;
        if (pin == atmPin) {
            displayMenuScreen();
        } else {
            cout << "Incorrect PIN. You have " << (1 - attempts) << " attempt(s) left." << endl;
            attempts++;
            if (attempts > 3) {
                cout << "Max attempts reached. Your card is blocked." << endl;
                exit(0);
            }
            enterATMPin();
        }
    }

    void displayMenuScreen() {
        cout << "Menu:" << endl;
        cout << "1. Deposit" << endl;
        cout << "2. Withdraw" << endl;
        cout << "3. Check Balance" << endl;
        int choice;
        cout << "Select a choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                deposit();
                break;
            case 2:
                withdraw();
                break;
            case 3:
                checkBalance();
                break;
            default:
                cout << "Invalid choice. Please select a valid option." << endl;
        }
    }

    void deposit() {
        double amount;
        cout << "Enter the amount to deposit: ";
        cin >> amount;
        currentBalance += amount;
        cout << "Deposit successful. Your new balance is: Rs. " << currentBalance << endl;
    }

    void withdraw() {
        double amount;
        cout << "Enter the amount to withdraw: ";
        cin >> amount;
        if (amount > currentBalance) {
            cout << "Insufficient balance. Your current balance is: Rs. " << currentBalance << endl;
        } else {
            currentBalance -= amount;
            cout << "Withdrawal successful. Your new balance is: Rs. " << currentBalance << endl;
        }
    }

    void checkBalance() {
        cout << "Your current balance is: Rs. " << currentBalance << endl;
    }
};

int main() {
    ATM atm;
    atm.displayWelcomeScreen();
    int choice;
    cout << "Enter your choice: ";
    cin >> choice;

    switch (choice) {
        case 1:
            atm.enterATMPin();
            break;
        case 2:
            cout << "This is the help screen." << endl;
            break;
        default:
            cout << "Invalid choice. Please select a valid option." << endl;
    }

    return 0;
}

