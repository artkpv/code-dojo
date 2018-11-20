using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Text.RegularExpressions;

public class RabbitVoting
{
  public string getWinner(string[] names, string[] votes)
  {
    if(names == null || names.Length == 0 || votes.Length == 0)
      return string.Empty;
      
    string winner = "";
    int max = 0;  
    Dictionary<string, int> votesTotal = new Dictionary<string, int>();
    for(int i=0; i < names.Length; i++)
    {
      string name = names[i], vote = votes[i];
      if(name != vote)
      {
        if(votesTotal.ContainsKey(vote))
          votesTotal[vote]++;
        else
          votesTotal.Add(vote, 1);
          
        if(max < votesTotal[vote])
        {
        	winner = vote;
        	max = votesTotal[vote];
        }
      }
    }
    
    if(votesTotal.Count == 0)
      return string.Empty; 
      
      
	int maxcount = 0;
	
    foreach(KeyValuePair<string, int> pair in votesTotal)
	    if(pair.Value == max)
   			maxcount++;
    return maxcount > 1 ? "" : winner;
  }


}
//Powered by [KawigiEdit] 2.0!
