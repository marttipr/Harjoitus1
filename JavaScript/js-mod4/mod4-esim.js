'use strict'
console.log('script start')

async function fetchImages() {
  const response = await fetch(pics.json())
  console.log('pic response', response);

  if (response.ok) {
    const pics = await response.json();
    console.log('kuvat', pics)
    for (const pic of pics){
      const imgElem = document.createElement('img')
      imgElem.src = pic.address;
      imgElem.alt = pic.description
      document.querySelector('#images').append(imgElem)
    }
  }
}
fetchImages()


/// Chuck Norris api esimerkki
async function getAJoke(){
  const outputElem = document.querySelector('#joke')
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random')

  console.log('joke response', response)
    if(response.ok) {
    // status koodi ok (2xx)
      throw new Error(response.status);

       }
  const joke = await response.json()
   console.log('Vitsi:', joke.value)
   outputElem.textContent = joke.value


  } catch (error) {
    console.log(error);
    outputElem.textContent = "vitsin haku epäonnistui"
  }
}

document.querySelector('#get-joke')
.addEventListener('click', getAJoke);


console.log('script end')