
document.querySelector('#sign-up').addEventListener("click", () => {
    document.querySelector('.sign-in').style.marginLeft = '-34rem';
    document.querySelector('#sign-up').style.marginTop = '-5rem';
    document.querySelector('.images > image').style.marginLeft = '0rem';
});

document.querySelector('#sign-in').addEventListener("click", () =>{
    document.querySelector('.sign-in').style.marginLeft = '0rem';
    document.querySelector('#sign-in').style.marginTop = '1rem';
    document.querySelector('.images > image').style.marginLeft = '-18rem';
});

