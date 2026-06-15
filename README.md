# Desafio Técnico – Automação RPA IBGE

# Objetivo

Desenvolver uma automação utilizando Selenium para navegar pelo portal SIDRA/IBGE, localizar a Tabela 1209 (População por grupos de idade), configurar os filtros e realizar o download dos dados da população com 60 anos ou mais por Unidade da Federação em formato CSV.

A navegação foi realizada integralmente pela interface do portal, sem utilização da URL direta da tabela ou da API do SIDRA.


# Tecnologias Utilizadas

* Python 3
* Selenium
* WebDriver Manager
* Google Chrome


# Instalação e Execução

1. Clone o repositório:

git clone <url-do-repositorio>
cd <repositorio>

2. Instale as dependências:

pip install -r requirements.txt

3. Execute a automação através do terminal:

python desafio_ibge_1209.py

Ao final da execução, o arquivo será salvo automaticamente em:

dados/populacao_60mais_1209.csv

A pasta "dados" é criada automaticamente caso não exista.


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

Ao final da execução é gerado o arquivo:

dados/populacao_60mais_1209.csv

contendo os dados da população com 60 anos ou mais por Unidade da Federação, obtidos a partir da Tabela 1209 do SIDRA/IBGE.
