package codewars.kyu6

object ConvertStringToCamelCase extends App{
  /*
  Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
  within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
  often referred to as Pascal case).
  Examples
  "the-stealth-warrior" gets converted to "theStealthWarrior"
  "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
   */

  def convertString(str: String): String = {
    "[-_]([a-zA-Z])".r.replaceAllIn(str, m => m.group(1).toUpperCase())
  }

  println(convertString("the-stealth-warrior"))
}
