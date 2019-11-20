# rsi-psd-project

# Configuração de maquina:
```
1 - git clone https://github.com/andrelarruda/rsi-psd-project.git
2 - git config --global user.email "your email on git"
3 - git config --global user.name "your name"
```

# Diretrizes push:
* Os códigos deverão ser baixados da branch "develop", alterados ou criados novos códigos. Ao publicar esses códigos no repositorio deverá ser criado um branch novo de acordo com o arquivo (1 branch por arquivo) e em seguida solicitar um pull request para aprovação na branch develop
```
1 - git branch "new branch"
2 - git checkout "new branch"
3 - git add "your files"
4 - git commit -m "commit title"
5 - git push origin "new branch"
6 - git checkout develop
7 - realizar o pull request no github.com 
```

# Sobre o Projeto:
* Este projeto tem por finalidade por em prática conceitos de sistemas distribuidos, ou seja, alguns componentes foram projetados para rodar em maquinas distintas em uma mesma rede.

OBS: A plataforma do thingsboard precisará ser configurada da forma que desejar desde que, os tokens sejam alterados em código

#Iniciando o APP + Services:

- APP
1-git clone https://github.com/andrelarruda/rsi-psd-project.git
2-git checkout app
3-cd app
4-npm install
5-npm start
6- baixar no celular o aplicativo EXPO
7-Ao iniciar o navegador irá abrir uma pagina contendo um QR CODE
8-Use o aplicativo EXPO instalado em seu celular para ler o QR code

-Service 5nearest
1- Volte para a raiz do projeto
2-cd api-5-nearest
3-npm install
4-npm run dev

-Service idw
1- Volte para a raiz do projeto
2-cd api-idw
3-npm install
4-npm run dev




# Referências:
- [Guia prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html)
- [Documentação](https://git-scm.com/doc)
- [Kafka](https://kafka.apache.org/)
- [Spark](https://spark.apache.org/)
- [Docker](https://docs.docker.com/)
