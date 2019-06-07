#!python3
"""

w(n, alice) =
 any alice == w(n-x, bob) for x in 1..n-1, n%x=0

winner
 0: alice, bob == bob, alice
 1: alice, alice = bob, bob
 2: alice,

Example 1
3 alice
1 bob
0 alice > lose

Example 2
6 A
 5 B
  4 A
   3 B
    2 A
     1 B
      0 A > lose
   2 B

 4 B

 3 B

"""


class Solution(object):
    def divisorGame(self, N):
        Alice = True
        Bob = False
        games = [
            None,  # N == 0, not possible
            (Alice, Bob)  # N == 1, Alice turn, Bob wins
        ]

        def get_winner(turn, game_turn, game_winner):
            if game_turn == turn:
                return game_winner
            return not game_winner

        while len(games) < N + 1:
            # if Alice now moves, who is the winner:
            m = len(games)
            winner = Bob
            for x in range(1, m):
                if m % x != 0:
                    continue
                remain = m - x
                if get_winner(Bob, *games[remain]) == Alice:
                    winner = Alice
                    break
            games += [(Alice, winner)]
        return get_winner(Alice, *games[N])


"""
N = 6
games:
1: A B
2: A A
 get_winner B, A, B > A
3: A B
 2 -> get_w B, A, A > B
 > B
4: A A : Alice 1, Bob 1, Alice 1, Bob lose
 1  3 , get_w(B, A, B) > A
 2
5: A B,  Alice 1, Bob .. bob wins
 x=1, get_w(B,[4] -> A A) > B
6: A A
 x=1, get_w(B, A, B) > A.
   Game: Alice 6, Bob 5, Alice 4, Bob 3, Alice 2, Bob 1 lose
 x=2
 x=3




"""
