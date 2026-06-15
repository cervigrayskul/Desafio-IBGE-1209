# Desafio Técnico – Automação RPA IBGE

# Objetivo

Desenvolver uma automação utilizando Selenium para navegar pelo portal SIDRA/IBGE, localizar a Tabela 1209 (População por grupos de idade), configurar os filtros e realizar o download dos dados da população com 60 anos ou mais por Unidade da Federação em formato CSV.

A navegação foi realizada integralmente pela interface do portal, sem utilização da URL direta da tabela ou da API do SIDRA.

# Tecnologias Utilizadas

* Python 3
* Selenium
* WebDriver Manager
* Google Chrome

# Pré-requisitos

Antes da execução, é necessário possuir instalado:

- Python 3.10 ou superior
- Google Chrome

Opcional:

- Git (caso deseje clonar o repositório)

Caso não possua Git instalado, o projeto também pode ser baixado através da opção "Download ZIP" disponível no GitHub.

# Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/cervigrayskul/Desafio-IBGE-1209.git
cd Desafio-IBGE-1209
```

Ou, caso prefira:

- Baixe o projeto em formato ZIP pelo GitHub.
- Descompacte o arquivo.
- Abra a pasta do projeto em sua IDE ou terminal.

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a automação através do terminal:

```bash
python desafio_ibge_1209.py
```

O arquivo é salvo dentro da pasta `dados`, criada automaticamente na mesma localização em que o script é executado.

Exemplo no Windows:

```text
C:\Users\usuario\Desafio-IBGE-1209\dados\populacao_60mais_1209.csv
```

O nome da pasta do usuário pode variar conforme o ambiente.


# Estratégia Adotada

A automação foi construída simulando a navegação de um usuário pelo portal SIDRA.

Fluxo executado:

1. Acessar a página inicial do SIDRA.

2. Navegar pelos menus iniciais:

   * Pesquisas
   * População
   * Censo Demográfico

3. Após selecionar "Censo Demográfico", o portal apresenta uma nova página com as pesquisas disponíveis. Nessa etapa são selecionadas as opções:

   * Demográfico 2022
   * População por Idade e Sexo
   * Tabela 1209

4. Ao selecionar a "Tabela 1209", o portal redireciona para a página de configuração da tabela, onde são definidos os filtros e parâmetros necessários para a extração dos dados.

5. Ativar o modo de somatório para permitir a soma dos grupos de idade desejados.

6. Selecionar os grupos de idade:

   * 60 a 69 anos
   * 70 anos ou mais

7. Ajustar o recorte territorial para Unidade da Federação.

8. Abrir o modal de download.

9. Definir o nome do arquivo.

10. Selecionar o formato CSV (BR).

11. Realizar o download.

12. Validar a conclusão do download.


# Tratamento de Erros e Confiabilidade

Para aumentar a estabilidade da automação foram implementadas as seguintes estratégias:

1. Esperas Explícitas

Utilização de "WebDriverWait" e "Expected Conditions" para sincronização dos elementos da página e redução de falhas causadas por carregamentos lentos.

2. Tentativas de Clique

A função de clique possui múltiplas tentativas para lidar com eventuais falhas temporárias de interação com elementos da interface.

3. Reexecução da Automação

Todo o fluxo da automação é executado dentro de uma estrutura de tentativa e recuperação, permitindo até 3 execuções completas em caso de erro inesperado.

4. Validação do Download

Após o clique para download, o script verifica a existência do arquivo esperado e aguarda a finalização do processo antes de concluir a execução.

5. Encerramento Seguro

O navegador é encerrado através de bloco "finally", garantindo o fechamento do processo mesmo em caso de exceção.


# Principais Desafios Encontrados

1. Navegação Sem URL Direta

Um dos requisitos do desafio era acessar a tabela exclusivamente através da interface do portal. Por esse motivo, toda a navegação foi realizada utilizando menus e elementos da aplicação até chegar à tela de configuração da Tabela 1209.

2. Download Automatizado

Foi necessário configurar o Chrome para permitir downloads automáticos sem exibir janelas de confirmação do navegador, garantindo que o arquivo fosse salvo diretamente na pasta especificada pelo desafio.

3. Interação com o Modal de Download

Durante o desenvolvimento foi identificado que alguns elementos do modal de download não apresentavam comportamento consistente quando acessados diretamente através dos seletores tradicionais do Selenium.

Em especial, a seleção do formato do arquivo apresentou dificuldades de interação mesmo com o elemento sendo localizado corretamente no DOM.

Para contornar esse comportamento e manter a automação próxima da experiência real do usuário, foi adotada uma navegação baseada em foco utilizando a tecla TAB, permitindo alcançar os campos desejados e realizar o preenchimento através do elemento ativo da interface.

Essa abordagem tornou o fluxo mais estável para o comportamento específico do modal de download do SIDRA.

4. Estabilidade da Interface

Durante os testes foram observadas variações ocasionais no carregamento de elementos da página. Para minimizar esse impacto foram implementadas esperas explícitas, tentativas adicionais de clique e reexecução completa da automação em caso de falha.


# Resultado

Ao final da execução é gerado automaticamente o arquivo:

dados/populacao_60mais_1209.csv

contendo os dados da população com 60 anos ou mais por Unidade da Federação, obtidos a partir da Tabela 1209 do SIDRA/IBGE.
