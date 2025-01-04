const task1 = document.querySelector("#task1");
const task2 = document.querySelector("#task2");
const task3 = document.querySelector("#task3");
const task4 = document.querySelector("#task4");
const task5 = document.querySelector("#task5");

console.log(wizards);

task1.textContent = wizards.filter(e => e.age < 100).length

const initialValue = 0;
task2.textContent = wizards.reduce((accumulator, currentValue) => accumulator + currentValue.age, initialValue) / wizards.length

let maxAge = wizards[0]
wizards.forEach(e => e.age > maxAge.age ? maxAge = e : {})
task3.textContent = maxAge.name

let maxXp = wizards[0]
wizards.forEach(e => e.xp > maxXp.xp ? maxXp = e : {})
task4.textContent = maxAge == maxXp

let fireSpells = []
wizards.forEach(e => e.spells.forEach(s => s.includes('Fire') ? fireSpells.push(s) : {}))
task5.textContent = fireSpells