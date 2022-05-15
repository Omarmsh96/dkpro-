/////frontend

  /* Handle text functions */
  handleText = (event) => {
    const text = event.target.value
    this.setState({ text: text});
    Streamlit.setComponentValue(this.text)
  }
  submitText = () => {

    const url = 'http://localhost:3001/pos';

    const setData = {
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Accept':'application/json',    
        'Content-Type': "application/json; charset=utf-8",
      },
      body: JSON.stringify({text: this.state.text}), //post data to api .. strin convert js obj to json string 
      
    }
    
    fetch(url, setData)
      .then(response => response.json()) // receive data ..response the object of json then convert to js obj through res.json 
      .then(data => {
        this.AddMarkup(data);
      })
  }


///backend

const Express = require('express');
const bodyParser = require('body-parser');
const tokenizer = require('wink-tokenizer');
const posTagger = require( 'wink-pos-tagger' );
 
const PORT = process.env.PORT || 3001;

const app = Express();
var cors = require('cors');
const Tagging = posTagger();

app.use(bodyParser.json());

app.options('/pos', cors());

app.post('/pos', cors(), (req, res) => {
  console.log('got api request');

  const text = req.body.text;

  const taggedText = Tagging.tagSentence(text);

  res.json(taggedText);
})


app.listen(PORT, (err) => {
  if (err) throw err;

  console.log(`now listening on port ${PORT}`);
})