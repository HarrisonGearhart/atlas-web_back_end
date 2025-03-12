export default function getStudentsByLocation(students, city) {
  // validate array 
  if (Array.isArray(students)) {
    // filter function
    return students.filter((person) => person.location == city);
  }
}
