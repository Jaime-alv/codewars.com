package codewars.kyu7

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

  println(accum("hello"))
}
