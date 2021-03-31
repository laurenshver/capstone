function subtotal() {
    toolcosts = document.getElementsByClassName("price");
    costs = [];
    for (let index = 0; index < toolcosts.length; index++) {
        costs.push(parseFloat(toolcosts[index].innerHTML));
    }
    subtotal = costs.reduce((a, b) => a + b, 0);
    return subtotal.toFixed(2);
}

function deposit() {
    subt = document.getElementById("cart-subtotal").innerHTML;
    taxes = parseFloat(subt) * 0.1
    return taxes.toFixed(2);
}

function est_total() {
    subt = document.getElementById("cart-subtotal").innerHTML;
    est = parseFloat(subt);
    return "$" + est.toFixed(2);
}

function save_total(){
    subtotal = document.getElementById("cart-subtotal").innerHTML;
    return subtotal;
}