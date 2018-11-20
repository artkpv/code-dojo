using NUnit.Framework;


using System;
using System.Linq;
using System.Collections.Generic;

public class TicTacToe
{
  public int IsSolved(int[,] board)
  {
    int L = board.GetLength(0);
    const int directions = 3, 
          myOWeight = 4,
          OWeight = 2,
          XWeight = 1;

    int sum;
    bool hasEmpty = false;
    for(int direction = 0; direction < directions; direction++){
      int count = 0;
      sum = 0;
      foreach(var i in Next(board, direction)){
        count++;
        sum += (i == OWeight ? myOWeight : i);

        if(count % L == 0) {
          if(sum == myOWeight * L) 
            return OWeight;
          else if (sum == XWeight * L)
            return XWeight;
          sum = 0;
          count = 0;
        }

        if(i == 0)
          hasEmpty = true;
      }
    }

    const int catsGame = 0,
          notSolvedYet = -1;
    return hasEmpty ? notSolvedYet : catsGame;
  }

  private static IEnumerable<int> Next(int[,] board, int direction) { 
    int L = board.GetLength(0);

    if(direction == 2) {
      for(int i = 0; i < 2; i++) {
        for(int j = 0; j < L; j++) {
          yield return board[ i == 0 ? j : Math.Abs(j - L + 1) ,j];
        }
      }
    }
    else {
      for(int i = 0; i < L; i++) {
        for(int j = 0; j < L; j++) {
          if(direction == 0) 
            yield return board[i,j];
          else if(direction == 1) 
            yield return board[j,i];
        }
      }
    }
  }
}


[TestFixture]
public class TicTacToeTest {
	private TicTacToe tictactoe = new TicTacToe();
  
	[Test]
	public void test1() {
		int[,] board = new int[,] { { 1, 1, 1 }, { 0, 2, 2 }, { 0, 0, 0 } };
    Assert.AreEqual(1, tictactoe.IsSolved(board));
	}
}
