function getMinMachines(start: number[], end: number[]): number {
  let pairs: { start: number; end: number }[] = [];

  pairs = start
    .map((element, index) => ({
      start: element,
      end: end[index],
    }))
    .sort((a, b) => a.start - b.start);

  let result = 1;
  const count = pairs.length;
  const stack: { start: number; end: number }[] = [];
  const machine = [pairs[0]];
  let i = 1;

  while (i < count) {
    if (pairs[i].start < machine[result].start) {
      result += 1;
      machine.push(pairs[i]);
    } else {
      stack.push(pairs[i]);
    }
    i++;
  }

  return result;
}

function getMinMachines2(start: number[], end: number[]): number {
  let pairs: { start: number; end: number; isRan: boolean }[] = [];

  pairs = start
    .map((element, index) => ({
      start: element,
      end: end[index],
      isRan: false,
    }))
    .sort((a, b) => a.start - b.start);

  let result = 0;
  const count = pairs.length;

  while (true) {
    const taskIndex = pairs.findIndex((pair) => !pair.isRan);

    if (taskIndex !== -1) {
      result += 1;
      pairs[taskIndex].isRan = true;
      let endTask = pairs[taskIndex].end;

      for (let i = taskIndex; i < count; i++) {
        if (pairs[i].start > endTask && !pairs[i].isRan) {
          pairs[i].isRan = true;
          endTask = pairs[i].end;
        }
      }
    } else {
      break;
    }
  }

  return result;
}
