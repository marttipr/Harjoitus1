'use strict'
console.log('moro')

// taulukot eli arrays
const items= [1,2,3,{name:'Martti'},[1,2,3], 'merkkijono']
console.log(items)

// alkioo viitataan perus indeksillä
console.log(items[0]);
// alkion arvoa voidaan muuttaa tai lisätä indeksin avulla
items[0] = 99;
console.log(items)
items[9]= 'Darwin Nunez'

// välissä on nyt ns määrittelemätön arvo/alkio eli undefined
console.log(items[6]);
console.log('taulukon pituus:', items.length)

// taulukoiden läpikäynti loopin avulla
console.log('--------------------------')
console.log('Perinteinen for-i looppi');
for (let i = 0; i < items.length; i++) {
  console.log(i, items[i]);
}


console.log('-----------------------')
console.log('Läpikäynti for/in rekenteella, jolla saadaan avain/indeksi ja arvo')
for(const index in items) {
  console.log(index, items[index]);
}

console.log('----------------------------------------------')
console.log('Läpikäyti for/of rakenteella, jolla saadaan arvot')
for (const item of items) {
  // if lause jossa  tutkitaa onko alkio undefined
  if (item != undefined) {
   console.log(item);
  }

}

  console.log('--------------------------')

const names = ['Frank Ocean', 'Scott Mctominay','Jasmine', 'Don Toliver']
const ages = [37,27,101,30]
for (let name of names) {
  console.log(`Name:${name}`);
}

/*
sort() sorts the array alphabetically
reverse() reverses the items in the array in reverse order
shift() deletes and returns the 1st item in the array
pop() deletes and returns the last item in the array
push(value) adds the value at the end of the array, multiple values separated by commas
includes(value) checks whether the array contains the given value
 */
names.sort();
console.log(names)
names.reverse()
console.log(names)

// ei toimi numeroiden kanssa

ages.sort()
console.log(ages)

// tämä toimii numeroiden kanssa

ages.sort((a, b)=> a - b)
console.log(ages)
ages.sort((a, b)=> b - a)
console.log(ages)

// lisätään nimiä
names.push('Mohammed Salah')
const newLength = names.push('Trent Alexander-Arnold')
console.log(names)
console.log('Taulukon pituus:', newLength)
// lisätään taulukon alkuun

names.unshift('Ibrahima Konate')
console.log(names)
// poistetaan taulukon eka ja otetaan muuttujaan talteeb
const firstName = names.shift()
console.log('Poistettiin:', firstName)
console.log(names)
// etsitään onko taulukossa ko. arovo palauttaa true/false

console.log(names.includes('Jasmine'))
// object literal eli olio
// samankaltainen kun pythonin sanakirja

const duck = {
  name: 'aku',
  age: 313
}

console.log(duck)
console.log(duck['age'])

// muutetaan arvoja
duck['age'] = 36;
duck.name = "Aku Ankka"
console.log(duck)




// lisätään uusi ominaisuus
duck.profession = 'Working like a duck'
console.log(duck);

// tietyn ominaisuuden arvon hakeminen
let moikkaus = `Moikkamoi ja tänne muuttuja ${duck.name}`;
let moikkaus2 = duck.name + 'on'+ duck.age + 'ikäinen ja motto:' +  duck.profession;

// metodin luominen olioon ns. nimeämättömänä funktiona

const duck2 = {
  name: 'Iiines',
  age: 34,
  getInfo: function(){
    return this.name + 'on' + this.age + '-vuotias';

  }
}
console.log(duck2.getInfo());


// JS funktiot

// perinteinen funktio määrittelu
function greet(name) {
  console.log(`Greet ${name}`);
  return;
}

// function expression. funktio joka on anonyymi mutta tallennetaan muuttujaan
const greet2 = function(name){
  console.log(`Greetings again ${name}!!!`)
}

const greet3 = (name) => {
  console.log(`Greetings a third time ${name}!!!`)
}
greet('Martti')
greet2('Martti')
greet3('Martti')

const nimi = 'Trent'

function logName(){
  console.log(name);
}

logName();
