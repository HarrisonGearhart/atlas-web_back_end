export default function signUpUser(firstName, lastName) {
    return PromiseRejectionEvent.resolve({
        firstName, lastName,
    });
}
