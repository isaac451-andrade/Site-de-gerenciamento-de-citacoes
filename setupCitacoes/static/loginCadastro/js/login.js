const inputs = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.span-required');
const formCadastro = document.querySelector('.form-cadastro');
const formLogin = document.querySelector('.form-login');

function isFormValidCadastro(){
    return validateName() && validateSenhaCadastro() && validateConfirmaSenha();
}
function isFormValidLogin(){
    return validateName() && validateSenhaLogin();
}



formCadastro.addEventListener('submit', (event) =>{
    event.preventDefault();
    if(isFormValidCadastro()){
        formCadastro.submit();
    }
})

formLogin.addEventListener('submit', (event) => {
    event.preventDefault();
    
    if(isFormValidLogin()){
        formLogin.submit();
    }
})

function setError(indice) {
    inputs[indice].classList.add('error');
    spans[indice].style.display = 'block';
}

function removeError(indice) {
    inputs[indice].classList.remove('error');
    spans[indice].style.display = 'none';
}

function validateName() {
    if(inputs[0].value.length < 3){
        setError(0);

        return false;
    }else {
        removeError(0);

        return true;
    }
}

function validateSenhaCadastro() {
    if(inputs[1].value.length < 8) {
        setError(1);
        return false;
    }else {
        removeError(1);
        validateConfirmaSenha();
        return true;
    }
}

function validateSenhaLogin() {
    if(inputs[1].value.length >=8) {
        removeError(1);
        return true;
    }else {
        setError(1);
        return false;
    }
}

function validateConfirmaSenha() {
    console.log(inputs[2].value)
    if(inputs[2].value != inputs[1].value || inputs[2].value.length <8) {
        setError(2);
        console.log("Entrou")
        return false;
    } else {
        console.log("NÃO entrou")
        removeError(2);
        return true;
    }
}