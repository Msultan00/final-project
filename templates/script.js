function calculateResult() {
    var expression = document.getElementById('expression').value;
    var result = eval(expression);

    // Check if the result is negative for subtraction operation
    if (expression.includes('-') && result < 0) {
        result = Math.abs(result); // Get the absolute value
    }

    document.getElementById('expression').value = result;
}
