#include <bits/stdc++.h>
#include <ctime>

using namespace std;

void transmission(long long &i, long long &N, long long &tf, long long &tt) {
    while (i <= tf) {
        int z = 0; // Successful acknowledgments in the current window
        cout << "\n[Sender] Sending frames " << i << " to " << min(i + N - 1, tf) << "...\n";
        
        // Sending frames
        for (long long k = i; k < i + N && k <= tf; k++) {
            cout << "Sending Frame " << k << "..." << endl;
            tt++; // Increment transmission count
        }

        // Receiving acknowledgments
        for (long long k = i; k < i + N && k <= tf; k++) {
            int ack = rand() % 10; // 80% chance of ACK success, 20% loss
            if (ack < 8) {
                cout << "[Receiver] Acknowledgment for Frame " << k << " received." << endl;
                z++; // Successful acknowledgment
            } else {
                cout << "[Receiver] Timeout!! Frame Number " << k << " not received." << endl;
                cout << "[Sender] Retransmitting from Frame " << k << "...\n";
                break; // Retransmit from this point
            }
        }
        
        cout << "\n";
        i += z; // Slide the window forward by the number of successfully received frames
    }
}

int main() {
    long long tf, N, tt = 0;
    srand(time(NULL));

    cout << "Enter the total number of frames: ";
    cin >> tf;
    cout << "Enter the window size: ";
    cin >> N;

    long long i = 1;
    transmission(i, N, tf, tt);

    cout << "\nTotal number of frames sent (including retransmissions): " << tt << endl;
    return 0;
}
