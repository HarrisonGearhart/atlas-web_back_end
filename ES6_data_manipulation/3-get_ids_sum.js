export default function getStudentIdsSum(students) {
  // reduce function
  return students.reduce((Sum, Student) => Sum + Student.id, 0);
}
