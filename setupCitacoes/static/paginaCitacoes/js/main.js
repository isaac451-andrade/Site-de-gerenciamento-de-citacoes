const campoQuote = document.getElementById('quote');
const campoAutor = document.getElementById('campo-autor');
const button_save = document.getElementById('button-save');


function showOtherButtons() {
    campoAutor.style.visibility = 'visible';
    button_save.style.visibility = 'visible';
}

campoQuote.addEventListener('focusin', () => showOtherButtons());

button_save.addEventListener('click', () => {
    campoAutor.style.visibility = 'hidden';
    button_save.style.visibility = 'hidden';
})