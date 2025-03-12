import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);

    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    // properties
    this._floors = floors;
  }

  // getters
  get floors() {
    return this._floors;
  }

  get sqft() {
    return this._sqft;
  }

  // evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
