<h4 align="center"> 
	Postalcam
</h4>

<p align="center">
 <a href="#-Sobre">Sobre</a> •
 <a href="#-Instalação">Instalação</a> •
 <a href="#-Funcionalidades">Funcionalidades</a> •
 <a href="#-Tecnologias">Tecnologias</a> • 
 <a href="#-Autores">Autores</a> • 
 <a href="#-Licença">Licença</a>
</p>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Sobre

<p align=justify>O <b>Postalcam</b> é uma aplicação web responsiva desenvolvida como projeto de conclusão para a <b>residência de software</b> com a <b>Accenture</b>, proporcionada pelo programa <b>Embarque Digital</b>, da <b>prefeitura do Recife</b>, juntamente com a <b>Faculdade Senac PE</b>, em 2024. Trata-se de uma aplicação que utiliza IA para resolver a dificuldade de não saber quando há uma entrega à sua porta. Com uma câmera apontada para a entrada, a IA analisa quando alguém se aproxima carregando uma encomenda e alerta o usuário na própria página </p>

<p>A versão inicial, conta com duas opções de tecnologias, flask (localizado em codeInFlask) e JS (localizado em codeInJS).</p>

## Observação:

- **Versão MVP 1.0:**
    - **Item 1:** Alerta o usuário na <b>própria página</b> quando uma entrega está sendo feita.


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Instalação

#### 1° Instale o python 3 e crie um ambiente venv dentro de p-postalcam-flask

#### 2° Instale as dependências. Obs: use pip3 no Linux
```bash
pip install tensorflow keras opencv-python numpy scikit-learn flask
```

#### 3° Execute o comando abaixo
```bash
flask run
```
#### Acesse o link disponibilizado pelo terminal.


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Funcionalidades

- [x] Com uma camera conectada ao computador e permissão concedida:
	  
   - [x] Ver as imagens ao vivo da camera
   - [x] Detectar pessoas, pacotes e pessoas com pacotes
   - [x] Alertar quando uma pessoa com pacote for detectada, exibindo ao log
   - [x] Log com imagem registrada, data e horário



## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Tecnologias

-   **[Python](https://www.python.org/)**
-   **[HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)**
-   **[CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)**
-   **[Tailwind CSS](https://tailwindcss.com/)**
-   **[Flask](https://flask.palletsprojects.com/en/3.0.x/)**

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Autores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/dayvsonlsantos">
        <img alt="" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/102249811?s=400&u=2843e9ff654eb5587f9e6ad6b873fed0b1c0df77&v=4" width="100px;" alt=""/>
        <br />
        <sub><b>Dayvson Lima</b></sub>
   </td>
   
   <td align="center">
      <a href="#">
        <img alt="" style="border-radius: 50%;" src="https://github.com/dayvsonlsantos/p-near-hospital/assets/102249811/a01154cd-50fb-4cad-96e9-c74a1276586b" width="100px;" alt=""/>
        <br />
        <sub><b>Daniel Oliveira</b></sub>
   </td>
   
 </tr>
   
</table>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Licença

O projeto se encontra sob a licença [GPLv3](https://github.com/dayvsonlsantos/p-postalcam/blob/feature/LICENSE).
