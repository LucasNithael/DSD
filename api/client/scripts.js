url = 'http://127.0.0.1:8000/aluno'

fetch(url)
.then( response => {
    return response.json()
}).then( aluno => {
    console.log(aluno)
} )