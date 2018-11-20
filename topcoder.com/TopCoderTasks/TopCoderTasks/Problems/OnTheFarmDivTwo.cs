using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Text.RegularExpressions;

public class OnTheFarmDivTwo
{
	public int[] animals(int heads, int legs)
	{
		for( int i = 0; ((i <= heads) && ( i <= (4*legs))); i++)
		{
			for( int j = 0; (j <= (heads - i)) && ( 2*j <= (legs - 4*i)); j++)
			{
				if(((i+j) == heads) && ((4*i + 2*j) == legs))
					return new int[] {j, i};
			}
		}
		return new int[] {};
	}


}
//Powered by [KawigiEdit] 2.0!
