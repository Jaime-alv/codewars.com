package codewars.kyu7

object countTheDigit extends App {
  /*
  Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
  Square all numbers k (0 <= k <= n) between 0 and n.
  Count the numbers of digits d used in the writing of all the k**2.
  Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.
  Examples:
  n = 10, d = 1
  the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
  We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.
  nb_dig(25, 1) returns 11 since
  the k*k that contain the digit 1 are:
  1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
  So there are 11 digits 1 for the squares of numbers between 0 and 25.
  Note that 121 has twice the digit 1.
  */

  def nbDig(n: Int, d: Int): Any = {
    (0 to n).flatMap(y => (y*y).toString).count(_.asDigit == d)
    (0 to n)
      .flatMap(y => (y*y)  // traverse and flat into a single array, if not, it will get arrays inside a big vector one
        .toString  // need to be string to be traversable again and check every digit
        .map(_.asDigit))  // need to be converted as digit, if not it's gonna read as alphabetic character
      .count(_ == d)  // count has a map itself, earlier map with as digit it's not necessary
  }

  println(nbDig(10, 1))
}
