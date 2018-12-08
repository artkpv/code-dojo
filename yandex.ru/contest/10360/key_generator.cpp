#include    <iostream>
#include <string>	   
	
using namespace	std;   	
 	   
int	main()
{ 	 	  	
 	int x =	4;
	    	   
	++x;
 	 	  	
 	  	
	int y = ++x +	++x;   
	--y;
 	 	  	
 	string s =	to_string(y);
	    	   
	
 	s.append(" is");	  	
 	s.append(" a number");	
	    	   
	
 	x <<=	2;  	
 	  	
	s.append(", and ");  	   
	s.append(to_string(x));
 	s.append(" too");	  	
 	  	
	cout << s << endl;	   
}	
 	
