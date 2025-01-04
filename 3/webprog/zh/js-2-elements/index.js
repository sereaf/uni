const elements = ["anemo", "geo", "electro", "dendro", "hydro", "pyro", "cryo"];

const correct = [
  ["anemo", "anemo", "pyro", "pyro"],
  ["geo", "electro", "electro", "geo"],
  ["dendro", "hydro", "dendro", "hydro"],
  ["cryo", "cryo", "cryo", "cryo"]
];

rows = document.querySelector('#rows')
rows_output = document.querySelector('#rows-output')
cols = document.querySelector('#cols')
cols_output = document.querySelector('#cols-output')

rows.addEventListener('input', (e => rows_output.textContent = e.target.value))
cols.addEventListener('input', (e => cols_output.textContent = e.target.value))


table = document.querySelector('table')
button = document.querySelector('button')
ctrl = document.querySelector('#controls')

cells = null
button.addEventListener('click', (e => {
  str = ''
  for (let i = 0; i < rows.value; i++) {
    str = str.concat('<tr>')
    for (let j = 0; j < cols.value; j++) {
      str = str.concat(`<td id='${i + ',' + j}'></td>`)
    }
    str = str.concat('</tr>')
  }
  table.innerHTML = str
  ctrl.style = 'display: none'
  cells = document.querySelectorAll('td')
  cells.forEach(el => {
    el.addEventListener('click', (e => {
      if (el.classList.contains('correct')) {
        return;
      }
  
      console.log(e.target.id)
      if (el.style.backgroundImage == '') {
        el.style.backgroundImage = `url('${elements[0]}.webp')`
      } else {
        let ind = elements.findIndex((element) => element == el.style.backgroundImage.split('"')[1].split('"')[0].split('.')[0]) + 1;
        if (ind > elements.length - 1) {
          el.style.backgroundImage = ''
        } else {
          el.style.backgroundImage = `url('${elements[ind]}.webp')`
        }
      }
      if (rows.value == 4 && cols.value == 4) {
        x = el.id.split(',')[0]
        y = el.id.split(',')[1]
        if (el.style.backgroundImage.includes(correct[x][y])) {
          el.classList.add('correct')
        } 
      }
    }))
  });
}))





