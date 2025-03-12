export default function getListStudentIds(objects) {
  // If the argument is not an array, the function is returning an empty array.
  if (!Array.isArray(objects)) {
    return [];
  }
  
  // returns an array of ids from a list of object
  return objects.map((student) => student.id);
}
