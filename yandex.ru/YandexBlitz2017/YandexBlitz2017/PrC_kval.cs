using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;

/*
"Cplusplus - C - 1:0`nCplusplus - Php - 2:0`nJava - Php - 1:0`nJava - C - 2:2`nJava - Perl - 1:1`nJava - Haskell - 1:1`n"
*/

namespace YandexBlitz2017
{
	public class ProgramPRc
	{
		public static void MainPRc(string[] args)
		{
			var games = new List<Game>();
			while (true)
			{
				var line = Console.ReadLine();
				if (line == null)
					break;
				if(line.Length == 0)
					continue;
				var rows = line.Trim().Split('-').ToArray();
				Debug.Assert(rows.Length == 3);
				var goals = rows[2].Trim().Split(':').Select(int.Parse).ToArray();
				Debug.Assert(goals.Count() == 2);
				games.Add(new Game(rows[0].Trim(), rows[1].Trim(), goals[0], goals[1]));
			}

			var table = new ResultTable(games);
			Console.Write(new ResultTableTextView(table).GetText());
		}
	}

	public class ResultTableTextView
	{
		private readonly StringBuilder _b;

		private readonly int[] _colSizes;

		private readonly IOrderedEnumerable<TeamResult> _results;

		public ResultTableTextView(ResultTable table)
		{
			_results = table.TeamResults.OrderBy(r => r.Name);
			_colSizes = GetColSizes();
			_b = new StringBuilder();
		}

		public string GetText()
		{
			var count = 0;
			foreach (var r in _results)
			{
				count++;
				AddBorder();
				AddResult(r, count);
			}
			AddBorder();
			return _b.ToString();
		}

		private int[] GetColSizes()
		{
			var sizes = new List<int>();
			var results = _results;
			sizes.Add(results.Count().ToString().Length); // number
			sizes.Add(results.Max(r => r.Name.Length) + 1); // +1 for space at right
			foreach (var r in results) // result to each other team
				sizes.Add(1);
			sizes.Add(results.Max(r => r.Score.ToString().Length)); // team score
			sizes.Add(1); // team place
			return sizes.ToArray();
		}

		private void AddResult(TeamResult teamResult, int count)
		{
			_b.Append("|");
			_b.Append(count.ToString().PadLeft(_colSizes[0], ' '));
			_b.Append("|");
			_b.Append(teamResult.Name.PadRight(_colSizes[1], ' '));
			foreach (var result in _results)
			{
				_b.Append("|");
				_b.Append(teamResult.GetGameResult(result.Name));
			}
			_b.Append("|");
			_b.Append(teamResult.Score.ToString().PadLeft(_colSizes[_colSizes.Length - 2], ' '));
			_b.Append("|");
			var place = teamResult.Place;
			const int NumberOfPlacesToShow = 3;
			_b.Append((place > NumberOfPlacesToShow ? " " : place.ToString()).PadLeft(_colSizes[_colSizes.Length - 1], ' '));
			_b.Append("|");
			_b.Append(Environment.NewLine);
		}

		private void AddBorder()
		{
			foreach (var colSize in _colSizes)
				_b.Append("+" + new String('-', colSize) );
			_b.Append("+");
			_b.Append(Environment.NewLine);
		}
	}

	public class ResultTable
	{
		private readonly Dictionary<string, TeamResult> _teamResults;

		public ResultTable(List<Game> games)
		{
			_teamResults = new Dictionary<string, TeamResult>();

			foreach (var game in games)
			{
				var team1result = GetResult(game.Team1);
				var team2result = GetResult(game.Team2);
				team1result.AddGame(game);
				team2result.AddGame(game);
			}

			var orderByDescending = _teamResults.Values.OrderByDescending(r => r.TotalScore).ToList();
			orderByDescending.First().Place = 1;
			for (var i = 1; i < orderByDescending.Count; i++)
			{
				var prev = orderByDescending.ElementAt(i - 1);
				var current = orderByDescending.ElementAt(i);
				current.Place = prev.TotalScore == current.TotalScore ? prev.Place : prev.Place + 1;
			}
			TeamResults = orderByDescending;
		}

		public List<TeamResult> TeamResults { get; private set; }

		private TeamResult GetResult(string team)
		{
			if (!_teamResults.ContainsKey(team))
				_teamResults[team] = new TeamResult() { Name = team };
			return _teamResults[team];
		}
	}

	public class TeamResult
	{
		private const int SomeLargeNumberNotToMessWithNumberOfWonGames = 100000;

		public string Name { get; set; }

		public int Score { get; set; } = 0;

		public int WonGames { get; set; } = 0;

		public int TotalScore => Score * SomeLargeNumberNotToMessWithNumberOfWonGames + WonGames;

		public int Place { get; set; }

		// Гарантируется, что нет ни одной пары команд с одинаковыми 
		// названиями, что ни одна пара команд не играла между собой более одного раза
		public Dictionary<string, Game> Games { get; set; } = new Dictionary<string, Game>();

		public char GetGameResult(string otherTeam)
		{
			if (otherTeam == Name)
				return 'X';
			if (!Games.ContainsKey(otherTeam))
				return ' ';

			var g = Games[otherTeam];
			if (g.Goals1 == g.Goals2)
				return 'D';
			if (g.Team1 == Name)
				return g.Goals1 > g.Goals2 ? 'W' : 'L';

			return g.Goals2 > g.Goals1 ? 'W' : 'L';
		}

		public void AddGame(Game game)
		{
			if (game.Team1 == Name)
			{
				var didWin = game.Goals1 > game.Goals2;
				Score += didWin ? 3 : game.Goals1 == game.Goals2 ? 1 : 0;
				WonGames += didWin ? 1 : 0;
				Games.Add(game.Team2, game);
			}
			else // if (game.Team2 == Name)
			{
				var didWin = game.Goals2 > game.Goals1;
				Score += didWin ? 3 : game.Goals1 == game.Goals2 ? 1 : 0;
				WonGames += didWin ? 1 : 0;
				Games.Add(game.Team1, game);
			}
		}
	}

	public class Game
	{
		public Game(string team1, string team2, int goals1, int goals2)
		{
			Team1 = team1;
			Team2 = team2;
			Goals1 = goals1;
			Goals2 = goals2;
		}

		public string Team1 { get; }

		public string Team2 { get; }

		public int Goals1 { get; }

		public int Goals2 { get; }
	}
}