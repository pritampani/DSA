#include <bits/stdc++.h>
using namespace std;

int main() {
    int gcd = 0;
    int n1 = 12, n2 = 36;

    for (int i = 1; i <= min(n1, n2); i++) {
        if (n1 % i == 0 && n2 % i == 0) {
            gcd = i;
        }
    }

    cout << gcd;
}