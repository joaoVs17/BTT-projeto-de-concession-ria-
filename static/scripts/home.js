let btn_below = document.getElementsByClassName('btn_below');
let slide1 = document.getElementById('slide1');
let slideA = document.getElementById('slideA');

let valor = 0;
let slide = 0;


function bemvindo() {
    document.getElementById('modal').style.display = 'block';
}

function fechar() {
    document.getElementById('modal').setAttribute('style', 'display: none !important');
}

function verify(){
    if (slide>0) {
        console.log('batata')
        document.getElementById('up').disabled = false;
        document.getElementById('up').style.opacity = '0.5';

    } else if (slide<1) {
        document.getElementById('up').disabled = true;
        document.getElementById('up').style.opacity = '0';
    }
    if (slide>3) {
        document.getElementById('down').disabled = true;
        document.getElementById('down').style.opacity = '0';
    } else if (slide<4) {
        document.getElementById('down').disabled = false;
        document.getElementById('down').style.opacity = '0.5'
    }
    
}

verify();

bemvindo();




function goDown() {
    if (slide<4) {
        slide+=1;
        valor = valor+100;
        document.getElementById('pp').setAttribute('style', 'margin-top: -'+valor+'vh !important');
        verify();
    }  
}

function goUp() {
    if (slide>0) {
        slide -= 1;
        valor = valor-100;
        document.getElementById('pp').setAttribute('style', 'margin-top: -'+valor+'vh !important');
        verify();
    }
}

//Para o modal

