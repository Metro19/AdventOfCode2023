/// Advent of Code 2023 Day 1 Star 1
/// Calculate the total score by the first number in the string and the last number in the string.

use std::fs;

///
/// Read from file and score everything.
///
pub fn main() {
    // constant
    let filepath: &str = "data.txt";

    // Setup array
    let mut vec: Vec<&str> = Vec::new();

    // read file
    let contents = fs::read_to_string(filepath)
        .expect("Was not able to read the file. :(");

    // input loop
    for item in contents.split("\r\n") {
        vec.push(item);
    }

    let mut score: u32 = 0;

    // iterate through all items
    for line in vec {
        score += score_str(line);
    }

    println!("{}", score);
}

///
/// Score an individual string.
/// str: String to score
/// Returns: Score of individual string.
///
fn score_str(str: &str) -> u32 {
    // init vars
    let mut first_val: u32 = 99;
    let mut last_val: u32 = 99;

    // check each letter
    let chars: Vec<char> = str.chars().collect();
    for letter in chars {
        if letter.is_numeric() && first_val == 99 {
            first_val = letter.to_digit(10).expect("That was not a number?");
            last_val = letter.to_digit(10).expect("That was not a number?");
        }
        else if letter.is_numeric() {
            last_val = letter.to_digit(10).expect("That was not a number?");
        }
    }

    return (first_val * 10) + last_val;
}