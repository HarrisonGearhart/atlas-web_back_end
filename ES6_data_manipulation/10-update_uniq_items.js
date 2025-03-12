export default function updateUniqueItems(groceryListMap) {
  // map validation
  if (!(groceryListMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  // For each entry of the map where the quantity is 1, update the quantity to 100
  groceryListMap.forEach((value, key) => {
    if (value === 1) {
      groceryListMap.set(key, 100);
    }
  });
}
