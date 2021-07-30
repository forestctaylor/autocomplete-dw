import './App.css';
import React, { useState } from 'react';

function AutocompleteSearchBar() { 
  const [searchSuggestions, setSearchSuggestions] = useState([]);

  function getSearchSuggestions(e) { // On input change, get suggestions & update global searchSuggestions list
    const searchString = e.target.value;
    //console.log(`Searching for ${searchString}`);

    var xhr = new XMLHttpRequest();

    xhr.onload = function (response) {
      console.log(`${xhr.status}: ${xhr.response}`);
      const suggestion = xhr.response;
      setSearchSuggestions(searchSuggestions => [...searchSuggestions, suggestion])
    };

    xhr.open('POST', 'http://localhost:5000/getSearchSuggestions');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
    xhr.send(searchString); // TODO: JSON.stringify({searchString: searchString})
  }
  
  return (
    <div>
      <input className="App-input" type="text" name="search" onChange={getSearchSuggestions}/>
      <ul>
        {searchSuggestions.map(suggestion => <li className="App-li">{suggestion}</li>)}
      </ul>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <form>
          <label className="App-label">
            Please search below!
          </label>    
          <AutocompleteSearchBar/>
        </form>
        </header>
    </div>
  );
}

export default App;
