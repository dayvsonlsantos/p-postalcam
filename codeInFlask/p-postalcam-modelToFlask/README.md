<h4 align="center"> 
	Dataset para o modelo de IA do Postalcam
</h4>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Sobre

<p align=justify>Para utilizar essa base, é necessário acessar o **[Teachable Machine](https://teachablemachine.withgoogle.com/train/image)**</p>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/16d7c222-81dd-46e5-bb01-94eb7057d0f3) Como criar o modelo ?

### 1° Instale o python 3 e crie um ambiente venv dentro de p-postalcam-modelToFlask

### 2° Execute o arquivo createModel.py
```bash
python createModel.py
```
##### Obs: No linux use: python3 createModel.py
##### Obs: As imagens para treino estão em codeInFlask/p-postalcam-modelToFlask/Dataset/train/*/, pode adicionar outras se desejar, porém respeite os nomes e quantidade de pastas dentro de train.

### 3° O modelo será salvo na pasta Model, pasta copia-lo e usa-lo onde desejar
##### Obs: No p-postalcam-flask, basta colocar o modelo dentro da pasta Model.

### 4° Para testar o modelo
```bash
Abra o arquivo testModel.py, e em image_path, coloque o endereço da imagem que deseja testar
```
##### Obs: Para teste, consta alguns exemplos em ./Dataset/test/

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
