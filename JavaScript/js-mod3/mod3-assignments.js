'use strict'
// tehtävä 1
document.getElementById("target").innerHTML = `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
`;

// tehtävä 2
const target2 = document.getElementById('target2');

const firstItem = document.createElement("li");
firstItem.textContent = "First item";
target2.appendChild(firstItem);


const secondItem = document.createElement("li");
secondItem.textContent = "Second item";
target2.appendChild(secondItem);


const thirdItem = document.createElement("li");
thirdItem.textContent = "Third item";
target2.appendChild(thirdItem);

// tehtävä 3

const names = ["John", "Paul", "Jones"];


const target3 = document.getElementById("target3");


let listItems = "";
for (let i = 0; i < names.length; i++) {
    listItems += `<li>${names[i]}</li>`;
}


target3.innerHTML = listItems;

// tehtävä 4

const students = [
  { id: "2345768", name: "John" },
  { id: "2134657", name: "Paul" },
  { id: "5423679", name: "Jones" }
];

const target4 = document.getElementById("target4");

students.forEach(student => {
  const option = document.createElement("option");

  option.value = student.id;
  option.textContent = student.name;

  target4.appendChild(option);
});
// tehtävä 6
const button = document.getElementById("button")
button.addEventListener("click", () =>{
  alert("Button Clicked");
})

// tehtävä 7

const trigger = document.getElementById("trigger")
const target7 = document.getElementById("target7")

trigger.addEventListener("mouseover", () =>{
  target7.src ="pic/picB.jpg";
})

trigger.addEventListener('mouseout',()=>{
  target7.src="pic/picA.jpg"
})
