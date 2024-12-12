'use strict'
// Tehtävä 1
console.log("I'm printing to console!")
// Tehtävä 2
let name = prompt('Syötä nimi')
console.log('Hello' + " " + name + "!")

// tehtävä 4

function sortStudent() {

  var name = document.getElementById("studentName").value;

  var houseNumber = Math.floor(Math.random() * 4) + 1
  var house;

  if (houseNumber === 1) {
    house = 'Gryffindor';
  } else if (houseNumber === 2) {
    house = 'Slytherin';
  } else if (houseNumber === 3) {
    house = 'Hufflepuff';
  } else {
    house = 'Ravenclaw'
  }
  document.getElementById("result").innerHTML = name + " " + "you are in" +
      " " + house + "!"
}

// tehtävä 3
function calculate() {
  var num1 = parseInt(document.getElementById("num1").value)
  var num2 = parseInt(document.getElementById("num2").value)
  var num3 = parseInt(document.getElementById("num3").value)

  var sum = num1 + num2 + num3
  var product = num1 * num2 * num3
  var average = sum / 3;

  document.getElementById("sum").innerHTML = "sum" + " " + sum
  document.getElementById("product").innerHTML = "product" + " " + product
  document.getElementById("Average").innerHTML = "average" + " " +
      average.toFixed(2)
}



function checkLeapYear() {
            // Get the input year from the user
            const year = parseInt(document.getElementById('yearInput').value);
            const resultElement = document.getElementById('result2');

            // Validate input
            if (isNaN(year)) {
                resultElement.textContent = "Please enter a valid year.";
                return;
            }

            // Determine if the year is a leap year
            if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
                resultElement.textContent = `${year} is a leap year.`;
            } else {
                resultElement.textContent = `${year} is not a leap year.`;
            }
        }
        checkLeapYear()

function calculateSquareRoot() {

            if (confirm("Should I calculate the square root?")) {

                const number = parseFloat(prompt("Enter a number:"));

                const resultElement = document.getElementById('result3');


                if (isNaN(number)) {
                    resultElement.textContent = "Please enter a valid number.";
                } else if (number < 0) {
                    resultElement.textContent = "The square root of a negative number is not defined.";
                } else {
                    const squareRoot = Math.sqrt(number);
                    resultElement.textContent = `The square root of ${number} is ${squareRoot}.`;
                }
            } else {

                document.getElementById('result').textContent = "The square root is not calculated.";
            }
        }


        calculateSquareRoot();

