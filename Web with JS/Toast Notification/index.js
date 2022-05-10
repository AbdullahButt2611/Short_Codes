const btn = document.querySelector(".btn");
const cancelBtn = document.querySelector(".cancel_btn");
const toastBox = document.querySelector(".toast_box");
const seconds = document.querySelector(".seconds");


let time = 5;
let interval;
let timeout;

btn.addEventListener("click",()=>{
    btn.setAttribute("disabled","");
    time = 5;
    toastBox.style.transform = ("translate(0%)");
    interval = setInterval(()=>{
        time -=1;
        seconds.innerHTML  = '0${time}s';
    },1000);
    
    interval = setInterval(()=>{
        toastBox.style.transform = ("translate(110%)");
        time =5;
        seconds.innerHTML  = '0${time}s';
        clearInterval(interval);
        btn.removeAttribute("disbaled","");
    },6000);
});



cancelBtn.addEventListener("click",()=>{
    btn.removeAttribute("disbaled","");
    toastBox.style.transform = ("translate(110%)");
    time = 5;
    seconds.innerHTML  = '0${time}s';
    clearInterval(interval);
    clearTimeout(timeout);
});

