/**
 * Remove items at positions which are multiples of 2 or 3.
 * @param {Array<number>} inputList - List of integers.
 * @returns {Array<number>} - Modified list with items removed.
 */
function removeMultiples(inputList) {
  return inputList.filter(
    (_, index) => (index + 1) % 2 !== 0 && (index + 1) % 3 !== 0,
  );
}

/**
 * Process the input list and handle errors.
 * @param {Array<number>} inputList - List of integers.
 * @returns {Array<number>} - Modified list or throws an error.
 * @throws Will throw an error if the list length is not a multiple of 10.
 */
function processList(inputList) {
  if (!Array.isArray(inputList)) {
    throw new Error("Input must be an array");
  }

  if (inputList.some(isNaN)) {
    throw new Error("All elements in the list must be numbers");
  }

  if (inputList.length % 10 !== 0) {
    throw new Error("List length must be a multiple of 10");
  }

  return removeMultiples(inputList);
}

module.exports = processList;
