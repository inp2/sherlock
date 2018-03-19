import React, { Component } from 'react';
import './Navbar.css';
import logo from './edited_logo.png';

class Navbar extends Component {
  render() {
      return (
        <div className="Nav">
          <header className="App-header">
            <h1>
              <center>
                <img className="logo" src={logo} alt="logo" height={80} width={80} />
                Sherlock 
              </center>
            </h1>
          </header>
        </div>
      )
  }
}

export default Navbar
