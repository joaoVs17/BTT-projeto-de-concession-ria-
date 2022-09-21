let a = document.getElementById('a');
let b = document.getElementById('b');
let c = document.getElementById('c');

let timer = 30;


let currentMargin = window.getComputedStyle(document.getElementById('slider')).marginLeft;
    currentMargin = currentMargin.replace('px','');
    currentMargin = parseInt(currentMargin);





setInterval(function(){   
    console.log(currentMargin)
    if (currentMargin >= -100) {
        currentMargin-=100;
        document.getElementById('slider').setAttribute('style', 'margin-left:'+currentMargin+'vw !important');
    } else {
        currentMargin = 0;
        document.getElementById('slider').setAttribute('style', 'margin-left:'+currentMargin+'vw !important');
    }
    if (currentMargin == 0) {
        a.checked = true;
    } else if (currentMargin == -100) {
        b.checked = true;
    } else if (currentMargin ==-200) {
        c.checked = true;
    }
}, 4000)


function aa(){
    document.getElementById('slider').setAttribute('style', 'margin-left: 0 !important');
    currentMargin = 0;
}

function bb() {
    document.getElementById('slider').setAttribute('style', 'margin-left: -100vw !important');
    currentMargin = -100
}

function cc() {
    document.getElementById('slider').setAttribute('style', 'margin-left: -200vw !important');
    currentMargin = -200
}

function bemvindo() {
    document.getElementById('modal').style.display = 'block';
}

function fechar() {
    document.getElementById('modal').setAttribute('style', 'display: none !important');
}

bemvindo();