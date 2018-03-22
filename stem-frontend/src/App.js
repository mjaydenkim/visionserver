import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import ImgUploader from './ImgUploader'
class App extends Component {
  render() {
    return (
      <div className="App">
        <ImgUploader/>
      </div>
    );
  }
}

export default App;
