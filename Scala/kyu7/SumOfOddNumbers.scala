package codewars.kyu7

object SumOfOddNumbers extends App{
/*
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
3 --> 7 + 9 + 11 = 27
*/

  //1 (1) 1 + 2 * 0
  //2 (2) 3 = 1 + 2 * 1
  //3 (4) 7 = 3 + 2 * 2
  //4 (6) 13 = 7 + 2 * 3
  //5 (8) 21

  def sumOfOddNumbers(n: Long): Long = {
    def getInitialValue(x: Long): Long = {
      if (x == 1) 1
      else 2 * (x - 1) + getInitialValue(x - 1)
    }

    (getInitialValue(n) to getInitialValue(n + 1) - 2).filter(_ % 2 != 0).sum
  }

  println(sumOfOddNumbers(41))
}
