
#include "stdafx.h"
#include <windows.h>


#define FILE_DEVICE_HELLOWORLD 0x00008337
#define IOCTL_SAYHELLO (ULONG) CTL_CODE( FILE_DEVICE_HELLOWORLD, 0x00, METHOD_BUFFERED, FILE_ANY_ACCESS )

int main()
{

	HANDLE hDevice;
	DWORD nb;
	hDevice = CreateFile(TEXT("\\\\.\\HelloWorld"), GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	DeviceIoControl(hDevice, IOCTL_SAYHELLO, NULL, 0, NULL, 0, &nb, NULL);
	CloseHandle(hDevice);
	return 0;

}
