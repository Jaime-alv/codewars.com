package codewars.kyu6

import scala.annotation.tailrec

object BuildAPileOfCubes extends App{
  /*
  Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of
  n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
  You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to
  build?
  The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the
  integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
  Examples:
  findNb(1071225) --> 45
  findNb(91716553919377) --> -1
   */

  @tailrec
  def findNb(m: Long, n: Int = 0, o: Long = 0): Int = {
    if (o == m) n - 1
    else if (o > m) -1
    else findNb(m, n + 1, math.pow(n, 3).toLong + o)
  }

  def power(y: Int): Int = {
    if (y == 1) y
    else math.pow(y, 3).toInt + power(y - 1)
  }

  println(findNb(1071225))
  println(power(45))
  print(findNb(91716553919377L))
}
