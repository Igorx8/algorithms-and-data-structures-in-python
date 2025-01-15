function mergeSort(arr) {
  if (arr.length > 1) {
    const div = Math.ceil(arr.length / 2);
    let left = arr.slice(0, div);
    let right = arr.slice(div);

    mergeSort(left);
    mergeSort(right);

    let i = 0,
      j = 0,
      k = 0;

    while (i < left.length && j < right.length) {
      if (left[i] < right[j]) {
        arr[k++] = left[i++];
      } else {
        arr[k++] = right[j++];
      }
    }

    while (i < left.length) arr[k++] = left[i++];

    while (j < right.length) arr[k++] = right[j++];
  }

  console.log(arr);
  return arr;
}

mergeSort([8, 5, 1, 4, 2, 3]);
