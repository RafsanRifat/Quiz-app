const modalBtns = [...document.getElementsByClassName('modal-button')]
console.log(modalBtns)
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    console.log(modalBtn)
}))