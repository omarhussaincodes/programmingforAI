// A spreadsheet on “Google Sheets” uses letters to label its columns. Column “1”,
// is labeled as “A”, column “26” is labeled as “Z” and column “27” is labeled as
// “AA”. Write a function that takes a single integer input, and outputs its
// corresponding column label.

// Sample Input Expected Output
// 1 - A
// 27  - AA
// 256 - IV
// 5028473 - JZBNU

function fetchColumnLabel(columnNumber) {
  if (typeof columnNumber !== "number" && columnNumber < 1) {
    throw new Error(
      "Invalid column number. Please provide a positive integer for column Number."
    );
  } else {
    let columnLabel = "";

    while (columnNumber > 0) {
      // base 26 or 0-25 or A-Z
      let remainder = (columnNumber - 1) % 26;
      columnLabel = String.fromCharCode(65 + remainder) + columnLabel;
      columnNumber = Math.floor((columnNumber - 1) / 26);
    }

    return columnLabel;
  }
}

console.log(fetchColumnLabel(1));
console.log(fetchColumnLabel(27));
console.log(fetchColumnLabel(65));
console.log(fetchColumnLabel(256));
console.log(fetchColumnLabel(5028473));
console.log(fetchColumnLabel("gibberish")); // throws error
