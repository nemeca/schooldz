/*Даны A, B : real. Получить: U=min(A,B); V=min(AB,A+B); min(U+V^2, 3.14).*/
#include <algorithm>
#include <iostream>
using namespace std;

float first(float x, float y);
float second(float x, float y);
float third(float e, float d);

int
main()
{
	float a, b;
	cin >> a >> b;
	float u = first(a, b);
	float v = second(a, b);
	float neponyal = third(u, v);
	cout << u << v << neponyal << "\n";
}

float
first(float x, float y)
{
	return min(x, y);
}

float
second(float x, float y)
{
	return min(x * y, x + y);
}

float
third(float e, float d)
{
	if (e + d * d < 3.14) {
		return e + d * d;
	} else {
		return 3.14;
	}
}
