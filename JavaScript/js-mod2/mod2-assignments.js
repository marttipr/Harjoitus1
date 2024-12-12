'use strict'
console.log('Assignments:');

console.log("tehtävä 1")

let numbers= []

for (let i = 0; i<5; i++) {

  let num = prompt(`Enter number ${i+1}:`)
  numbers.push(Number(num));
}
console.log("Numbers in reverse order:")
for(let i = numbers.length - 1; i>=0;i--){
  console.log(numbers[i]);
}


console.log('Tehtävä 2')
const nlist = document.querySelector('.namelist');
console.log(nlist);
let inner = '';

const num = parseInt(prompt('Please give me a number of participants: '));
const names = [];

function askNames() {

  for (let i = 0; i < num; i++) {
    console.log(i);
    let name = prompt('Please give me a name');
    names.push(name);
  }
  console.log(names);
}

function printNames() {

  console.log(names.length);

  for (let i = 0; i < names.length; i++) {
      console.log(names[i]);
      inner += `<li>${names[i]}</li>`
  }
  console.log(inner);
  nlist.innerHTML = inner;


  for (let name of names) {
    console.log(name);

    let liElement = document.createElement('li');

    liElement.innerHTML = name;
    nlist.appendChild(liElement);
  }
}

askNames();
printNames();

console.log('Tehtävä 3')

const dlist = document.querySelector('.dogName')
console.log(dlist)

const dogs = []

function displaydogNames() {
  for(let i = 0; i < 6; i++){
    let dname = prompt('Give dog names')
    dogs.push(dname)
  }
  dogs.sort().reverse()

  let ul = document.createElement('ul')
  dogs.forEach(dname => {
    let li = document.createElement('li');
    li.textContent = dname;
    ul.appendChild(li)
  })
  document.body.appendChild(ul);
}
displaydogNames()

console.log('Tehtävä 4')


function nums(){
  const numlist = []
  let input;
do {
  input = parseFloat(prompt('Enter a number, 0 to stop'))
  if (input !==0) {
    numlist.push(input)
  }
}while (input !==0)
  numlist.sort((a,b) => b-a);
  console.log("numbers from largest to smallest")
  console.log(numlist)
}
nums()

console.log('tehtävä 5')
function main() {
  const numero = new Set();
  const orderedNumbers = []

  console.log('Enter number, Same number stops the program')

  while(true){
    const input = prompt('Enter a number')
    if(input == null){
      console.log('Code canceled')
      break;
    }
    const num1 = Number(input)
    if (isNaN(num1)){
      console.log('Invalid input')
      continue;
    }
    if (numero.has(num1)) {
      console.log(`The number ${num1} has been entered, stopping program`)
      break;
    }
    numero.add(num1);
    orderedNumbers.push(num1)

  }
  console.log('All numbers in ascending order')
  console.log(orderedNumbers.sort((a,b) => a-b));
}
main();

function rollDice() {
            // Generate a random dice roll between 1 and 6
            return Math.floor(Math.random() * 6) + 1;
        }

        function main2() {
            const resultsElement = document.getElementById('rollResults');
            let roll;

            // Roll the dice until a 6 is rolled
            do {
                roll = rollDice();
                const listItem = document.createElement('li');
                listItem.textContent = `You rolled: ${roll}`;
                resultsElement.appendChild(listItem);
            } while (roll !== 6);
        }

        // Run the main program when the page loads
        main2();






