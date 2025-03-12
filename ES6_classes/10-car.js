export default class Car {
  constructor(brand, motor, color) {
    // attributes
    this._brand = brand;
    this._motor = motor;
    this._color = color; 
  }
  // cloneCar method
  cloneCar() {
    return new this.constructor();
  }
}
