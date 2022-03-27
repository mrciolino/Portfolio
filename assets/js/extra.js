// wait until after everything is loaded to reorder the portfolio
document.addEventListener('DOMContentLoaded', function () {
    order_portfolio();
});

function order_portfolio() {

    // sort them
    // 0 : Transformers
    // 1 : xEval
    // 2 : sisr
    // 3 : deepfake
    // 4 : portfolio
    // 5 : jobtag
    // 6 : sot
    // 7 : dnd
    // 8 : wikipedia
    // 9 : poltics
    // 10 : crowd
    // 11 : testing

    // declare variables
    var copied_jumbotrons = [];
    var order = [10, 0, 1, 2, 5, 8, 6, 7, 4, 3, 9, 11];
    var jumbotrons = document.getElementById("portfolio_array").children;
    var portfolio_array = document.getElementById("portfolio_array");

    // copy the elemnts into a new array
    for (var i = 0; i < jumbotrons.length; i++) {
        copied_jumbotrons.push(jumbotrons[i].cloneNode(true));
    }

    // put them in the right order
    portfolio_array.innerHTML = '';
    for (var i = 0; i < order.length; i++) {
        portfolio_array.appendChild(copied_jumbotrons[order[i]]);
    }
}