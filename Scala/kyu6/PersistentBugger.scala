package codewars.kyu6

import scala.annotation.tailrec

object PersistentBugger extends App{
  /*
  Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
  which is the number of times you must multiply the digits in num until you reach a single digit.
  For example (Input --> Output):
  39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
  999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
  4 --> 0 (because 4 is already a one-digit number)
   */
  def persistence(num: Int): Int = {
    @tailrec
    def rounder(num: Int, round: Int): Int = {
      val temp = num.toString.map(x => x.asDigit)
      if (num.toString.length == 1) round
      else {
        var result = 1
        for (x <- temp.indices) result *= temp(x)
        rounder(result, round + 1)
      }
    }
    rounder(num, 0)
  }

  println(persistence(25))
}
