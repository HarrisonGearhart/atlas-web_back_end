export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const grade = newGrades.find((gr4de) => gr4de.studentId === student.id);
    return {
      ...student, grade: grade ? grade.grade : 'N/A',
    };
  });
}
