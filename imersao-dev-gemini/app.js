function pesquisar() {
    // Obtém a seção HTML onde os resultados serão exibidos
    let section = document.getElementById("resultados-pesquisa");

    let campoPesquisa = document.getElementById("campo-pesquisa").value;

    // Inicializa uma string vazia para armazenar os resultados HTML
    let resultados = '';

    if (campoPesquisa == ''){
        section.innerHTML = "<p>Nada foi encontrado</p>"
        return
    }

    campoPesquisa = campoPesquisa.toLowerCase()

    let titulo = '';
    let descricao = '';
    let tags = '';

    // Itera sobre cada item de dados (assumindo que 'dados' é um array de objetos)
    for (let dado of dados) {
        titulo = dado.titulo.toLocaleLowerCase();
        descricao = dado.descricao.toLocaleLowerCase();
        tags = dado.tags.toLocaleLowerCase();

        if (titulo.includes(campoPesquisa) || descricao.includes(campoPesquisa) || tags.includes(campoPesquisa)){
            // Concatena o HTML de cada resultado à string 'resultados'
            resultados += `
                <div class="item-resultado"> 
                    <h2><a href="#" target="_blank">${dado.titulo}</a></h2>
                    <p class="descricao-meta">${dado.descricao}</p>
                    <a href=${dado.link} target="_blank">Mais informações</a>
                </div>
            `;
        }
    }

    if (!resultados) {
        resultados = "<p>Nada foi encontrado<p>";
    }
    // Atribui o HTML completo da lista de resultados à seção
    section.innerHTML = resultados;
}