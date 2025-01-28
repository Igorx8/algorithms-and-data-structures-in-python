function partition(arr, start, end) {
  let pivot = arr[end];
  let i = start - 1;

  for (let j = start; j < end; j++) {
    if (arr[j] <= pivot) {
      i++;
      let aux = arr[j];
      arr[j] = arr[i];
      arr[i] = aux;
    }
  }
  let aux = arr[end];
  arr[end] = arr[i + 1];
  arr[i + 1] = aux;
  return i + 1;
}

function quickSort(arr, start, end) {
  if (start < end) {
    pivot = partition(arr, start, end);
    quickSort(arr, start, pivot - 1);
    quickSort(arr, pivot + 1, end);
  }

  return arr;
}

let array = [3, 1, 5, 6, 8, 2, 4];
console.log(quickSort(array, 0, array.length - 1));
