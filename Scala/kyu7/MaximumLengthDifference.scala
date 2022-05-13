package codewars.kyu7

object MaximumLengthDifference extends App {
  /*
  You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string
  in the first array and y be any string in the second array.
  Find max(abs(length(x) − length(y)))
  If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
  Example:
  a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
  a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
  mxdiflg(a1, a2) --> 13
   */

  def maximumLengthDifference(a1: Array[String], a2: Array[String]): Int = {
    if (a1.isEmpty || a2.isEmpty) -1
    else {
      val arr1 = (a2.maxBy(_.length).length - a1.minBy(_.length).length).abs
      val arr2 = (a1.maxBy(_.length).length - a2.minBy(_.length).length).abs
      if (arr1 > arr2) arr1
      else arr2
    }
  }

  println(maximumLengthDifference(
    Array("hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"),
    Array("cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww")))
}
