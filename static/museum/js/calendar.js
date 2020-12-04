events = document.querySelectorAll('div.jsEvent > div > ul');

for(let i=0; i<events.length; i++){

    if(/[\w]/.test(events[i].innerHTML) === true){
        el = document.querySelectorAll('button.buttonHoverCal')[i].classList.add('btnEvent');
    }
}


