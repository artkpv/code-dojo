using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class Islands {
    public int beachLength(string[] kingdom) {
        int res=0;

        if(kingdom.Length == 0)
            return 0;
        int width = kingdom[0].Length, heigth = kingdom.Length;
        int column =1, row = 1;
        for (int i = 1; i <= width*heigth; i++)
        {
            bool isEven = row%2 == 0;
            char current =  kingdom[row - 1][column - 1];
            //right
            if (column + 1 <= width && current != kingdom[row - 1][column])
                res++;

            bool isNotLast = row + 1 <= heigth;
            //left bottom
            if (isNotLast && (isEven || column > 1) && current != kingdom[row][isEven ? column - 1 : column - 2])
                res++;

            //right bottom
            if (isNotLast && (!isEven || column < width) && current != kingdom[row][!isEven ? column - 1 : column])
                res++;


            column++;
            if(column > width)  
            {
                column = 1;
                row++;
            }
        }
        return res;
    }

}


// Powered by FileEdit
// Powered by CodeProcessor
