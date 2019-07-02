/* 
 * Exercise 5-8.There is no error checking in day_of_yearor month_day. Remedy
 * this defect.
 *
 * Author: Artyom K. <w1ld at inbox dot ru>
 * Done at 06.08.2015
 */

#include <assert.h>
#include <stdio.h>

static char daytab[2][13] = {
	{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
	{0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
};

/* day_of_year: set day of year from month & day */
int day_of_year(int year, int month, int day)
{
	if(year < 1 || month > 12 || month < 1 || day < 1 || day > 31)
		return -1;
	int i, leap;
	leap = year%4 == 0 && year%100 != 0 || year%400 == 0;
	for (i = 1; i < month; i++)
		day += daytab[leap][i];
	return day;
}

/* month_day: set month, day from day of year */
void month_day(int year, int yearday, int *pmonth, int *pday)
{
	if(year < 1  || yearday < 1)
	{
		*pmonth = -1;
		*pday = -1;
		return;
	}
	int i, leap;
	leap = year%4 == 0 && year%100 != 0 || year%400 == 0;
	if(!leap && yearday > 365)
	{
		*pmonth = -1;
		*pday = -1;
		return;
	}

	for (i = 1; yearday > daytab[leap][i]; i++)
		yearday -= daytab[leap][i];
	*pmonth = i;
	*pday = yearday;
}

int main(void)
{
	int day = -1;
	int *pday = &day;
	int month = -1;
	int *pmonth = &month;

	assert(day_of_year(2014, 1, 1) == 1);
	assert(day_of_year(2014, 12, 31) == 365);

	month_day(2014, 365, pmonth, pday);
	assert(*pmonth == 12);
	assert(*pday == 31);

	assert(day_of_year(2014, 13, 1) == -1);
	assert(day_of_year(2014, 12, 32) == -1);
	assert(day_of_year(2014, 0, 31) == -1);
	assert(day_of_year(2014, 1, 0) == -1);
	assert(day_of_year(2014, 1, -1) == -1);

	month_day(2014, 366, pmonth, pday);
	assert(*pmonth == -1);
	assert(*pday == -1);

	month_day(2014, 0, pmonth, pday);
	assert(*pmonth == -1);
	assert(*pday == -1);
}
