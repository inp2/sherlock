import React, { Component } from 'react';
import './App.css';
import Header from './Header.js';

class App extends Component {
  render() {
    return(
      <div className="App">
        <Header/>
        
        <p>
          <center> Choose a file to analyze
          <form enctype="multipart/form-data" action="/upload/image" method="post">
            <input id="image-file" type="file" />
          </form>
          </center>
        </p>
      </div>
    )
  }
}

export default App;
