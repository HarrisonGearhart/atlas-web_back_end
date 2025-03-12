export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }

    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    // properties
    this._name = name;
    this.code = code;
  }

  // getter and setters
  get name() {
    return this._name;
  }

  set name(NewName) {
    if (typeof NewName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = NewName;
  }

  get code() {
    return this._code;
  }

  set code(NewCode) {
    if (typeof NewCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = NewCode;
  }

  // displayFullCurrency method
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
