let displayNum = document.getElementById('displayNum');

async function insert(value) {
  var num = displayNum.innerText;
  // add 1 to string
  let user_string = await eel.add_string(num,value)();
  displayNum.innerText = user_string;
}

document.getElementById("clear-btn").onclick = function() {clear()};
function clear(){
    displayNum.innerHTML = 0;
    console.log('cleared');
}


async function operator_checker(){
    let number = displayNum.innerText;
    console.log(number);
    let operator = await eel.operation_checker(number)();
    return operator
}

async function numbers_get(){
    let string = displayNum.innerText;
    let numbers = await eel.numbers_get(string)();
    console.log(numbers)
    return numbers
    }

document.getElementById("equal").onclick = function() {operation()};
async function operation(){
    let event = await operator_checker();
    let numbers = await numbers_get();
    let result = await eel.object_init('common',event, numbers)();
    console.log(result);
    displayNum.innerText = result;


}
