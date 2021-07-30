import './App.css';

function App() {

  function getSearchSuggestions(e) {
    const searchString = e.target.value;
    console.log(`Searching for ${searchString}`);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/getSearchSuggestions');
    xhr.onreadystatechange(function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        console.log('SUCCESS');
        // PROCESSING
      }
    });
    xhr.send(searchString);
  }

  return (
    <div className="App">
      <header className="App-header">
        <form>
          <label className="App-label">
            Please search below!
          </label>
          <input className="App-input" type="text" name="search" onChange={getSearchSuggestions}/>
        </form>
        </header>
    </div>
  );
}

export default App;
