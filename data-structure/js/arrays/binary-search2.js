class VetorOrdenado {
  capacity;
  lastPos = -1;
  values;
  constructor(length) {
    this.values = new Array(length);
    this.capacity = length;
  }

  print() {
    if (this.lastPos === -1) return console.log("O vetor está vazio");
    for (let i = 0; i <= this.lastPos; i++) {
      console.log(i + " -- " + this.values[i]);
    }
  }

  find(value) {
    if (this.lastPos === -1) {
      return -1;
    }

    let i = 0;
    while (i <= this.lastPos) {
      if (this.values[i] === value) return i;
      if (this.values[i] > value) return -1;
      i++;
    }

    return -1;
  }

  bSearch(value) {
    let min = 0;
    let max = this.lastPos;

    let nOps = 0;
    while (min <= max) {
      nOps++;
      let mid = Math.ceil((min + max) / 2);

      if (this.values[mid] === value) {
        console.log(
          `O número de operações para achar o número ${value} na pesquisa binária foi ${nOps} vezes`
        );

        return mid;
      }
      if (this.values[mid] > value) max = mid - 1;
      else min = mid + 1;
    }

    return -1;
  }

  insert(value) {
    if (this.lastPos === this.capacity - 1) {
      console.log("O vetor está cheio");
      return;
    }

    let position = 0;
    for (let i = 0; i <= this.lastPos; i++) {
      position = i;
      if (this.values[i] > value) break;
      if (this.lastPos === i) {
        position = i + 1;
      }
    }

    let aux = this.lastPos;
    while (aux >= position) {
      this.values[aux + 1] = this.values[aux];
      aux--;
    }

    this.values[position] = value;
    this.lastPos = this.lastPos + 1;
  }

  remove(value) {
    if (this.lastPos === -1) {
      console.log("O vetor está vazio");
      return;
    }

    const position = this.find(value);

    if (position !== -1) {
      for (let i = position; i <= this.lastPos; i++) {
        this.values[i] = this.values[i + 1];
      }
      this.lastPos = this.lastPos - 1;
    }
  }
}

const vetor = new VetorOrdenado(5);
vetor.print();
vetor.insert(2);
vetor.insert(8);
vetor.insert(3);
vetor.insert(1);
vetor.insert(6);
vetor.print();
vetor.insert(4);
console.log(vetor.find(5));
vetor.remove(1);
vetor.remove(8);
vetor.insert(15);
vetor.insert(13);
vetor.print();
console.log(vetor.bSearch(15));

const vetor2 = new VetorOrdenado(100);
for (let i = 0; i < 100; i++) {
  vetor2.insert(i);
}

console.time("bsearch");
console.log(vetor2.bSearch(33));
console.timeEnd("bsearch");

console.time("linear-search");
console.log(vetor2.find(33));
console.timeEnd("linear-search");
