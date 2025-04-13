<div id='home'/>

# GameCursor


![GitHub repo size](https://img.shields.io/github/repo-size/Fulanodtals/GameCursor?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Fulanodtals/GameCursor?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Fulanodtals/GameCursor?style=for-the-badge)



### Sobre o projeto

O projeto GameCursor criado por [Fulanodtals](https://github.com/Fulanodtals) possibilita que você controle e 
execute ações com o mouse apartir de um controle, como click, dubble click, click direito, arrastar, selecionar e outros.<br> 
Instale o programa [aqui](#instalacao)<br>


## veja o Tutorial:
<a href="https://www.youtube.com/watch?v=awqex2CtUkk">
  <img src="https://img.youtube.com/vi/awqex2CtUkk/hqdefault.jpg">
</a>

<br>
<br>

## Utilidades:
A seguir esta listado tudo o que o programa consegue fazer:

* A|X = click esquerdo
* B|O = click direito
* X|□ = click duplo
* Y|△ = selecionar
* L3 = controla o cursor
* R3 = controla o scroll
* RB|R1 = aumenta a velocidade do cursor
* LB|L1 = diminui a velocidade do cursor
* menu + start = pausa/dispausa o programa

 <br>
 
<!--
### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [x] criar conexao com o controle
- [x] criar arquivo para guardar valores
- [x] criar janela de gerenciamento
- [ ] suavilizar a movimentacao do mouse
- [ ] opcao de modificar teclas na janela
- [ ] otimizar
- [ ] outras utilidades...
-->

<!--
<div id='sumario'/>

*******
## Sumário da documentação

Aqui esta linkado as partes do projeto que deseja ver:

* **[Informações iniciais](#introducao)**
* **[Instalação](#instalacao)**
* **[Controller](#controller)**
* **[Settings](#settings)**
* **[Main](#main)**
* **[Arquivo.vbs](#arquivovbs)**
* **[Buttons](#buttons)**   
*******
-->

<div id='introducao'/>

##  Informações iniciais do projeto

O GameCursor é organizado com POO, utilizando bibliotecas como pygame, pyautogui e PyQt6.<br> 
Sendo separado por alguns arquivos principais:

* GameCursor.vbs - arquivo que inicia o programa
* main.py - Arquivo onde tem a janela do programa
* controller.py - Classe que gerencia as ações do controle
* settings.py - Classe que interage com o arquivo config.txt
* config.txt - arquivo que guarda as velociades do cursor

Os tres primeiros são os principais que controlam, configuram e gerenciam o programa;
Os outros dois podem ser usados também, principalmente o GameCursor.vbs mostrado na [Instalacao](#instalacao).

Quando o programa é iniciado(pelo arquivo main.py) é feita uma varredura de controles, ou seja, o programa so
ira iniciar realmente quando um controle for conectado; se o controle for desconectado, o programa devera ser
reiniciado!

> ATENCAO:<br>
> A varredura de controle é feita a cada 10s

Abaixo esta um exemplo de ação com o mouse, usando o GameCursor

<img src="./readme_assets/precionando.gif" >



<div id='instalacao'/>

## Instalação
Você de principio pode dar um git clone neste repositorio para uma pasta desejada:<br>
```bash
git clone https://github.com/Fulanodtals/GameCursor.git
```
Eu recomendo ver as [Recomendações](#recomendacoes) após copiar os arquivos.<br>
Acessando a pasta, você pode excluir alguns arquivos, exceto os listados abaixo que são necessarios para o programa funcionar
e não devem ser deletados! São eles:

* main.py
* [Veja o script principal](main.py)
* controller.py
* settings.py
* config.txt
* icon.png

E o arquivo de inicialização

* GameCursor.vbs

Os outros arquivos podem ser deletados. Veja [Recomendações](#recomendacoes)<br>
Para o programa funcionar você deve executar o arquivo main.py(ou controller.py), e ha algumas possibilidades para facilitar que ele se
inicie, vou mostrar algumas delas:

### Apenas executando
Nao é recomendado criar um .exe do arquivo principal, tanto por causa do windows defender quando pela má adaptação.
entao apenas clique com o botao direito no main.py, mas claro eu recomendo usar o arquivo .vbs por ser mais prático.

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
e por fim cole o arquivo **GameCursor.vps** na pasta e o programa ira iniciar assim que o computador for ligado

(delay provável de 30-60 segundos)

> IMPORTANTE! <br>
> O programa inicia uma busca por controles antes de ser executado totalmente;<br>
> para cancelar essa busca precione `Ctrl + Shift + Esc` e finalize a tarefa.



*******

<div id='recomendacoes'/>

# Recomendações!!!
Eu recomendo você executar apenas o controller.py, por gastar menos memoria ao ser executado.
Então se preferir assim, mantenha apenas os seguintes arquivos:

* controller.py (Obvio)
* settings.py
* config.txt

Excluindo os outros arquivos; Ao executar o controller.py o programa ira executar em segundo plano normalmente e só
ira parar ao desconectar o controle.<br>
Claro, coloque deve colocar o caminho deste arquivo no local indicado no arquivo GameCursor.vbs

<br>
<br>
<br>

Obrigado por usar o programa
