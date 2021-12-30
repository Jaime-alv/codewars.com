/*
Your function takes two arguments:
current father's age (years)
current age of his son (years)

Сalculate how many years ago the father was twice as old as his son 
(or in how many years he will be twice as old).
*/


// "Testing for dad's age: 55 and son's age: 30"

function twiceAsOld(dadYearsOld: number, sonYearsOld: number): number {
    var result:number = dadYearsOld - (sonYearsOld * 2);
    if (result < 0) return result * -1;
    else return result;
   }

console.log(twiceAsOld(55, 30));