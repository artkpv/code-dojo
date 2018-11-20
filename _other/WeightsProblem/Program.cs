using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Linq.Expressions;
using System.Text;

namespace WeightsProblem
{
	class Program
	{
		const int maxPossibleValue = 40;
		static void Main(string[] args)
		{
			
			int[] weights = new int[] {1,1,1};
			int[] placesInxs;
			int sumLeft, sumRight;
			bool isSuccess = false;
			int numberOfTries = 0;
			
			//переберем различные гирьки
			while (weights != null)
			{
				placesInxs = new int[weights.Length];
				
				StringBuilder reportBuilder= new StringBuilder();
				
				reportBuilder.Append("Weights: ");
				foreach (var inx in weights)
					reportBuilder.Append(inx + " ");

				// с гирьками взвешиваем веса от 1 до 40
				for (int weight = 40; weight >= 1; weight--)
				{
					isSuccess = false;
                    
					for (int i = 0; i < placesInxs.Length; i++)
						placesInxs[i] = 1;
                    while (placesInxs != null)
					{
                        sumLeft = weight;
						sumRight = 0;	

						for (int i = 0; i < placesInxs.Length; i++)
						{
							if (placesInxs[i] == 1)
								sumLeft += weights[i];
							else if (placesInxs[i] == 2)
								sumRight += weights[i];
						}
                        
						++numberOfTries;

						if (sumLeft == sumRight)
						{
							isSuccess = true;
							break;
						}
                        else
							placesInxs = Math.CombinatoricsAlgorithms.NextDistribution(placesInxs, 3);
					}

					if (!isSuccess) // не смогли найти как уравновесить весы для этого веса
						break;
					else
					{
						reportBuilder.Append("\nWeight:" + weight + " Inxs:");
						foreach (var inx in placesInxs)
							reportBuilder.Append(inx + " ");
					}
				}

				if (isSuccess)
				{
					Console.WriteLine(reportBuilder);
//					Console.Read();
				}


				if (numberOfTries% 10000 == 0)
				{
					Console.WriteLine("Already " + numberOfTries + " tries.");
					Console.WriteLine();
					foreach (var i in weights)
					{
						Console.Write(i + " ");
					}
				}
				
				//Взять следующий набор гирек
				weights = Math.CombinatoricsAlgorithms.NextDistribution(weights, maxPossibleValue);
			}

			Console.WriteLine("End.");
			Console.WriteLine(numberOfTries);
			Console.Read();
			
		}


//		static uint[] GetNext

		static uint F(uint i)
		{
			if (i == 0 || i == 1)
				return 1;
			else
				return i * F(--i);
		}

		static bool IsEqual(uint weight, uint[] leftWeights, uint[] rightWeights)
		{
			uint rightSum = 0, leftSum = weight;
			Array.ForEach(leftWeights, delegate(uint i) { leftSum += i; });
			Array.ForEach(rightWeights, delegate(uint i) { rightSum += i; });
			return leftSum == rightSum;
		}


		static uint[] GenerateNextWeights(uint[] weights)
		{
			for (int i = 0; i < weights.Length; i++)
			{
				if (weights[i] < maxPossibleValue)
				{
					weights[i]++;
					return weights;
				}
				else
				{
					if (i == weights.Length - 1)
						return null;
					else
						weights[i] = 0;
				}
			}

			throw new ArgumentException();
		}
	}
}

