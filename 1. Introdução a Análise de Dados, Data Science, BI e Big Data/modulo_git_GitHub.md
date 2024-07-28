## Bootcamp Data Analitycs - Semana 04: Git e GitHub

Na semana 4 do Bootcamp Data Analitycs aprendemos o funcionamento da plataforma do GitHub e funcionalidades do Git. Essas ferramentas são extremamente úteis para um analista de dados, pois permite a colaboração e compartilhamento de códigos, arquivos e projetos. Além disso, é uma ferramenta segura e que mantém o controle de todas as versões dos arquivos e diretórios presentes em um repositório, deixando registrada todas suas modificações, data e usuário responsável por tal modificação.

### Roteiro para contribuir com repositórios de outros usuários do GitHub

Para contribuir com repositórios outros usuários do GitHub, deve-se seguir os seguintes passos:
- *No site do GitHub*: escolher o repositório que quer contribuir e clicar em "fork" no canto superior direito da página.
- Depois de fazer o fork do repositório original, esse repositório vai aparecer na sua página do GitHub.
- **Clonar repositório**: O próximo passo será clonar esse repositório que você fez o fork na sua máquina local.
    - *Copiar chave HTTPS*: no repositório clonado na sua conta do GitHub, clicar em "Code" e copiar a chave HTTPS do repositório.
    - *Criar pasta para repositório*: Na sua máquina local abra o terminal de comando e crie uma pasta para comportar o repositório clonado pelo comando --> *mkdir nome_nova_pasta*
    - *Verificar se configuração do git esta correta*: antes de clonar o repositório, é interessante você conferir se seu git esta configurado corretamente por meio do seguinte comando no terminal --> *git config --list*
    - *Clonar repositório*: entre na pasta criada (*cd nome_nova_pasta*) e clone o repositório com o comando --> *git clone chave_https_copiada*
- Após clonar o reposítório, entre na pasta em que ele se encontra (*cd nome_do_repositóro*) e depois digite *code .* no terminal para abrir o diretório no VSCode.
- No VSCode: clicar em "Terminal" e depois "New Terminal" para abrir uma interface do terminal no VSCode.
- *Conferir conexão com repositório remoto*: Nesse terminal do VSCode digite *git remote -v* para conferir a conexão do repositório local com o repositório remoto.
- **Criar branch nesse repositório**: Para fazer as modificações ao repositório, temos criar uma nova branch dele. Fazemos isso digitando no terminal -->  *git checkout -b nome_nova_branch*
- *Fazer modificações*: estando nessa nova branch podemos fazer as modificações que desejar.
- **Salvar modificações**: Após fazer as modificações, voltamos para o terminal de comando e digitamos a seguinte série de comandos:
    - *git add .*
    - *git commit - m "comentário"*
- **Subir as modificações feitas no repositório local para o repositório remoto**: fazemos isso usando o seguinte comando no terminal --> *git push --set-upstream origin nome_branch_que_fez_modificações*
- **Fazer Pull Request**: Depois de você execultar esse comando, o Git irá sugerir que você faça uma Pull Request e fornecerá um link para isso. Você deve clicar no link ou copiar o link e colar ele no navegador. Na pagina que aparecer, você deverá seguir os seguintes passos:
    - Alterar título e descrição da Pull Request
    - Delimitar configurações referentes à revewers, assigment e label (se possível)
    - Conferir se a Pull Request é da sua branch no repositório "forkado" para a branch principal no repositório original (associado ao username do criador daquele repositório)
    - Clicar no botão verde para mandar pull request
- Pronto! Sua contribuição esta feita. Depois disso cabe ao dono do repositório aceitar ou propor modificações à sua Pull Request.

