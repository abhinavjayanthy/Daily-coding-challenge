const RecurringChar = str => {
  let dict = {};
  for (const char of str) {
    if (dict[char] !== undefined) {
      return char;
    } else {
      dict[char] = 1;
    }
  }
  return null;
};

console.log(RecurringChar('acbbac'));
console.log(RecurringChar('abcdef'));
console.log(RecurringChar('aaaaaaa'));
console.log(RecurringChar(''));
