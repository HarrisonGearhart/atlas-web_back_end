export default function getStudentIdsSum(students) {
  return students.reduce((Sum, Student) => Sum + Student.id, 0);
}
