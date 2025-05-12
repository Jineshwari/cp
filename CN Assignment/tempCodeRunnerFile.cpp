#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void calculateSubnetMask(int subnetBits, int subnetMask[]) {
    for (int i = 0; i < 4; i++) {
        if (subnetBits >= 8) {
            subnetMask[i] = 255;
            subnetBits -= 8;
        } else if (subnetBits > 0) {
            subnetMask[i] = 256 - (1 << (8 - subnetBits));
            subnetBits = 0;
        } else {
            subnetMask[i] = 0;
        }
    }
}

void printIP(int ip[]) {
    for (int i = 0; i < 4; i++) {
        printf("%d", ip[i]);
        if (i < 3) printf(".");
    }
    printf("\n");
}

char getIPClass(int firstOctet) {
    if (firstOctet >= 1 && firstOctet <= 126) {
        return 'A';
    } else if (firstOctet >= 128 && firstOctet <= 191) {
        return 'B';
    } else if (firstOctet >= 192 && firstOctet <= 223) {
        return 'C';
    } else {
        return 'X';
    }
}

void getDefaultSubnetMask(char ipClass, int subnetMask[]) {
    if (ipClass == 'A') {
        subnetMask[0] = 255; subnetMask[1] = 0; subnetMask[2] = 0; subnetMask[3] = 0;
    } else if (ipClass == 'B') {
        subnetMask[0] = 255; subnetMask[1] = 255; subnetMask[2] = 0; subnetMask[3] = 0;
    } else if (ipClass == 'C') {
        subnetMask[0] = 255; subnetMask[1] = 255; subnetMask[2] = 255; subnetMask[3] = 0;
    }
}

int main() {
    char ipAddress[16];
    int ip[4], subnetMask[4], subnetBits, numSubnets;

    printf("Enter IP address: ");
    scanf("%s", ipAddress);
    sscanf(ipAddress, "%d.%d.%d.%d", &ip[0], &ip[1], &ip[2], &ip[3]);

    char ipClass = getIPClass(ip[0]);
    if (ipClass == 'X') {
        printf("Invalid or unsupported IP class!\n");
        return 1;
    }

    getDefaultSubnetMask(ipClass, subnetMask);
    printf("IP Class: %c\n", ipClass);
    printf("Default Subnet Mask: ");
    printIP(subnetMask);

    printf("Enter the number of subnets you want: ");
    scanf("%d", &numSubnets);

    for (int i = 1; i <= numSubnets; i++) {
        printf("Enter the number of subnet bits for subnet %d: ", i);
        scanf("%d", &subnetBits);

        calculateSubnetMask(subnetBits, subnetMask);
        printf("Subnet %d Mask: ", i);
        printIP(subnetMask);
    }

    return 0;
}
