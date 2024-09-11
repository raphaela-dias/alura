alert('Boas-vindas ao jogo do número secreto');

let numeroSecreto = 5;
console.log(numeroSecreto)
let chute = prompt('Escolha um número entre 1 e 30');

//Se o chute dor igual ao número secreto
if (chute == numeroSecreto) {
    alert("Isso aí! Você descobriu o número secreto!");
} else {
    alert("Você errou! :(");
}