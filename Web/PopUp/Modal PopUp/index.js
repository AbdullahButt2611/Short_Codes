const openBtn = document.querySelector("button");
const closeBtn = document.querySelector("#close");
const modal = document.querySelector(".modal");
const form = document.querySelector("form");




// -----------------            Program Logic        ------------------------------
openBtn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);
form.addEventListener("submit", submitForm);







// -----------------            Function Definitions        ------------------------------

function openModal(){
    modal.style.display = "grid";
}

function closeModal(){
    modal.classList.add('close-modal-animation');
    setTimeout(()=>{
        modal.style.display = "none";
        window.location.reload();
    }, 1000);
}

modal.addEventListener('click', function(e){
    if(e.target.classList.contains("modal")){
        closeModal();
    }
});

function submitForm(){
    const card = document.querySelector(".card");
    card.innerHTML = "<h1>Thank you for following my account</h1>";
    setTimeout(() => {
        closeModal();
    }, 3000);
}
