export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw new TypeError('Size must be a number');
    }
    if (typeof location !== 'string') {
      throw new TypeError('Location must be a string');
    }
    // properties
    this._size = size;
    this._location = location;
  }

  // getters
  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  // returm size and location
  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
