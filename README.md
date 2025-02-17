# GameCursor


![GitHub repo size](https://img.shields.io/github/repo-size/Fulanodtals/GameCursor?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Fulanodtals/GameCursor?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Fulanodtals/GameCursor?style=for-the-badge)



### Sobre o projeto

O projeto GameCursor criado por [Fulanodtals](https://github.com/Fulanodtals) possibilita que você controle e 
execute ações com o mouse apartir de um controle, como click, dubble click, click direito, arrastar, selecionar, 
Veja mais sobre o projeto [aqui](#sumario)

<img src="./readme_assets/window.png" alt="Imagem do programa">

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [x] criar conexao com o controle
- [x] criar arquivo para guardar valores
- [x] criar janela de gerenciamento
- [ ] opcao de modificar teclas na janela
- [ ] outras utilidades...



<div id='sumario'/>

*******
## Sumário da documentação

Aqui esta linkado as partes do projeto que deseja ver:

* **[Informações iniciais](#introducao)**
* **[Instalação](#instalacao)**
* **[Controller]()**
* **[Settings]()**
* **[Main]()**
* **[Arquivo.vbs]()**
* **[Buttons]()**   
*******


<div id='introducao'/>

##  Informações iniciais

O GameCursor é organizado com POO, utilizando bibliotecas como pygame, pyautogui e PyQt6.<br> 
Sendo separado por tres arquivos principais:
* main.py - Arquivo principal onde tem a janela do programa
* controller.py - Classe que gerencia as ações do controle
* settings.py - Classe que interage com o arquivo config.txt

E outros arquivos como:

* GameCursor.vbs - arquivo que inicia o programa
* settings.py - programa para testes de teclas

Os tres primeiros são os principais que controlam, configuram e gerenciam o programa;
Os outros dois podem ser usados também, principalmente o GameCursor.vbs mostrado na [Instalacao](#instalacao).

Abaixo esta um exemplo de ação com o mouse, usando o GameCursor

<img src="./readme_assets/precionando.gif" >



<div id='instalacao'/>

## Instalação
Você de principio pode dar um git clone neste repositorio para uma pasta desejada:<br>
```bash
   git clone https://github.com/Fulanodtals/GameCursor.git
```
Acessando a pasta, voce pode excluir alguns arquivos, exceto os listados abaixo que são necessarios para o programa funcionar
e não devem ser deletados! São eles:

* main.py
* controller.py
* settings.py
* config.txt
* icon.png

E o arquivo de inicialização

* GameCursor.vbs

Os outros arquivos porem ser deletados.<br>
Para o programa funcionar você deve executar o arquivo main.py, e ha algumas possibilidades para facilitar que ele se
inicie, vou mostrar algumas delas:


### Por meio do arquivo .vbs
Você pode usar o **GameCursor.vbs** para executar o programa, apenas troque a parte <arquivo_main> pelo caminho do arquivo
main.py presente na pasta do projeto.

Apos isso ao executar o **GameCursor.vbs** ele ira iniciar o arquivo main.py, o que permite colocar este arquivo em varios lugares
como no Desktop, barra de tarefas e principalmente na pasta de inicializar:

Ao colocar o **GameCursor.vbs** na pasta de iniciar, o programa ira iniciar junto com o computador, segue como fazer isso:

Precione a tecla `win + r` e digite:
```shell
  shell:startup
```
e por fim cole o arquivo GameCursor.vps na pasta e o programa ira iniciar assim que o computador for ligado

(delay provável de 30-60 segundos)

> IMPORTANTE! <br>
> O programa inicia uma busca por controles antes de ser executado totalmente;<br>
> para cancelar essa busca precione `Ctrl + Shift + Esc` e finalize a tarefa.

<br>

******

<div id='instalacao'/>
   
## Controller

<p id='instalacao'></p> <!gambiarra para linkar->

## ☕ Usando <nome_do_projeto>

Para usar <nome_do_projeto>, siga estas etapas:

```
<exemplo_de_uso>
```

Adicione comandos de execução e exemplos que você acha que os usuários acharão úteis. Forneça uma referência de opções para pontos de bônus!

## 📫 Contribuindo para <nome_do_projeto>

Para contribuir com <nome_do_projeto>, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://avatars3.githubusercontent.com/u/31936044" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Iuri Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://s2.glbimg.com/FUcw2usZfSTL6yCCGj3L3v3SpJ8=/smart/e.glbimg.com/og/ed/f/original/2019/04/25/zuckerberg_podcast.jpg" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Mark Zuckerberg</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 😄 Seja um dos contribuidores

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

https://github.com/iuricode/readme-template/blob/main/repositorio/exemplo-01.md
