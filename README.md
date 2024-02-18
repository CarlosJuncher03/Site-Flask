# Site de Visualização de Tickets - Flask

Este é um projeto de site desenvolvido em Flask para visualização de tickets abertos em um sistema de gerenciamento de atendimentos. O objetivo principal é permitir que os clientes da empresa tenham acesso aos tickets abertos em um banco de dados SQL Server, fornecendo transparência e visibilidade sobre o progresso de suas solicitações de suporte.

## Funcionalidades Principais

- **Visualização de Tickets:** Os clientes podem visualizar os tickets abertos, incluindo informações relevantes como status, data de abertura e descrição do problema.
- **Filtragem de Tickets:** Os tickets podem ser filtrados com base em diferentes critérios, como status, data de abertura ou tipo de problema.
- **Acesso Restrito:** A visualização dos tickets é restrita aos clientes autenticados, garantindo a confidencialidade das informações.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- **main.py:** Arquivo principal do aplicativo Flask.
- **templates:** Pasta contendo os modelos HTML usados para renderizar as páginas.
- **static:** Pasta contendo arquivos estáticos, como CSS e imagens.
- **conex_sql_sever.py:** Arquivo de configuração do banco de dados SQL Server.
- - **main.py:** nesse arquivo tem a query que valida o ususario, ajustar a mesma para validar o proprio usuario.

## Como Executar

Para executar o aplicativo localmente, siga estas etapas:

1. Certifique-se de ter o Python instalado em seu sistema. Recomenda-se a versão 3.x.
2. Clone este repositório em seu ambiente local.
3. Navegue até o diretório do projeto.
4. Instale as dependências usando o comando `pip install -r requirements.txt`.
5. Configure as informações de conexão com o banco de dados SQL Server no arquivo `conex_sql_sever.py`.
6. Execute o aplicativo com o comando `python main.py`.
7. Abra um navegador da web e acesse `http://localhost:5000` para visualizar os tickets.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.

## Video do site 

https://github.com/CarlosJuncher03/site_flask/assets/145303814/af98c7cd-392d-4b36-a56f-e3eb79dbddd1




## Autor

Este projeto foi desenvolvido por [Carlos Juncher](https://github.com/CarlosJuncher03) para uso interno da empresa onde trabalha.
