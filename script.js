let output = document.getElementById("output-screen");
let previousOutput = ""; 

function show(value){
    if (value === 'sqrt') {
        output.value += '√';
    } else if (value === 'ans') {
        output.value += previousOutput; 
    } else if (value === '%') {
        // Calculate percentage
        output.value = parseFloat(output.value) / 100;
    } else if (value === '±') {
        // Toggle plus/minus sign
        let currentValue = parseFloat(output.value);
        output.value = currentValue * -1;
    } else {
        output.value += value;
    }
}

function cal(){
    try{
        let expression = output.value.replace(/√/g, 'Math.sqrt');
        previousOutput = eval(expression); 
        output.value = previousOutput;
    }
    catch(err){
        alert("Invalid expression");
    }
}

function clr(){
    output.value = ""; 
}

function del(){
    output.value = output.value.slice(0,-1);
}