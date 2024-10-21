const L = 4;
const H = 5;
const T = "E";

function createArray(H, L) {
  return Array(H).fill(Array(L).fill(0));
}

const arrChar = [];
for (let x = 0; x <= 27; x++) {
  arrChar.push(createArray(H, L));
}

let TOTALROW = [
  " #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ",
  "# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ",
  "### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ",
  "# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ",
  "# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ",
];

// for (let i = 0; i < H; i++) {
TOTALROW.forEach((ROW, i) => {
  const arrArt = ROW.split("");
  for (let j = 0; j < arrChar.length; j++) {
    arrChar[j][i] = arrArt.splice(0, 4);
  }
});
// }

function writeTextArt(arrArt, T, H) {
  const result = [];
  for (let i = 0; i < T.length; i++) {
    const index = getIndexArt(T[i]);
    result.push(arrArt[index]);
  }

  for (let j = 0; j < H; j++) {
    let resultString = "";
    for (let i = 0; i < result.length; i++) {
      resultString += result[i][j].join("");
    }
    console.log(resultString);
  }
}

function getIndexArt(T) {
  const asciiCode = T.toLowerCase().charCodeAt(0);
  if (asciiCode >= 97 && asciiCode <= 122) {
    return Math.abs(97 - asciiCode);
  }
  return 26;
}

writeTextArt(arrChar, "$a", H);
