export default function hasValuesFromArray(set, array) {
  // every() checks if all values in array match, then returns true or false
  return array.every((value) => set.has(value));
}
