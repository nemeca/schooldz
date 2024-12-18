#include <cmath>
#include <iostream>
using namespace std;

float first(float a);
float second(float a);
float third(float a);

int
main()
{
	int A;
	cin >> A;
	float X = first(A);
	float Y = second(A);
	float Z = third(A);
	cout << X - Y + 2 * Z << "\n";
}

float
first(float a)
{
	return (a * a - 2 * a + 17) / (2 * a - 9);
}

float
second(float a)
{
	return (a * a * a * a - 2 * a * a + 17) / (2 * a * a - 9);
}

float
third(float a)
{
	return (sin(a) * sin(a) - 2 * sin(a) + 17) / (2 * sin(a) - 9);
}
