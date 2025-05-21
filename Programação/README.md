# Restaurante Massa™

O objetivo desse trabalho foi fazer uma aplicação em [Shiny for Python](https://shiny.posit.co/py/) que utilizasse, de alguma forma, o framework Shiny, condicionais e loops.

No nosso caso, o projeto é um gerenciador de restaurantes, possivelmente com controle de reservas para mesas, pedidos e cardápio.

## Instruções para rodar

O projeto foi feito com Python 3.13.2, mas deve rodar com qualquer versão recente do Python.

- Clone o repositório.
- Abra o terminal (do próprio sistema ou do VSCode) na pasta do projeto.
- Crie um ambiente virtual do Python usando `python -m venv .venv` (ou `python3.13 -m venv .venv`, se a versão default do sistema não for a certa).
- Ative o ambiente usando o comando `./.venv/Scripts/Activate.ps1` (no Windows).
- Instale os pacotes necessários com o comando `pip install -r requirements.txt`.
- Rode o projeto com o comando `shiny run app.py --reload`. O `--reload` faz com que o aplicativo atualize automaticamente quando você faz alterações no código.

## Instruções para o servidor

- **Criando a instância do AWS:**
    - Após acessar o AWS pelo AWS Learner Lab, você vai procurar o serviço "EC2".
    - Clicando nele, você vai ver um monte de opções. Em algum lugar deve ter um botão escrito "Launch Instance". Clique nele.
    - Agora, você verá um o painel de criação. Comece por dar um nome a ele.
    - Escolha um sistema operacional para ele. O recomendado é o Debian.
    - Você poderia configurar a máquina nas opções seguintes, mas nós só temos acesso a uma, então não precisa.
    - Desça até onde está escrito "Key pair (logon)" e clique em "Create new key pair".
        - Adicione um nome ao seu key pair e crie ele. O AWS vai imediatamente baixar a chave no seu computador.
        - Essa chave é o que permite que você acesse o servidor pelo terminal ou pelo VSCode.
    - Finalmente, clique em "Launch Instance" para terminar a criação.
    - Agora, você pode acessar os detalhes do servidor voltando para o painel do serviço EC2, clicando em "Instances (running)" e selecionando a instância que você criou.
- **Acesso ao servidor pelo terminal:**
    - O seu computador precisará de algum cliente SSH para conseguir fazer isso.
        - Ele já deve vir instalado, mas verifique com o comando `ssh`. Se não estiver, baixe o OpenSSH ou equivalente.
    - Para acessar o terminal do servidor, rodar o comando `ssh -i "CAMINHO_DA_CHAVE" admin@ENDERECO_DO_SERVIDOR`.
        - Aqui, o `CAMINHO_DA_CHAVE` seria o caminho do arquivo `.pem` do servidor, que permite acesso ao terminal.
        - O `ENDERECO_DO_SERVIDOR` é o DNS IPv4 público ("Public IPv4 DNS", no painel de controle da instância do AWS).
        - Se ele perguntar sobre a autenticidade do host, você pode digitar `yes` para continuar conectando ao servidor.
    - Para enviar arquivos ao servidor, rodar o comando (em um terminal que não seja do servidor) `scp -r -i "CAMINHO_DA_CHAVE" "CAMINHO_DA_PASTA_OU_ARQUIVO" admin@ENDERECO_DO_SERVIDOR:DESTINO`;
        - Alguns dos argumentos são os mesmos do comando anterior.
        - `CAMINHO_DA_PASTA_OU_ARQUIVO` é o caminho do que você quer enviar.
        - `DESTINO` é a pasta para qual você quer copiar os arquivos, dentro do sistema do servidor.
- **Configuração do servidor:**
    - Para rodar o servidor, é necessário abrir uma porta no AWS para permitir o tráfego.
        - Para fazer isso, comece entrando no painel de controle da instância.
        - Vá para a abra "Security" ou segurança.
        - Ache o grupo de segurança principal na parte "Security groups" e clique nele.
        - No painel "Inbound rules", clique no botão "Edit inbound rules".
        - Lá, uma nova regra com "Add rule" e escolha o tipo "Custom TCP".
        - Escolha o port que você quer usar e o escreva em "Port range".
        - Onde está escrito "Source type", escolha "Anywhere-IPv4".
        - Opcionalmente, adicione uma descrição.
        - Clique em "Save rules" para salvar.
    - Após copiar os aquivos do projeto, será necessário criar um novo ambiente virtual do Python.
        - Na verdade, isso não é estritamente necessário, mas é prática padrão da indústria.
        - Enfim, navegue até pasta do seu projeto.
        - Atualize o gerenciador de pacotes do Debian com `sudo apt update`. Isso garante que você poderá instalar pacotes.
        - Digite o comando `python3 -m venv NOME_DO_VENV`. Geralmente, eu uso o `NOME_DO_VENV` como `.venv`.
            - É possível que a ferramenta para criar o venv não esteja instalada. Nesse caso, ele vai te dar um comando para instalar.
        - Ative o ambiente com `source ./NOME_DO_VENV/bin/activate`.
        - Instale as dependências necessárias. Idealmente, você terá um arquivo `requirements.txt`. Se esse for o caso, digite `pip install -r requirements.txt`. Se não, instale as dependências manualmente com `pip install x`.
        - Tendo o Shiny instalado, você pode rodar o comando `shiny run app.py --host 0.0.0.0 --port PORT_QUE_VOCE_ESCOLHEU` para rodar o servidor.
        - Finalmente, você pode acessar o seu servidor pelo link `IP_DO_SERVIDOR:PORT_QUE_VOCE_ESCOLHEU`!
            - Aqui, o `IP_DO_SERVIDOR` seria o IP encontrado na parte "Public IPv4 address" do painel de controle da sua instância.