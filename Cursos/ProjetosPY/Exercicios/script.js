const arquivos = [
    "ex001 Olá Mundo.py",
    "ex002 Boas Vindas.py",
    "ex003 Somando dois numeros.py",
    "ex004 Dissecando uma variável.py",
    "ex005 Antecessor e Sucessor.py",
    "ex006 Dobro, Triplo, Raiz.py",
    "ex007 Média Aritimética.py",
    "ex008 Conversor de Medidas.py",
    "ex009 Tabuada.py",
    "ex010 Conversor de Moedas.py",
    "ex011 Pintando Parede.py",
    "ex012 Calculando Descontos.py",
    "ex013 Reajuste salarial.py",
    "ex014 Conversor de Temperatura.py",
    "ex015 Aluguel de carros.py",
    "ex016 Numero real inteiro.py",
    "ex017 Hipotenusa.py",
    "ex018 Seno-Cosseno-Tangente.py",
    "ex019 Sorteio de alunos.py",
    "ex020 Sorteio de ordem de alunos.py",
    "ex021 Tocar mp3.py",
    "ex022 Fatiamento e contar.py",
    "ex023 Milhar Centena Dezena Unidade.py",
    "ex024 Começa com Santo.py",
    "ex025 Tem silva no nome.py",
    "ex026 Quantas vezes aparece a letra A.py",
    "ex027 Primeiro e ultimo nome.py",
    "ex028 Adivinhando o numero.py",
    "ex029 Multa se acima de 80Km.py",
    "ex030 Par ou impar.py",
    "ex031 Cobrando passagem.py",
    "ex032 Ano é bissexto.py",
    "ex033 Qual numero é maior.py",
    "ex034 Aumento se for maior.py",
    "ex035 Formam um triângulo.py",
    "ex036 Emprestimo bancário.py",
    "ex037 Binário Decimal Octognal.py",
    "ex038 Serviço militar.py",
    "ex039 Média aluno aprovado.py",
    "ex040 Categoria por idade.py",
    "ex041 Equilátero Isósceles Escaleno.py",
    "ex042 Valor maior menor e igual.py",
    "ex043 IMC ideal.py",
    "ex044 Pagamento.py",
    "ex045 Jokenpô.py",
    "ex046 Contagem regressiva com espera.py",
    "ex047 Numeros pares entre 1 e 50.py",
    "ex048 Soma dos numeros impares divisiveis por 3.py",
    "ex049 Tabuada com for.py",
    "ex050 Some apenas se for impar.py",
    "ex051 Progressão Aritimética.py",
    "ex052 O numero é primo.py",
    "ex053 É um palíndromo.py",
    "ex054 Quantas pessoas são de maior.py",
    "ex055 Maior Menor da Sequência.py",
    "ex056 Dissecando informações.py",
    "ex057 Validação de dados.py",
    "ex058 Jogo da adivinhação 2.0.py",
    "ex059 Menu de opções.py",
    "ex060 Cálculo fatorial.py",
    "ex061 Progreção Aritimética 2.0.py",
    "ex062 Progreção Aritimética 3.0.py",
    "ex063 Fibonacci 1.0.py",
    "ex064 Tratando vários valores 1.0.py",
    "ex065 Maior e Menor valores.py",
    "ex066 Interrompendo repetições.py",
    "ex067 Tabuada 3.0.py",
    "ex068 Jogo Par ou Impar.py",
    "ex069 Análise de dados do grupo.py",
    "ex070 Estatísticas em produtos.py",
    "ex071 Simulador de caixa eletrônico.py"
];

const container = document.getElementById("exercicios-container");

// Função para executar o código
function executar(botao) {
    const exContainer = botao.parentElement;
    const codigo = exContainer.querySelector('.codigo').value;
    const resultado = exContainer.querySelector('.resultado');

    function outf(text) {
        resultado.textContent += text + '\n';
    }

    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "Arquivo não encontrado: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }

    // Configura Skulpt com input via prompt
    Sk.configure({
        output: outf,
        read: builtinRead,
        inputfun: function(promptText) {
            return prompt(promptText); // exibe janela para o usuário digitar
        },
        inputfunTakesPrompt: true
    });

    resultado.textContent = '';
    Sk.misceval.asyncToPromise(function() {
        return Sk.importMainWithBody("<stdin>", false, codigo, true);
    }).catch(function(err) {
        resultado.textContent += err.toString();
    });
}

// Função para ajustar altura do textarea
function ajustarAltura(textarea) {
    textarea.style.height = 'auto'; // resetar altura
    const alturaMin = 50;   // altura mínima
    const alturaMax = 400;  // altura máxima
    const novaAltura = Math.min(Math.max(textarea.scrollHeight, alturaMin), alturaMax);
    textarea.style.height = novaAltura + 'px';
}

// Carregar exercícios na ordem correta
async function carregarExercicios() {
    for (const nome of arquivos) {
        try {
            const res = await fetch(`exerciciospy/${encodeURIComponent(nome)}`);
            if (!res.ok) throw new Error(`Erro ao carregar ${nome}: ${res.status}`);
            const codigo = await res.text();

            const exDiv = document.createElement('div');
            exDiv.classList.add('exercicio');

            exDiv.innerHTML = `
                <h2>${nome}</h2>
                <textarea class="codigo">${codigo}</textarea><br>
                <button onclick="executar(this)">Executar</button>
                <pre class="resultado"></pre>
            `;
            container.appendChild(exDiv);

            const textarea = exDiv.querySelector('.codigo');
            ajustarAltura(textarea);
            textarea.addEventListener('input', () => ajustarAltura(textarea));

        } catch (err) {
            console.error(err);
        }
    }
}

// Inicia o carregamento
carregarExercicios();
