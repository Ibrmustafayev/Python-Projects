🏛️ Simplifier v.Roman
Simplifier v.Roman is a Python-based mathematical expression evaluator specifically designed for Roman Numerals. Unlike standard calculators, this engine parses strings containing Roman numerals, respects the mathematical order of operations ($PEMDAS$), and handles nested parentheses—all while staying true to the constraints of the Roman numeral system.

🚀 Features
-Roman to Decimal Conversion: Translates Roman strings (e.g., XIV) into integers (14) using standard subtractive logic.
-Decimal to Roman Conversion: Converts calculated results back into Roman numerals for the user.
-Expression Evaluation: Supports addition (+), subtraction (-), multiplication (*), and division (/).
-Order of Operations: Implements logic to prioritize multiplication and division before addition and subtraction.
-Parentheses Support: Recursively solves expressions inside brackets () first.
-Historical Constraints: Returns error flags (!!!) for results that cannot be expressed in Roman numerals, such as zero, negative numbers, or fractions.

🛠️ How It Works
The system is divided into four distinct logical modules:
1. The Interpreter (interpret)This module handles the translation. It includes a validation check to ensure no symbol is repeated more than three times (e.g., IIII is invalid) and correctly calculates subtractive pairs like IV, XC, and CM.
2. Math Engine (operations)Contains the logic for basic arithmetic. It includes specific "Roman-safe" guards:Division: Only returns a result if the quotient is an integer.Subtraction: Only returns a result if the total is greater than zero.
3. Logic & Precedence (order)This is the "brain" of the calculator. It treats the expression as a list of tokens and iterates through them to solve high-priority operations first. It uses a "find-and-replace" method where the operator and its surrounding numbers are replaced by the single result of that operation.
4. Expression Parser (main)The parser breaks down the user's input string into a list format that the math engine can understand, separating numerals from operators and brackets.

⚠️ Limitations
As it adheres to the classical Roman system:
Maximum Value: Standardly supports up to MMM (3,000).
No Zero: Roman numerals have no representation for 0.
No Negatives: Calculations resulting in less than 1 will trigger an error message.
Integers Only: Fractions or floating-point results are not supported.
