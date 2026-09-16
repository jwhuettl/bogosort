
function buildArray(size) {
  // could use spread operator but i feel like it hides too much
  // return [...Array(size).keys()]
  return Array.from(Array(size).keys());
}

function fyShuffle(list) {
  for (let i = (size - 1); i >= 0; i--) {
    let j = Math.floor(Math.random() * (size - 1));

    let tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }

  return list;
}

function bogosort(input) {

  sorted = true;
  attempts = 0;

  do {

    sorted = true;

    att = fyShuffle(input);

    // console.log(att);

    att.forEach(function (val, index) {
      if (val != index) {
        sorted = false;
      }
    })

    attempts += 1;

  } while (!sorted);

  // return [att, attempts];
  return attempts;

}

let size = parseInt(process.argv[2]);
let input = fyShuffle(buildArray(size));
let total = bogosort(input);
console.log("Attempts: ", total);
