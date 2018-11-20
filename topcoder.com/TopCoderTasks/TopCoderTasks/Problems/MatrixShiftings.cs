using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class MatrixShiftings {
    public int minimumShifts(string[] matrix, int value) {
        int? res = null;
        Regex r = new Regex(value.ToString());
        for (int i = 0; i < matrix.Length; i++)
        {
            string str = matrix[i];

            Match m = r.Match(str);
            while (m.Success)
            {
                if (m.Index != -1)
                {
                    int shift = GetShifts(matrix, m.Index, i);
                    if (!res.HasValue || res.HasValue && res.Value > shift)
                        res = shift;
                }
                m = m.NextMatch();
            }
            

        }

        return res.HasValue ? res.Value : -1 ;
    }

    private int GetShifts(string[] matrix, int x, int y)
    {
        if (x == 0 && y == 0)
            return 0;

        int xShift, yShift;
        int xLength = matrix[0].Length;
        xShift = xLength - x < x ? xLength - x : x;

        yShift = matrix.Length - y < y ? matrix.Length - y : y;

        return xShift + yShift;
    }

}


// Powered by FileEdit
// Powered by CodeProcessor
