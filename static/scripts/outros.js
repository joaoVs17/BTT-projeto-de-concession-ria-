let btn_below = document.getElementsByClassName('btn_below');
let slide1 = document.getElementById('slide1');
let slideA = document.getElementById('slideA');

let valor = 0;
let slide = 0;


let swiper = document.getElementById('swiper');

function verify(){
    if (slide>0) {
        console.log('batata')
        document.getElementById('up').disabled = false;
        document.getElementById('up').style.opacity = '0.5';

    } else if (slide<1) {
        document.getElementById('up').disabled = true;
        document.getElementById('up').style.opacity = '0';
    }
    if (slide>0) {
        document.getElementById('down').disabled = true;
        document.getElementById('down').style.opacity = '0';
    } else if (slide<1) {
        document.getElementById('down').disabled = false;
        document.getElementById('down').style.opacity = '0.5'
    }
    
}

verify();




function goDown() {
    if (slide<2) {
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

//Para o swiper

let swip = 0;
let pos = 0;

//Função para ir para a esquerda 
function left() {
    if (pos>-2) {
    pos -= 1;
    swip += 41.5;
    swiper.setAttribute('style', 'margin-left:'+swip+'vw !important');
    } 
}


//Função para ir para a direita
function right() {
    if (pos<2) {
    pos += 1;
    swip -= 41.5;
    swiper.setAttribute('style', 'margin-left:'+swip+'vw !important');
    }
}



