using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class VacationTime {
    public int bestSchedule(int N, int K, int[] workingDays) {
        int res = int.MaxValue;
        
        for (int i = 1; i <= N-K+1; i++)
        {
            int intersection = 0;
            for (int j = i; j < i+K; j++)
            {
                if (Array.IndexOf(workingDays, j) != -1)
                    intersection++;
            }

            if (intersection < res)
                res = intersection;

        }
        return res == int.MaxValue ? 0 : res;
    }

}


// Powered by FileEdit
// Powered by CodeProcessor
