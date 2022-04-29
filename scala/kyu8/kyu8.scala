package codewars.kyu8

object kyu8 {
  def main(arg: Array[String]): Unit = {
    // println(sum_of_positive(Array(1, 2, 3, 4, 5, 6)))
    // println(vowel_count("There is something"))
    // println(countPositivesSumNegatives(Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15)))
    // println(removingElements(Array("Keep", "Remove", "Keep", "Remove", "Keep")))
  }

  def sum_of_positive(arr: Array[Int]): Int = {
    var sum = 0
    for (x <- arr) {
      if (x > 0) {
        sum += x
      }
    }
    sum
  }

  def return_negative(nmb: Int): Int = {
    if (nmb > 0) -nmb else nmb
  }

  def countPositivesSumNegatives(nmbs: Array[Int]): (Int, Int) = {
    /*
    Given an array of integers.
    Return an array, where the first element is the count of positives numbers and the second element is sum of negative
     numbers. 0 is neither positive nor negative.
     */
    val positives = nmbs.count(_ > 0)
    val negatives = nmbs.filter(_ < 0).sum
    (positives, negatives)
  }

  def removingElements[T](list: List[T]): List[T] = {
    /*
    Take an array and remove every second element from the array. Always keep the first element and start removing with
    the next element.
    Example:
    ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
    None of the arrays will be empty, so you don't have to worry about that!
     */
    println(for (e <- list.indices if e % 2 == 0) yield list(e))
    val test = (for (elem <- list.indices if elem % 2 == 0) yield list(elem)).toList
    test
  }

  println(removingElements(List("Keep", "Remove", "Keep", "Remove", "Keep")))

  def opposite(number: Double): Double = {
    if (number > 0) -number else number.abs
    // -1 * number
  }

  def removeFirstAndLastChar(s: String): String = {
    s.slice(1, s.length - 1)
  }
  println(removeFirstAndLastChar("AdsgsdgfA"))

  def reversedStrings(str:String): String = {
    str.reverse
  }

  println(reversedStrings("Hello"))
}
