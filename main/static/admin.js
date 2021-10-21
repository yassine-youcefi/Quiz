const modal = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementsByClassName('modal-body')[0];
const updateQuiz = document.getElementById('update-button');
const deleteQuiz = document.getElementById('delete-button');
const link = window.location.href;

modal.forEach(modal => modal.addEventListener('click', () => {
    // console.log(modal);
    const pk = modal.getAttribute('data-pk');
    const name = modal.getAttribute('data-quize');
    const numberQuestions = modal.getAttribute('data-questions')   
    const time = modal.getAttribute('data-time')   
    const pass = modal.getAttribute('data-pass')   

    modalBody.innerHTML = `

        <div class="h5 mb-3" >"<b>${name}</b>"</div>
        <div class="text-muted">
            <ul>
                <li>number of questions :  <b>${numberQuestions}</b></li>
                <li>score required to passs :  <b>${pass}</b></li>
                <li>time :  <b>${time} min</b></li>
            </ul>
        </div>
        
    `
    updateQuiz.addEventListener('click', () => {
        
        window.location.href = link  + pk + '/update/'
    
    })

    deleteQuiz.addEventListener('click', () => {
        
        window.location.href = link  + pk + '/delete/'
    
    })
}))











