export default function createInt8TypedArray(length, position, value) {
  // position validation
    if (position < 0 || position >= length) {
      throw Error('Position outside range');
    }
  // arraybuffer
  const buffer = new ArrayBuffer(length);
  // view the buffer as int8
  const view = new DataView(buffer);
  // set Int8 value at that index position givem
  view.setInt8(position, value);
  // return the new view of the buffer
  return view;
}
