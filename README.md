# Longest Substring App

This Django application calculates the length of the longest substring without repeating characters, based on the logic implemented in an algorithm derived from a [LeetCode problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/). The solution to the problem can also be found in my [LeetCode repository](https://github.com/Mike014/LeetCode-Solutions/tree/main/Longest_Substring_Without_Repeating_Characters).

## Features
- **Algorithm Integration:** The logic for calculating the longest substring without repeating characters is implemented in `algorithm.py` and integrated into the Django app through the `views.py` file.
- **User Input:** A simple HTML form allows users to input a string and calculate the result.
- **Database Storage:** Results are saved in the database for record-keeping and debugging purposes.

## Debugging Process
Initially, the app did not return the correct substring length. Here's the step-by-step debugging process that helped resolve the issue:

1. **Algorithm Verification:**
   - The logic in `algorithm.py` was independently verified using unit tests to ensure correctness.

2. **Django Debugging:**
   - The `DEBUG` setting in `settings.py` was set to `TRUE`:
     ```python
     DEBUG = True
     ```
   - Debugging messages were added in `views.py` to trace request methods and ensure the correct flow of data:
     ```python
     print("Received Request: ", request.method)
     ```

3. **Root Cause Analysis:**
   - After testing, the issue was identified in the `HTML` template. The problem was in the line:
     ```html
     <p>Longest Substring Length: {{ result.length_of_longest_substring }}</p>
     ```
     - The variable name did not match the field in the `models.py` file.

4. **Fix:**
   - The incorrect variable name was corrected to:
     ```html
     <p>Longest Substring Length: {{ result.length_of_longest_substring }}</p>
     ```

## Files in the Project

- **`algorithm.py`:** Contains the logic for calculating the longest substring without repeating characters.
- **`views.py`:** Integrates the algorithm with Django views and handles user requests.
- **`models.py`:** Defines the `SubstringResult` model for storing input strings and their corresponding results.
- **`templates/substring/index.html`:** The HTML template for the user interface.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mike014/LongestSubstringApp.git
   cd LongestSubstringApp