package codewars.kyu7

object kyu7 {
  def main(args: Array[String]): Unit = {
    println(vowel_count("There is something"))
  }

  def vowel_count(str: String): Int = {
    str.toLowerCase().replaceAll("[^aeiou]", "").length()
  }
}
