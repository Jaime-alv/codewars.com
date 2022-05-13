package codewars.kyu6

import scala.annotation.tailrec
import scala.collection.mutable.ListBuffer

object SplitStrings extends App{
  /*
  Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
  of characters then it should replace the missing second character of the final pair with an underscore ('_').
  Examples:
  * 'abc' =>  ['ab', 'c_']
  * 'abcdef' => ['ab', 'cd', 'ef']
   */

  @tailrec
  def splitStrings(str: String): List[String] = {
    if (str.length % 2 == 0) {
      var result = ListBuffer[String]()
      for (i <- 0 to (str.length - 2) by 2) result += {
        str.substring(i, i+2)
      }
      result.toList
    }
    else splitStrings(str + "_")
  }

  println(splitStrings("x"))


  def solution(s: String): List[String] =
    s.padTo(s.length + s.length%2, '_').grouped(2).toList
}

