const modal = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementsByClassName('modal-body')[0];
const updateQuiz = document.getElementById('update-button');
const deleteQuiz = document.getElementById('delete-button');
const detailsQuiz = document.getElementById('details-button');
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

    detailsQuiz.addEventListener('click', () => {
        
        window.location.href = link  + pk + '/details/'
    
    })
}))








// for quiz_question
const modalQuestion = [...document.getElementsByClassName('modal-question-button')];
const modalQuestionBody = document.getElementsByClassName('modal-question-body')[0];
const answrButton = document.getElementById('answer-button');
const cancelButton = document.getElementById('cansel-button');

const answerLink = window.location.href;


console.log('modalQuestionBody',modalQuestionBody)
console.log('modalQuestion',modalQuestion)


modalQuestion.forEach(modal => modal.addEventListener('click', () => {
    // console.log(modal);
    const pk = modal.getAttribute('data-pk');
    const questionType = modal.getAttribute('data-question-type');
    const Text = modal.getAttribute('data-text')   
    const answer = modal.getAttribute('data-answers')
    
    console.log('answer',answer)
    console.log('Text',Text)
    console.log('questionType',questionType)

    modalQuestionBody.innerHTML = `

        <div class="h5 mb-3" >  "<b>${Text}</b>" ?</div>
        <div class="text-muted">
            <ul>
                <li>type of questions :  <b>${questionType}</b></li>
                <li>number of answers :  <b>${answer}</b></li>
            </ul>
        </div>
        
    `

    answrButton.addEventListener('click', () => {
        
        window.location.href = answerLink  + pk + '/answers/'
    
    })


    
}))








