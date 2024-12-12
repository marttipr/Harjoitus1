'use strict'
const h1ELem=document.querySelector('h1')
console.log(h1ELem);


const title = h1ELem.textContent
h1ELem.textContent = title + ' + lisäys otsikkoon'
h1ELem.style.fontSize = '22px';
h1ELem.classList.add('text');
// piilotetaan elementti ccs:n avulla
h1ELem.classList.add('hidden')
// näytetään taas
h1ELem.classList.remove('hidden')


// koko bodyn piilotus parentin avvulla
//h1ELem.parentElement.classList.add('hidden')

// lisätään sisältöä sivulle
const pElem = document.createElement('p')
document.querySelector('main').append(pElem)
pElem.textContent = 'Uusi kappale by JS!';

// haetaan viittaus useampaan elementtiin/nodeen kerralla
const paragraphs = document.querySelectorAll('p')
//console.log(paragraphs)
paragraphs[2].textContent = 'Kolmas kappale'
// iteroidaan kappaleet läpi
/*
for (const p of paragraphs) {
 p.textContent = 'Päivitetty!'
}
*/

// tehdään järjestetty lista jossa 5 alkiota
const olElement = document.createElement('ol')
const listContents = ['kynä', 'kumi', 'reppu', 'pulpetti']

const listDiv = document.querySelector('#list')

function renderList(){
  for (let i = 0; i < listContents.length; i++){
  const newLi = document.createElement('li')
  newLi.textContent = listContents[i]
  olElement.append(newLi)
}
 listDiv.append(olElement)

}
//renderList(listContents)
//listContents.sort()
//listContents.push('tietskari')
//renderList(listContents)
//listContents.sort()


// selaimen "sijainti" (URL)
//window.console.log(window.location.href)
// siirrytään johonkin toiseen osoitteeseen
// window.location.href =='https://www.google.fi';

const printButton = document.querySelector('#print')
printButton.addEventListener('click', function(event)  {
console.log('Print and sort button clicked', event)
listContents.sort()
renderList(listContents)
})


// tapahtuma käsittely eli  eventit

const addButton = document.querySelector('#add')
// asetetaan napille tapahtumankäsitteliä click eventille
addButton.addEventListener('click', () => {
  const newItem = window.prompt('Lisää listaan jotain')
  listContents.push(newItem)
  renderList(listContents);
})

// Hiiritapahtumia
document.addEventListener('mousemove', function (event) {
  // console.log(event)
  document.querySelector('#output').textContent = `Hiiren 
  osoittimen koordinaatit: ${event.clientX}, ${event.clientY}`;
  if (event.clientY>300) {
    h1ELem.classList.remove('hidden')
  }
});

h1ELem.addEventListener('mouseenter', function() {
  h1ELem.classList.add('hidden');
})

// näppiseventit


const keyLog =[]
document.addEventListener('keypress', function(event){
  // console.log('näppäin:',   event.key)
  keyLog.push(event.key);
  console.log('logi', keyLog);
  if (event.key === 'h') {
    if (!hidden) {
      document.querySelector('body').classList.add('hidden')

    } else {
      document.querySelector('body').classList.remove('hidden')
    }
    'hidden' = !'hidden'
  }
});