function merge(nums1, m, nums2, n) {
  let theMergeArray1 = nums1.slice(0, m);
  let theMergeArray2 = n > 0 ? nums2.slice(0, n) : [];
  let mergeTwoList = theMergeArray1.concat(theMergeArray2);
  for (let i = 0; i < m + n; i += 2) {
    let theTerm = mergeTwoList[i + 1];
    if (mergeTwoList[i] > mergeTwoList[i + 1]) {
      mergeTwoList[i + 1] = mergeTwoList[i];
      mergeTwoList[i] = theTerm;
    }
  }
  console.log('mergeTwoList',mergeTwoList)
}

let nums1 = [1, 2, 3, 0, 0, 0];
let nums2 = [2, 5, 6];
let m = 3;
let n = 3;

merge(nums1, m, nums2, n);
