package codewars.kyu7

import scala.annotation.tailrec
import scala.language.postfixOps

object kyu7 {
  def main(args: Array[String]): Unit = {
    // println(vowel_count("There is something"))
  }

  def vowel_count(str: String): Int = {
    str.toLowerCase().replaceAll("[^aeiou]", "").length()
  }

  def accum(str: String): String = {
    val test = (for (index <- str.indices) yield str.substring(index, index + 1).toUpperCase() + str.substring(index, index + 1).toLowerCase() * index).mkString("", "-", "")
    println(str.indices.map(i => str(i).toLower.toString * (i+1) capitalize).mkString("-"))
    test
  }

  // println(accum("hello"))

  def isSquare(x: Int): Boolean = {
    import scala.math.pow
    if (pow(x, 0.5) isValidInt) true else false
  }

  // println(isSquare(9))

  def XO(str: String):Boolean = {
    // Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
    // insensitive. The string can contain any char.
    // if (str.toLowerCase().count(_ == 'x') == str.toLowerCase().count(_ == 'o')) true else false
    str.toLowerCase().count(_ == 'x') == str.toLowerCase().count(_ == 'o')
  }

  // println(XO("zzoo"))

  def shortestWord(sentence: String): Int = {
    var length = ""
    val array = sentence.split(" ")
    length = array(0)
    for (word <- array) if (word.length < length.length) length = word
    length.length
    // println(array.mkString(","))
  }

  def findShortest(str: String): Int = {
    str.split(' ').map(_.length).min
  }

  // println(shortestWord("Hello world more words for the world of many humans and persons"))

  def dnaStrand(dna: String): String = {
    dna.map(x => if (x == 'A') 'T' else if (x == 'T') 'A' else if (x == 'C') 'G' else 'C')
    // dna.map { case 'A' => 'T' case 'T' => 'A' case 'G' => 'C' case 'C' => 'G' }
  }

  // println(dnaStrand("GTAT"))

  def sumOfTwoLowest(array: List[Int]): Int = {
    val arr_1 = array.filter(! _.==(array.min))
    array.min + arr_1.min
  }

  def sumTwoSmallest(numbers: List[Int]): Int =
    numbers.sorted.take(2).sum

  // println(sumOfTwoLowest(List(10, 343445353, 3453445, 34535453)))

  def getTheMiddleCharacter(string: String): String = {
    if (string.length % 2 == 0)
      string.substring((string.length/2).toInt - 1, (string.length/2).toInt + 1)
    else
      string.substring((string.length/2).toInt, (string.length/2).toInt + 1)
  }

  // println(getTheMiddleCharacter("testing"))

  // TODO: exercise not completed!
  def speedControl(distance: List[Double], s: Int): Int = {
    val avg = distance.length
    println(avg)
    if (distance.size == 2) (3600 * (distance.take(2).sum - distance.take(1).sum) / s).toInt
    else
      ((3600 * (distance.take(2).sum - distance.take(1).sum) / s) + speedControl(distance.drop(2), s)).toInt
  }

  // println(speedControl(List(0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25), 15))

  def sumOfNumbers(a: Int, b: Int): Int = {
    (for (i <- List(a, b).min to List(a, b).max) yield i).sum
  }

  // println(sumOfNumbers(2, -1))

  def longest(s1: String, s2: String): String = {
    (s1 + s2).distinct.sorted
  }

  def nb_year(p0: Int, percent: Double, aug: Int, p: Int): Int ={
    @tailrec
    def roundYear(p0: Int, percent: Double, aug: Int, p: Int, rounds: Int): Int = {
      val result = (p0 + (p0 * (percent / 100) + aug)).toInt
      if (p0 >= p) rounds
      else roundYear(result, percent, aug, p, rounds + 1)
    }
    (roundYear(p0, percent, aug, p, 1) - 1)
  }

  // println(nb_year(1500000, 2.5, 10000, 2000000))

  def numberOfPeopleInTheBus(busStops: List[(Int, Int)]): Int = {
    busStops.map(x => x._1 - x._2).sum
  }

  println(numberOfPeopleInTheBus(List((3, 0), (9, 1), (4, 10), (12, 2), (6, 1), (7, 10))))
}
