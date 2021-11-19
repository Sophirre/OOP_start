let number = document.getElementById('displayNum');

async function show(value){
    let a = await eel.show(value)();
    console.log(a)
}


function showNumber(value){
    let tempNum = value;
    number.innerHTML = value;

//    number.innerHTML = tempNum + value;
}

function clear(){
    number.innerHTML = 0;
    show('Clear');
    console.log('success')
}


