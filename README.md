# Assistente de Aulas de Inglês

Este projeto foi desenvolvido com o objetivo de criar uma assistente virtual para ajudar meu primo, que recentemente começou a dar aulas de inglês. Ele tem dificuldades em guiar as aulas de maneira eficiente e, para isso, o sistema foi criado para gerar tópicos e sugestões baseadas no que ele fala durante a aula.

## Como Funciona

O assistente utiliza captura de áudio em tempo real para ouvir a fala do professor durante a aula. A transcrição do áudio é feita e, com base nela, o assistente gera respostas com sugestões de tópicos, explicações ou ideias que podem ser usadas para desenvolver a aula de maneira mais fluída e eficaz.

## Funcionalidades

- **Gravação de Áudio em Tempo Real**: O sistema capta o áudio da sala de aula em tempo real, utilizando o microfone configurado.
  
- **Transcrição de Áudio para Texto**: A fala do professor é transcrita automaticamente para texto, para que o assistente possa analisar.

- **Geração de Respostas com Base na Transcrição**: A partir do texto transcrito, o assistente gera respostas com tópicos e ideias que podem ser utilizados para continuar ou enriquecer a aula.

- **Interação Dinâmica**: O assistente responde de forma dinâmica e em tempo real, fornecendo sugestões à medida que a aula avança.

## Tecnologias Utilizadas

- **Google Gemini (LLM)**: Utilizado para gerar respostas com base nos tópicos falados pelo professor.

- **Faster Whisper**: Utilizado para transcrever áudio em texto.

- **SoundDevice**: Biblioteca para captura de áudio em tempo real.

- **Scipy**: Para salvar o áudio gravado no formato WAV.

## Como Executar

1. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt

2. **Crie um arquivo .env e adicione a sua chave da API do Google Gemini**:

   ```bash
   GEMINI_API_KEY=sua_key
   
3. **Execute**:

   ```bash
   main.py
   
4. **Apartir dai o assistente começará a ouvir a aula e transcrever as melhores rotas para conduzir a aula e auxiliar o professor para melhor proveito da aula.**

---

## **Licença**
Este projeto está licenciado sob os termos da [Licença MIT](https://opensource.org/licenses/MIT).
