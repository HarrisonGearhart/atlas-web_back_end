export default function getStudentsByLocation(students, city) {
  // validate array
  if (Array.isArray(students)) {
    // filter function
    return students.filter((person) => person.location === city);
  }
  //linter expects a return value at the end of the function
  return [];
}
