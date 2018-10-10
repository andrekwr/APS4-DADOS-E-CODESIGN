document.addEventListener('DOMContentLoaded', function() {
    /*
        Inicializa uma medição de tempo, que será gravada no
        banco de dados cujo endereço é passado como parâmetro.
        Altere o endereço abaixo para seu próprio banco de dados.
    */
    let ab = start('https://teste-ab-4d23b.firebaseio.com/')

    /*
        Seleciona o elemento que, quando clicado, finaliza a
        medição de tempo e envia o resultado para o banco.
        Altere o seletor abaixo para o do elemento desejado.
    */


    let classe = document.querySelectorAll('.clicar');

    for (let element of classe) {


        element.addEventListener('click', function() {
        ab.finish()
        })

        let as = document.querySelectorAll('a')

        for(let a of as) {
            a.addEventListener('click', function(event) {
                event.preventDefault()
                setTimeout(function() {
                    window.location.assign(a.href)
                }, 5000)
            })
        }

        }



    /*
        A princípio, o restante do código não precisa mudar.
    */

    
})
