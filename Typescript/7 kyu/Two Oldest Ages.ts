/*
The two oldest ages function/method needs to be completed. It should take an array 
of numbers as its argument and return the two highest numbers within the array. 
The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include 
at least 2 items. If there are two or more oldest age, then return both of them in 
array format.

For example:

two_oldest_ages( 4, {1, 2, 10, 8}, result) // should fill result array with {8, 10}
*/

function twoOldestAges(ages: number[]): number[]{
    var result:number[]= ages.sort((n1,n2) => n1 - n2)
    return result.slice(result.length-2)
}

console.log(twoOldestAges([1,5,87,45,8,8]))