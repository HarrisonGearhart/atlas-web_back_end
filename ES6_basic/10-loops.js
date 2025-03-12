export default function appendToEachArrayValue(array, appendString) {
  const NewArray = array;
  for (const x of array) {
    NewArray.push(appendString + x);
  }
    
  return array;
}
