#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char findClass(int firstOctet) { if
(firstOctet >= 1 && firstOctet <= 126)
return 'A';
 else if (firstOctet >= 128 && firstOctet <= 191)
return 'B';
 else if (firstOctet >= 192 && firstOctet <= 223)
return 'C';
 else if (firstOctet >= 224 && firstOctet <= 239)
return 'D';
 else if (firstOctet >= 240 && firstOctet <= 255)
return 'E'; else
 return 'X'; // Invalid IP
}
int isPrivate(int firstOctet, int secondOctet) {
 if ((firstOctet == 10) ||
 (firstOctet == 172 && secondOctet >= 16 && secondOctet <= 31) ||
 (firstOctet == 192 && secondOctet == 168))
{ return 1;
 }
return 0;
}
int main()
{ char ip[16];
 int octets[4];
 printf("Enter an IP address (e.g., 192.168.1.1): ");
scanf("%15s", ip);
 if (sscanf(ip, "%d.%d.%d.%d", &octets[0], &octets[1], &octets[2], &octets[3]) != 4)
{ printf("Invalid IP address format!\n"); return 1;
 }
 for (int i = 0; i < 4; i++) { if
(octets[i] < 0 || octets[i] > 255) {
 printf("Invalid IP address! Each octet must be between 0 and 255.\n");
return 1;
 }
 }
 char ipClass = findClass(octets[0]);
 if (ipClass == 'X')
{ printf("Invalid IP address class!\n");
 return 1;
 }
 int privateFlag = isPrivate(octets[0], octets[1]);
 printf("IP Address: %s\n", ip);
printf("Class: %c\n", ipClass);
 printf("Type: %s\n", privateFlag ? "Private" : "Public");
 return 0;
}