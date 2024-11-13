  'use strict';

// arvotaan testinumero
 const randomNumber = Math.random()

  // else haaran testaamista vare´ten kovakoodattu arvo
  // const randomNumber = 0.503
  console.log('arvottu numero', randomNumber)

// ehtolause, ehdon täytyy olla aina true/False
// 50 % todennäköisyys
if (randomNumber < 0.495) {
  console.log('kruuna')
} else if(randomNumber > 0.505){
  console.log('klaava')
} else {
  console.log('Kolikko jää kantilleen')
}
console.log('suoritus jatkuu ehtolauseen jälkeen ')

  const cabinClass = prompt('Enter the cabin class (A/B/C).');
  switch (cabinClass) {
    case 'A':
      console.log('Top deck cabin with window.');
      break;
    case 'B':
      console.log('Top deck cabin without window.');
      break;
    case 'C':
      console.log('Windowless cabin under the car deck.');
      break;
    default:
      console.log('Invalid cabin class.');
  }


  // TOISTORAKENTEET
  // kuinka monta heittoa menee että kolikko jää kyljelleen
  const throwCounts = [];
  for (let i = 0; i < 100; i++) {
    let throwCount = 0
    let stillThrowing = true;
    while (stillThrowing) {

      const randomNumber = Math.random();
      throwCount++
      if (randomNumber < 0.495) {
        console.log('kruuna');
      } else if (randomNumber > 0.505) {
        console.log('klaava');
      } else {
        console.log('Kolikko jää kantilleen');
        console.log('Heittojen lukumäärä', throwCount)
        throwCounts.push(throwCount);
        stillThrowing = false
      }
    }
  }

 console.log('Heittojen lukumäärät', throwCounts)
// lasketaan heittomäärien summa for-silmukalla
  let sum =0;
  for (let i=0; i<throwCounts.length; i++){
    sum += throwCounts[i]
  }
  console.log('heittojen ka', sum/throwCounts.length)